---
name: tofu-surprising-number
description: "Draft or rewrite a SURPRISING-NUMBER / STAT-SHOCK TOP-OF-FUNNEL LinkedIn post in your own voice: leads with one specific, checkable, counterintuitive number (a dollar figure, a percentage, a count, a timeframe) that stops the scroll, then spends the body explaining what the number means and why it should change how the reader thinks ('One Claude user consumed $27,000 of compute in 23 days. They paid $200.'). Carries the signature moves: the single-shock stat or split-percentage hook, a sourced authority anchor, the number contextualized not just stated, a two-line reframe closer. Hard rules: hook line 1 ≤ 62 / line 2 ≤ 50; the headline number must be REAL, sourced, and checkable (never rounded for rhythm or invented for shock); the body must EXPLAIN the number, not just repeat it; never claim you shipped a real customer product; soft CTA only. Use when you have one genuinely surprising, verifiable statistic that reframes an AI/business belief. NOT for concept decompositions (that's the explainer), runnable setups (that's the how-to), contrarian myth-busts with no number, resource roundups, news breakdowns, or MOFU/BOFU posts."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md`, plus the shared cross-skill rules in `<BRAND_DIR>/linkedin-voice.md` (formatting, hook hard limits, footer convention, credibility beat, humor recalibration, sound-human checklist, mobile geometry, truth/authorship). This file only holds what's SPECIFIC to the Surprising-Number archetype — if a rule isn't here, it's in `<BRAND_DIR>/linkedin-voice.md`. If that file's shared rules change, this skill inherits the change automatically; don't fork a copy here.

# TOFU Surprising Number / Stat-Shock

Write a **surprising-number top-of-funnel post in your own voice**: the archetype where one specific, verifiable, counterintuitive number does the scroll-stopping, and the body earns it by explaining what the number actually means. This is a **make-them-do-a-double-take** post, not a concept decode and not a runnable how-to. The number is the payload, and everything after it exists to make that number land, hold, and get reshared.

The goal of every post: a stranger reads the number, thinks "wait, that can't be right" or "I need to double-check that," reads the body to resolve the tension, and reshares it as "look at this number."

---

## Classification — is this actually a Surprising Number?

Test: is there ONE specific, checkable number (a dollar amount, a percentage, a ratio, a count, a timeframe) that a stranger would find genuinely surprising, and does the body EXPLAIN that number rather than just decorate around it? If yes, it's this archetype.

**Not this archetype if:**
- The number is a *count of layers/parts* the post then decodes → Conceptual Explainer (`tofu-explainer`); a "5-layer stack" is an explainer's structure, not a stat-shock.
- The number is a *count of runnable steps* the reader executes → Tactical How-To (`tofu-howto`); "8 ways to get 3x from your subscription" is a how-to.
- The number sets up a *first-person story with a cost and a turning point* → that's a MOFU (trust) post, out of scope for this TOFU pack; a real personal arc, not a universal point.
- There's no number at all, just an asserted belief being rejected → Contrarian (`tofu-contrarian`).
- The payload is external links/resources → Resource Roundup (`tofu-resource-list`).

---

## The structure (near-verbatim skeleton)

```
[HOOK — 2 lines: the surprising number, then the twist that makes it land]
[One specific, checkable number, stated flat.]
[The one line that makes the number impossible to ignore — the contrast, the "this is not a typo," the "they paid $200."]

[bridge: 1 line that promises the explanation]
Here's why this is [unsustainable / happening / the real story]:
(or)
Here's what the research actually says.

[credibility beat / source anchor — see <BRAND_DIR>/linkedin-voice.md]
[the sourced institution or study that backs the number, OR your own builder anchor]

