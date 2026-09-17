---
name: anti-ai-pass
description: "Strip AI tells from your copy on a BUDGET: hard-ban tell words (quietly, silently, leverage, actually...), allow at most ONE structural move (Most-people / Not-X-Y / Everyone-wants-X) per post and only when it carries real specifics, ban stacking two or more. Runs automatically after every draft in every writing skill. Deterministic linter (scripts/lint.py) for the mechanical catches + a judgment layer for the structural budget. NOT an anti-detection tool; it's a taste + voice gate."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** this skill enforces the `# FOLLOW THIS WRITING STYLE` rules in
`<BRAND_DIR>/writing-style.md` plus your own anti-AI tell list. It is the final
gate, run AFTER a funnel skill has drafted, before the draft is shown to you.

# Anti-AI pass (budgeted)

Every draft you write (LinkedIn, Substack, email, captions) runs through this
pass before you see it. Two tiers, one deterministic and one judgment.

## The approach: BUDGETED, not absolute

Your own top posts USE these structures: "Everyone wants to be AI-first. Nobody wants
to fix the data." (4,509 likes), "Most builders don't have an agent problem..." (2,734),
"That's not a feature. That's a risk." An absolute ban would delete your best hooks. So
the rule is a budget, not a prohibition:

- **Taste words: hard-banned, always, no exceptions.** These read as AI/marketing tells
  to human readers too. Remove every one. No judgment call.
- **Structural moves: at most ONE per post, and only when it carries real specifics.**
  The move is fine as the scroll-stopping hook. What reads as machine is STACKING two,
  three, four of them in one post with generic filler between and nothing un-generatable.
  Your real posts use one move then fill the body with details only you could write
  (the data-swamp line, "for roughly 48 hours," a real API bill). The AI drafts stacked
  four hollow moves. Same patterns, opposite outcome — the difference is stacking +
  specificity, not the pattern existing.

> One-line test: does the post lean on the STRUCTURE to feel smart, or on a real specific
> only you could supply? Structure carrying the weight = AI. Specific carrying it =
> you. One structural move is a frame; two+ is a crutch.

## Procedure (run every time, automatically — never wait to be asked)

### 1. Run the deterministic linter first
```bash
python3 .claude/skills/anti-ai-pass/scripts/lint.py <draft-file>
# or:  echo "<draft text>" | python3 .../lint.py --stdin
# or:  python3 .../lint.py --json <file>   (machine-readable)
```
Exit 0 = clean (no hard hits, structural moves <= 1). Exit 1 = needs work. The linter
reports: HARD banned words/phrases (always remove), structural move COUNT (budget = 1),
and rhythm flags (-ing tails, rule-of-three, em dashes).

The linter is mechanical and will over- and under-catch. It is the floor, not the
ceiling. It cannot tell whether the one kept structural move earns its place — that's
step 2.

### 2. Apply the judgment layer (what the linter can't)
- **Every HARD hit: remove it.** Replace with the plain word you'd say out loud.
  "quietly released" -> "released". "leverage X" -> "use X". "actually" -> cut it.
  ("harness" is NOT banned as a word — "agentic harness" / "eval harness" is your real
  domain vocabulary. Only the marketing phrase "harness the power/potential of X" is banned.)
- **Structural moves == 0:** fine, ship (if the specificity gate below passes).
- **Structural moves == 1:** keep it ONLY if the post also carries >=2 un-generatable
  specifics (a real number, named breakage, dated moment, a person, a lived detail). A
  structural hook on a post full of generic claims is still AI — the move was supposed to
  frame a specific, not replace one. If there's no specific behind it, cut the move to
  plain prose or (better) ask for the missing specific. Never invent one.
- **Structural moves >= 2 (budget blown):** keep the strongest ONE (usually the hook),
  rewrite the others as plain sentences. See the worked example below.

