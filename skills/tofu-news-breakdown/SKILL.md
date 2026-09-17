---
name: tofu-news-breakdown
description: "Draft or rewrite a THIRD-PARTY NEWS/LAUNCH BREAKDOWN TOP-OF-FUNNEL LinkedIn post in your own voice: a recognized person/company just did/said/launched something real, and you distill it into numbered lessons ('An Anthropic engineer just told us not to build agents. Here's the breakdown.'). Hard rules: hook line 1 ≤ 62 / line 2 ≤ 50; the source event must be REAL, named, and linkable/verifiable; the numbered lessons must be genuine distillations, not padding; never claim you shipped a real customer product; soft CTA only. Use when a real, recent, named external event/talk/launch is worth distilling into a lesson list. NOT for your own announcements (a first-party MOFU post, out of scope here), resource roundups (payload is links, not lessons), contrarian takes with no real news hook, or explainers with no dated event."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md`, plus the shared cross-skill rules in `<BRAND_DIR>/linkedin-voice.md` (formatting, hook hard limits, footer convention, credibility beat, humor recalibration, sound-human checklist, mobile geometry, truth/authorship). This file only holds what's SPECIFIC to the Third-Party News Breakdown archetype — if a rule isn't here, it's in `<BRAND_DIR>/linkedin-voice.md`.

# TOFU News / Launch Breakdown (third-party)

Write a **news breakdown top-of-funnel post in your own voice**: a recognized person, company, or team just did/said/launched something real and recent, and you distill the substance into a numbered lesson list for builders. This is your **highest-authority-borrowed** archetype — the credibility comes from the named source, and the value comes from your distillation.

The goal of every post: a stranger who missed the original talk/launch/announcement gets the substance in 60 seconds, and saves the post instead of the original.

---

## Classification — is this actually a third-party News Breakdown?

Test: does the hook name a REAL, RECOGNIZABLE external person/company/event ("[Name] just told us / showed / dropped X"), and does the body distill that event into numbered lessons YOU extracted, not facts you're asserting on your own authority? If yes, this archetype.

**Not this archetype if:**
- You yourself are the subject of the announcement → that's a first-party MOFU post, out of scope for this TOFU pack.
- The payload is a multi-item free resource list, not lessons from ONE event → Resource Roundup.
- There's no real, dated, named event — just a belief being asserted → Contrarian.
- The distillation decodes a general concept's parts rather than one specific talk/launch → Conceptual Explainer.

---

## The structure (near-verbatim skeleton)

```
[HOOK — 2 lines: named source + what they just did]
[Recognized name/role] just [told us / showed / dropped] [X].
[1 line: who they are / what it was]