[THE BODY — context the number, don't just repeat it]
[where the number comes from, what it's really measuring, what it hides]
[the mechanism / the playbook / the breakdown, in your one-line-per-line rhythm]
[optional: a second number that deepens or complicates the first — 90% vs 10%, 88% vs 5%]

[THE REFRAME — the two-line punch closer that flips the number into a lesson]
[The number] isn't [the surface reading].
It's [the real reading].
(or)
The [model / tool] is the visible 10%. The system is where the value lives.

[engagement question]

----
♻️ Repost [if your network needs to see this number]
➕ Follow me ([your name]) for more on building with AI
```

Use when: the number genuinely reframes something, and you can source it. A stat-shock post with no explanation underneath is a screenshot, not a post.

**Real reference examples** (from the golden dataset, likes as tagged):
- Alex Banks — "One Claude user consumed $27,000 of compute in 23 days. / They paid $200. Now everyone's limits are getting cut." (2,696 likes — single-shock stat + timeframe, then the twist).
- Rakesh Gohel — "98.7% accuracy with zero vectors; this is not a typo." (2,009 likes — implausibly precise number, defended immediately).
- Andreas Horn — "The uncomfortable math of AI transformation: 10% is the model. 90% is work your organization hasn't budgeted for." (1,402 likes — split-percentage that reframes).
- Michael Lee — "88% of organizations now use AI. Only 5% capture value at scale. 95% of pilots show no measurable P&L impact." (1,348 likes — stacked stats building to a gap).
- Chris Donnelly / Allie K. Miller — "IKEA replaced 8,500 customer service roles with AI. And the company is now $1.4 billion richer." (2,931 / 1,872 likes — number-in, number-out transformation).
- Real example: "$100K AI projects fail. Not because of bad models. Because of missing layers." (692 likes — high-stakes number leading a reframe).

---

## Signature voice moves (archetype-specific)

- **The hook is the number.** The default is a single implausible stat stated flat ("One Claude user consumed $27,000 of compute in 23 days."), but for hook variety pull a proven alternative template (single-shock stat, split-percentage, cost-contrast, stacked-stat gap, big-outcome transformation, counterintuitive-finding question, high-stakes number, opportunity number) from `references/hook-template-bank.md` — 8 fixed-word templates with slot tests and real examples from the golden dataset. Fill the slots with a REAL number; never round for rhythm or invent for shock.
- **Line 2 makes the number impossible to scroll past.** The number alone stops the scroll; line 2 opens the loop — the contrast ("They paid $200."), the defense ("this is not a typo."), the stakes ("90% is work your organization hasn't budgeted for.").
- **Source the number in the bridge, not later, in one of two explicit forms.** These posts live or die on trust. Right after the hook, either (1) name the study, company, survey, or benchmark the number comes from (a16z CIO survey, McKinsey, MIT, the API price sheet), or (2) if there is no external citation because the figure is your own estimate or rule-of-thumb, say so honestly ("a rough number from my own build costs," "a representative figure, not an audited one") rather than stating it as if it were externally verified. A number with neither an external source nor an honest illustrative-figure disclosure fails the self-check below — the number's credibility is the whole post.
- **Context the number, don't just repeat it.** The body's job is to explain what the number measures, where it comes from, and what it hides — "these consumer AI plans are massively subsidised, and the limits were never defined in the first place." A post that only restates the headline is under-built.
- **A second number that deepens the first** (optional, common in the dataset): 90% vs 10%, 88% vs 5% vs 95%, $150K vs $4.5K. The ratio is often more surprising than either number alone.
- **The two-line reframe closer.** "The model is the visible 10%. The system is where the value lives." / "AI models are becoming a commodity. AI systems are becoming the moat." Flip the number into the lesson.

**Floor-check (run before finalizing):** the full checklist lives in `post-grader`'s `references/hook-floor-check.md` (post-grader is invoked in the draw-check-rewrite loop below);
(cross-creator structural finding, not voice-specific) — does it open a real
loop that's still open at the fold, is it concrete not abstract, is the register
right. Surprising Number wasn't one of the 5 archetypes with enough sample size for
its own baseline row in that analysis — apply the general checklist with judgment.
One archetype-specific note: this hook is inherently concrete by design (a real
number IS the concreteness check), so lean hardest on the loop check — does line 2
open a real gap ("this is not a typo," "they paid $200") rather than just restating
the number. This checklist is a quality floor, not a virality predictor — whether the
number itself is genuinely surprising is your call, not something structure alone
can supply.

---

## Judge this archetype by ITS success metric: SHARES and DISBELIEF-COMMENTS, not saves

A surprising-number post wins when readers reshare it as "look at this number" and comment in disbelief ("wait, that can't be right" / "is this real?"). It is a **screenshot-and-reshare stat asset**, not a save-for-reference study guide (that's the Explainer) and not a copy-the-setup how-to (that's the How-To). The share-to-like ratios in the golden set skew high for a reason: a checkable, counterintuitive number is the single most reshareable payload on the feed. If a draft buries the number under setup or fails to source it, it loses the exact mechanism that makes this archetype travel.

---

## Length target
1,400–2,000 characters. Shorter than the contrarian/roundup archetypes — the number does the heavy lifting, and over-explaining dilutes the shock. But the number MUST be contextualized (where it comes from, what it hides, what it means): a draft that only restates the headline in different words is under-built, not concise. If short, add the mechanism behind the number, not more wind-up before it.

## What NOT to do
- ❌ Rounding the number for rhythm ("~$25K" when it's $27,000) — the precision IS the credibility; an inflated or rounded stat breaks trust on the first fact-check.
- ❌ An unsourced headline number — if you can't name where it comes from, don't lead with it. Flag it as unverified rather than posting it bare.
- ❌ Restating the number three ways instead of explaining it once — the body must add context, not echo.
- ❌ Letting the number set up a personal story arc (that's MOFU) or a runnable setup (that's How-To) or a layered concept decode (that's the Explainer).
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
### 2. The number + what it reframes, one sentence
### 3. Facts to verify (the headline number and every stat asserted, with its source)
### 4. Self-Check
- Hook L1 ≤ 62 / L2 ≤ 50, two-part test ✅
- Headline number is real, precise (not rounded), and sourced — either a named external source, or an explicit "this is my own estimate/rule-of-thumb" disclosure if no external citation exists ✅
- The body EXPLAINS the number (origin + what it hides), doesn't just repeat it ✅
- Credibility beat / source anchor present (per <BRAND_DIR>/linkedin-voice.md) ✅
- Two-line reframe closer present ✅
- Humor: 0-2 beats max, self-deprecating > pure dry (per <BRAND_DIR>/linkedin-voice.md) ✅
- Anti-AI-pass lint run and clean ✅
- Length 1,400-2,000 ✅