### 3. Rhythm / structural tells (from your list + <BRAND_DIR>/reads-human.md)
Flag and fix even when the linter is silent:
- **Rule of three** ("Agents. Automations. Orchestration layers."). Cut to two or expand
  to four+. Groups of exactly three are a tell.
- **-ing tails** at sentence ends (highlighting, showcasing, demonstrating). Rewrite as a
  real clause.
- **Fancy verbs for "is"** (serves as, stands as, represents, embodies). Use "is".
- **Banned transitions** (Additionally, Furthermore, Moreover, Consequently). Delete or
  replace with how you'd actually connect the thought.
- **Wrap-up summary at the end** ("In conclusion...", a tidy bow). Cut it; end on the jab.
- **Em/en dashes.** Never. Commas, periods, parentheses.
- **Rhetorical question answered immediately.** State the point directly.

### 4. Specificity gate (the real anti-AI move, per <BRAND_DIR>/reads-human.md)
The structural budget kills the surface tell; specificity is what actually makes it read
as you. Before shipping, count details ONLY you could have supplied:
- TOFU: >= 2. MOFU: >= 3, one shown as a scene.
- If it can't clear the bar, **ask for the specific — never fabricate one.** A made-
  up specific is a lie and usually reads AI anyway.

### 5. Read it out loud (the final human check)
"If you would not say it out loud, do not write it." A line that sounds like a poster,
a press release, or a LinkedIn-guru caption gets cut or folded into a real sentence.

## Worked example (budget blown -> budgeted)

Your real 4,509-like post stacks 2 moves (linter flags it):
> Everyone wants to be "AI-first". Nobody wants to fix the data. [wants_split]
> ... That's not a feature. That's a risk. [binary_flip]

Budgeted fix — keep the hook (move #1, it's the scroll-stopper), rewrite the ending flip
as plain prose:
> Everyone wants to be "AI-first". Nobody wants to fix the data.
> ...
> Point AI at a mess like that and it runs the same broken process faster, and the wrong
> answers come out looking polished enough to trust.

The insight still lands. It lands through a plain sentence with a concrete image, not a
fourth "not X, it's Y." One move, carried by specifics. That's the target.

## How this wires into the writing skills

Every drafting skill (`tofu-orchestrator` and its 8 archetype skills) runs
this pass as the LAST step before showing you the draft, in the same turn, unprompted.
The skills' own examples still teach the signature moves — this pass just enforces the
budget on top so a draft never ships with the moves stacked or the tell-words in.

## Pitfalls
- **Don't over-apply to your PROVEN hooks.** One structural move IS allowed. The linter
  flagging a single move as "verify" does not mean delete it — it means confirm a specific
  sits behind it. Deleting every hook turns your voice into flat oatmeal; that's the
  absolute path you explicitly rejected.
- **Don't fabricate a specific to pass the specificity gate.** Ask instead. Fabrication is
  the worse failure — see the multiple real fabrication incidents logged in
  `your own content-ops notes`.
- **The linter is a STYLE gate, not anti-detection.** Per `<BRAND_DIR>/reads-human.md`, you cannot
  beat a neural detector (Pangram) with a word list, and chasing that is a treadmill.
  This exists so the copy reads like you to a human, which is the same job as killing
  the fingerprint — but the goal is voice, not evasion. Don't sell it as detector-proofing.
- **Regex over/under-catches.** "everyone" mid-sentence is not always a crowd-split;
  "most people" in a quoted source is not your move. Read the flag, don't obey it
  blindly.

## Verification
- [ ] Linter run, exit code checked. Every HARD hit removed (re-run to confirm 0).
- [ ] Structural moves <= 1, and the one kept has >= 2 specifics behind it.
- [ ] Rhythm tells (rule-of-three, -ing tails, em dashes, wrap-up bow) fixed.
- [ ] Specificity gate met for the funnel stage, or the missing specific was asked for.
- [ ] Read out loud once; nothing sounds like a poster.
