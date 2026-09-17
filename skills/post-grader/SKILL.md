---
name: post-grader
description: "Use when grading a finished LinkedIn post. Runs checklist."
user-invocable: true
metadata:
  hermes:
    editorial_name: "Post Grader"
    editorial_description: "Grades a finished LinkedIn post against your data-validated hook/body/structure checklist, check by check."
---

# Post Grader — structured recheck of a finished post

Use when the user pastes a finished/already-written post (your own, or someone
else's, e.g. a reference/competitor post) and asks how it would score, what to fix,
or for a grade/review. NOT for drafting a new post — use the archetype-specific
the `tofu-*` drafting skills for that (they already have the same checks
built into their draft loop).

This skill exists because grading a post freeform, from memory of the rules, is
where real misses happen — e.g. approving a hook that previews a count but also
states the full outcome, because "opens a loop" was pattern-matched loosely instead
of tested precisely. Forcing the checks in order, with an explicit pass/fail line
for each, is the whole value of this skill. Don't skip a check because the post
"obviously" passes it.

**This skill does not contain the rules themselves.** Every check below points at
`<BRAND_DIR>/hook-floor-check.md` — read that file fresh each time (don't rely on
memory of it from earlier in the conversation; it gets updated as new findings land).
If a claim here and in that file ever disagree, the file wins.

## Procedure (run in this exact order, do not reorder or skip)

### Step 0 — classify
- Which funnel: TOFU or MOFU?
- Which archetype/family: contrarian, conceptual_explainer, how-to, news-breakdown,
  resource_roundup, relatable_mirror, surprising_number, meme (TOFU) — or
  personal_story, opinion_stance, tactical_how-to, relatable_mirror (MOFU)?
- Which STRUCTURE family does that archetype map to for the attention-mechanic
  checks: story / argument / teach / list / reframe? (see the family table in
  `hook-floor-check.md`'s "How attention is actually held" section — MOFU personal
  narratives and MOFU tactical how-to both map to `story`; contrarian and MOFU
  opinion-stance map to `argument`; explainer/how-to/news-breakdown map to `teach`;
  resource roundup and meme map to `list`; relatable mirror maps to `reframe`.)

State the classification explicitly before scoring anything — every check after
this depends on knowing the family.

### Step 1 — hook + rehook checks (line 1 through the fold, ~lines 2-5)
Run each of these as its own pass/fail, quoting the actual hook text each time:
1. **Opens a real loop?** Apply the count-vs-outcome sub-check explicitly: after
   reading the hook, can the reader already state what the post proves/delivers in
   their own words? If yes, it fails this check even if a count/list was previewed.
2. **Loop still open at the end of the fold** (not resolved by line 4-5)?
3. **Concrete, not abstract** — named person/number/scene vs generic nouns?
4. **Direct address appropriate for this archetype's baseline** (check the
   per-archetype table — don't force "you/your" where the archetype runs
   third-person, e.g. News Breakdown)?
5. **Register matches the archetype** (casual/punchy vs essayistic — check baseline)?
6. **Hook TEMPLATE reliability tier** — name the template used (direct_challenge,
   most_people_think_X, bare_claim, number_stat_lead, list_lead, personal_confession,
   question_lead, other) and state its high%/low% from the reliability table. If it's
   `question_lead` or anything not in the reliable tier, flag it as a variance/gamble
   choice explicitly, don't silently treat it as equal to a reliable-tier pick.

### Step 2 — body checks (whole draft)
1. **Reading level** — estimate Flesch-Kincaid grade (short sentences, common words
   = lower grade). Target 6-8. If it reads harder, name the specific sentences/words
   driving it up.
2. **Single point** — state the payload in ONE sentence. If an "and" joins two
   unrelated ideas (not just two supporting facts for one idea), fail this and name
   the second idea explicitly.
3. **No filler** — scan line by line; name any line that could be deleted with no
   loss of new information/detail/momentum. A concrete example or specific number is
   never filler regardless of count. Report an approximate ratio, not just yes/no.

### Step 3 — structure/attention-mechanic checks (family-specific, from Step 0)
Run ONLY the checks for the family identified in Step 0 — do not apply story checks
to a list post or vice versa. Pull the exact check list and known deltas from
`hook-floor-check.md`'s per-family sections. For each check in that family's table,
state pass/fail/partial with a one-line reason tied to the actual text.

If the family is `list` or `reframe`, say explicitly that the underlying sample is
too thin (n=24 and n=13) to treat these as firm rules — flag any fail there as a
hypothesis-level concern, not a confirmed problem.

### Step 4 — verdict
- List every check that FAILED or was a GAMBLE choice, each with the one concrete
  fix that would resolve it (not vague "tighten this up" — an actual rewritten line
  or restructuring instruction).
- Do not average failures into a vague overall score. State plainly whether this
  post is ready, ready-with-one-fix, or needs a real rewrite pass, and why.
- Never claim a check predicts virality — per `hook-floor-check.md`'s scope note,
  this whole checklist is a floor/executability check, not a virality predictor.
  Whether the underlying topic/take has real emotional charge for the audience right
  now is a human judgment call this skill cannot make.

## What NOT to do
- ❌ Do not skip Step 0's classification and go straight to "the hook feels fine" —
  that's the exact freeform-impression failure mode this skill exists to prevent.
- ❌ Do not apply the wrong family's structure checks (e.g. grading a resource
  roundup against "has a turning point").
- ❌ Do not treat a thin-sample finding (list, reframe) as equally solid as a
  well-sampled one (argument, teach, story) — always name the n.
- ❌ Do not silently pass a hook that previews a count without checking whether the
  outcome was also given away in the same breath.
