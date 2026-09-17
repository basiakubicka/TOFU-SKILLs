#!/usr/bin/env python3
"""
Deterministic anti-AI linter for your content.

Two tiers:
  HARD  -- banned words/phrases: any hit is a defect, always remove. No judgment.
  STRUCT-- structural AI moves: counted, not auto-failed. The BUDGET rule is
           "at most ONE structural move per post, and only if it carries real
           specifics." This script COUNTS them and flags when the budget (>1) is
           exceeded; a human/model still judges whether the one that's kept earns
           its place. Stacking (2+) is the machine tell and is always flagged.

Usage:
  python3 lint.py path/to/draft.txt
  python3 lint.py --stdin  < draft.txt
  echo "text" | python3 lint.py --stdin
  python3 lint.py --json path/to/draft.txt     # machine-readable

Exit code: 0 if clean (no HARD hits and structural budget not exceeded),
           1 if any HARD hit OR structural moves > 1 (budget blown).
This is a STYLE gate, not an anti-detection tool -- see SKILL.md.
"""
import sys, re, json, argparse

# ---- TIER 1: HARD BANS (always remove) ----------------------------------
# Single words. Word-boundary, case-insensitive. Kept as a taste layer:
# these read as AI/marketing tells to human readers too.
HARD_WORDS = [
    # your explicit adds -- the drafts' actual tells
    "quietly", "silently",
    # your ban list + the classic AI-vocabulary set
    "delve", "realm", "unlock", "tapestry", "paradigm",
    "cutting-edge", "revolutionize", "revolutionise", "landscape", "intricate",
    "crucial", "pivotal", "meticulously", "vibrant", "unparalleled", "leverage",
    "synergy", "innovative", "game-changer", "gamechanger", "testament",
    "groundbreaking", "foster", "showcase", "enhance", "holistic", "pioneering",
    "unleash", "transformative", "seamless", "empower", "streamline", "elevate",
    "effortless", "unprecedented", "reimagine", "actually", "shift", "shifted",
    "utilize", "utilise", "moreover", "furthermore", "additionally",
    "consequently", "boost", "skyrocket", "profound", "nestled", "boasts",
    "vital", "notably", "importantly", "ultimately", "essentially",
    "fundamentally", "remarkable",
]

# Multi-word banned phrases (substring, case-insensitive, whitespace-flexible).
HARD_PHRASES = [
    "whole game", "this is the part", "nobody talks about", "turns out",
    "heavy lifting", "and honestly", "here's why i think",
    "here's what that means", "at the end of the day", "when it comes to",
    "in a world where", "make no mistake", "let me be clear",
    "the real question is", "at its core", "in reality", "what really matters",
    "the deeper issue", "the heart of the matter", "let's dive in",
    "let's explore", "let's break this down", "here's what you need to know",
    "without further ado", "needle", "move the needle", "double down",
    "deep dive", "circle back", "take a step back", "lean into",
    "harness the power", "harness the potential", "harness the full",
]

# ---- TIER 2: STRUCTURAL MOVES (budget = 1) ------------------------------
# Each returns a list of matched snippets. The BODY of the post may contain at
# most ONE of these total (the hook's move counts). 2+ = stacking = machine tell.
def _find(patterns, text, flags=re.I):
    out = []
    for p in patterns:
        for m in re.finditer(p, text, flags):
            out.append(m.group(0).strip())
    return out