[1-2 lines: the angle — what's surprising or notable about it]
[credibility beat — see <BRAND_DIR>/linkedin-voice.md]

Here's the breakdown. Save it before [your next build]:

1️⃣ [Lesson]
↳ [concrete sub-point]
↳ [concrete sub-point]

2️⃣ ... (repeat, 3 max)

[the whole-thing-in-one-sentence mic drop]
[Autonomy isn't the goal. Reliability is. / a similarly tight reframe]

[link to the talk/source]

[engagement question]

----
♻️ Repost [to help builders in your network]
➕ Follow me ([your name]) for more on building with AI
```

Use when: a real, recent, NAMED talk/launch/announcement exists that's worth distilling. Always name AND link the real source.

**Real reference examples** (Sub-type B specifically, from the golden-dataset pull, likes≥750):
- Strong real example: "An Anthropic engineer just told us not to build agents. Barry Zhang runs agent infrastructure at Anthropic. He just gave a 14-minute talk... Here's the breakdown." (2,734 likes, 335 shares — full breakdown in the source examples).
- Real example: "The entire RAG industry is about to get cooked. Researchers built a new RAG approach... PageIndex... 98.7% on FinanceBench." (per `examples.md`).
- Chris Donnelly — "IKEA replaced 8,500 roles... $1.4B" style distillation, numbered breakdown of a real corporate event.
- Third-party pattern to emulate (structure only, never facts): "End of an era at Apple: Tim Cook's last day... This was a 15-year masterclass: → iPhone... → Services crossed $100B..." (Linas Beliūnas pattern).

---

## Signature voice moves (archetype-specific)

- **Hook variety:** see `references/hooks-swipe.md` for the real hook lines from every third-party post in the golden dataset, tagged by pattern (named-entity-just-did-X, breaking-alert, named-creator callout, shock-stat, threat-framing, comparison/diss, myth-vs-data). Rotate patterns across a run; reference for variety, never copy verbatim.
- **"[Name/role] just [did X]" + a who-they-are line** establishing why this person's word carries weight.
- **"Here's the breakdown. Save it before [your next build]:"** — the tease into the numbered lessons.
- **1️⃣ + ↳ sub-points**, max 3 top-level lessons, each with 2 concrete sub-points.
- **The whole-thing-in-one-sentence mic drop** — the entire talk/launch compressed into one memorable line.
- **Always link the real source — inline, not "in comments."** Put the actual `Source: <url>` directly in the post body (e.g. under the mic-drop line or in the footer), not deferred to "link in comments." R3 eval evidence: this single change moved the source_linked_verifiable dimension +2.5 points (an order of magnitude past judge noise) with zero truth risk — "in comments" reads as unverifiable/deferred even when the same source is genuinely real.

**Floor-check (run before finalizing):** per `<BRAND_DIR>/hook-floor-check.md`
(cross-creator structural finding, not voice-specific) — does it open a real
loop that's still open at the fold, is it concrete not abstract, is the register
right. News Breakdown's baseline from that analysis: opens_loop ~57%, takes_a_side
~29% (low — this archetype distills a real event, it doesn't argue a belief),
abstraction ~84% CONCRETE (the highest of any archetype — named people, real events,
real numbers, never vague musing). This checklist is a quality floor, not a virality
predictor — whether the source itself is notable enough to distill is your call,
not something structure alone can supply.

---

## Judge this archetype by ITS success metric: SHARES and SAVES from a credibility signal

A news breakdown wins when readers reshare it BECAUSE the named source is credible, and save it as a substitute for watching/reading the original. If the source isn't genuinely notable, or the lessons feel padded rather than distilled, the mechanic fails even with good prose.

---

## Length target
1,800-2,400 characters. Each of the (max 3) lessons needs 2 concrete sub-points — a lesson with one bare line is under-built.

## Truth & authorship (critical for this archetype specifically)
- **The event must be real, dated, and verifiable.** Name the actual person/company/talk. Link it **inline in the post body** (`Source: <url>`), never "link in comments."
- **Never invent a stat, a quote, or a detail attributed to the named source.**
- **If the source can't be verified as real and current, flag it and don't post it as fact.**

## What NOT to do
- ❌ Naming a source without linking/verifying the actual event.
- ❌ Deferring the source link to "comments" instead of putting it inline in the post body.
- ❌ More than 3 top-level lessons (loses the save-and-skim shape).
- ❌ Fabricating a stat or quote attributed to the named person.
- ❌ Confusing this with a first-party announcement of your OWN news — that's a MOFU/trust post, out of scope for this TOFU pack.
- ❌ AI-tell vocabulary, unicode-bold in the hook — see `<BRAND_DIR>/linkedin-voice.md`.

## Output Format
Follow `<BRAND_DIR>/linkedin-voice.md`'s mandatory anti-AI-pass lint step before presenting any draft.

**Draft → check → rewrite loop (mandatory, max 3 loops).** Write the draft, then run
it through `post-grader`'s ordered procedure (hook checks including the
count-vs-outcome sub-check, body checks, family-specific structure checks) rather
than an informal read — that ordering exists because informal checks have missed
real issues before. Rewrite based on every failed/gamble check the grader surfaces.
Repeat the grader pass on the rewrite. Stop as soon as every check passes; stop at 3
loops regardless and name what's still failing if it hasn't converged. Output only
the final version — the grading itself stays internal, not shown to the user unless
they ask to see it.

### 1. The Post
### 2. The source event, named + link
### 3. Facts to verify (every stat/quote/claim attributed to the source)
### 4. Self-Check
- Hook L1 ≤ 62 / L2 ≤ 50, names a real recognizable source ✅
- Source event is real, dated, linked INLINE in the post body (not "in comments") ✅
- Max 3 lessons, each with 2 concrete sub-points ✅
- Whole-thing-in-one-sentence mic drop present ✅
- Credibility beat present if it adds, not competes (per <BRAND_DIR>/linkedin-voice.md) ✅
- Humor: 0-2 beats max, self-deprecating > pure dry (per <BRAND_DIR>/linkedin-voice.md) ✅
- Anti-AI-pass lint run and clean ✅
- Length 1,800-2,400 ✅