def struct_moves(text):
    # Order matters: the paired "Everyone wants X / Nobody wants Y" hook is ONE
    # move. Detect it FIRST and mask its span so the generic everyone/nobody
    # crowd-split patterns below don't double-count the same two lines.
    moves = {}
    masked = text

    # "Everyone wants X. Nobody wants Y." (the paired hook) -- one move
    ws = _find([
        r"\beveryone wants\b[^.\n]{0,50}[.\n]\s*(?:almost )?nobody wants\b[^.\n]{0,50}",
    ], masked)
    if ws:
        moves["wants_split"] = ws
        masked = re.sub(
            r"\beveryone wants\b[^.\n]{0,50}[.\n]\s*(?:almost )?nobody wants\b[^.\n]{0,50}",
            " ", masked, flags=re.I)

    # "It's not X. It's Y." / "Not X. Y." binary flip and triple reveal
    bf = _find([
        r"(?m)^\s*not\s+[^.\n]{1,60}\.\s*$",          # a line that is just "Not X."
        r"it'?s not [^.,\n]{1,50}[.,]\s*it'?s\s+[^.\n]{1,50}",
        r"that'?s not [^.,\n]{1,40}[.,]?\s*(?:that'?s|it'?s)\s+[^.\n]{1,40}",
    ], masked)
    if bf:
        moves["binary_flip / not-x-y"] = bf

    # "Most people X. The few who Y." / crowd splits (on the masked text, so the
    # wants-hook's own everyone/nobody lines are excluded)
    cs = _find([
        r"\bmost (?:people|orgs|organizations|founders|builders|teams|companies)\b[^.\n]{0,80}",
        r"\bthe (?:ones|few|people) who\b[^.\n]{0,60}",
        r"\bnobody\b[^.\n]{0,40}\.\s",
        r"\beveryone\b[^.\n]{0,40}\.\s",
    ], masked)
    if cs:
        moves["crowd_split / most-people"] = cs

    # "Stop doing X. Start doing Y." switch
    moves["stop_start_switch"] = _find([
        r"\bstop [^.\n]{1,40}[.\n]\s*start [^.\n]{1,40}",
    ], masked)
    # "You don't need X. You need Y." minimalist smack
    moves["dont-need"] = _find([
        r"\byou don'?t need [^.\n]{1,50}[.\n]\s*you need [^.\n]{1,50}",
    ], text)
    # "If you're not doing X, you're already behind" FOMO
    moves["fomo_behind"] = _find([
        r"if you'?re not [^.\n]{1,50}(?:behind|falling behind|too late)",
    ], text)
    # "Here's the truth nobody tells you" fake reveal
    moves["fake_reveal"] = _find([
        r"here'?s the (?:truth|secret|part)[^.\n]{0,40}",
        r"nobody (?:tells|talks about|mentions)[^.\n]{0,40}",
    ], text)
    # drop empties
    return {k: v for k, v in moves.items() if v}

# ---- structural / rhythm tells that are always worth flagging (soft) ----
def rhythm_flags(text):
    flags = {}
    # -ing tails at sentence ends
    ing = re.findall(r"\b\w+ing\b[.,]", text)
    ing = [w for w in ing if w.lower().rstrip(".,") not in
           ("thing","something","nothing","everything","morning","evening","during")]
    if ing:
        flags["ing_tails"] = ing
    # Rule of three: three short comma/period fragments in a row (e.g. "Agents. Automations. Orchestration.")
    r3 = re.findall(r"(?:\b[A-Z][a-z]+\.){3}", text)
    if r3:
        flags["rule_of_three"] = r3
    # em dashes
    if "\u2014" in text or "\u2013" in text:
        flags["em_or_en_dash"] = ["\u2014/\u2013 present"]
    return flags

def analyze(text):
    low = text.lower()
    hard_word_hits = []
    for w in HARD_WORDS:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", text, re.I):
            hard_word_hits.append(m.group(0))
    hard_phrase_hits = [p for p in HARD_PHRASES if p in low]
    moves = struct_moves(text)
    move_count = len(moves)  # count of DISTINCT move types present
    rhythm = rhythm_flags(text)
    clean = (not hard_word_hits) and (not hard_phrase_hits) and move_count <= 1
    return {
        "hard_word_hits": hard_word_hits,
        "hard_phrase_hits": hard_phrase_hits,
        "structural_moves": moves,
        "structural_move_count": move_count,
        "budget_exceeded": move_count > 1,
        "rhythm_flags": rhythm,
        "clean": clean,
    }

def render(res):
    L = []
    if res["hard_word_hits"]:
        L.append(f"HARD banned words ({len(res['hard_word_hits'])}): " +
                 ", ".join(sorted(set(w.lower() for w in res['hard_word_hits']))))
    if res["hard_phrase_hits"]:
        L.append(f"HARD banned phrases: " + ", ".join(res['hard_phrase_hits']))
    mc = res["structural_move_count"]
    if mc == 0:
        L.append("Structural moves: 0 (fine)")
    elif mc == 1:
        k = list(res["structural_moves"])[0]
        L.append(f"Structural moves: 1 ({k}) -- within budget IF it carries real specifics. Verify.")
    else:
        L.append(f"Structural moves: {mc} -- BUDGET EXCEEDED (max 1). Stacking is the machine tell. Keep one, rewrite the rest:")
        for k, v in res["structural_moves"].items():
            L.append(f"    - {k}: {v[0][:70]}")
    if res["rhythm_flags"]:
        for k, v in res["rhythm_flags"].items():
            L.append(f"rhythm: {k} -> {v[:4]}")
    L.append("VERDICT: " + ("CLEAN" if res["clean"] else "NEEDS WORK"))
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--stdin", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.stdin or not a.path:
        text = sys.stdin.read()
    else:
        text = open(a.path, encoding="utf-8").read()
    res = analyze(text)
    print(json.dumps(res, ensure_ascii=False, indent=2) if a.json else render(res))
    sys.exit(0 if res["clean"] else 1)

if __name__ == "__main__":
    main()
