---
name: tofu-explainer
description: "Draft or rewrite a CONCEPTUAL EXPLAINER TOP-OF-FUNNEL LinkedIn post in your own voice: demystifies a concept via an analogy/metaphor + a layered N-step decomposition ('Most people think Agentic AI is just ChatGPT + tools. They're wrong. Think of it in 5 layers.'). Carries the signature moves: 'Most people think X. They're wrong.' hook, one sticky metaphor that organizes the whole post, bold-unicode numbered layers, a recap-quadruplet mic drop. Hard rules: hook line 1 ≤ 62 / line 2 ≤ 50; one concept, one metaphor, no second thread; every layer needs a limit/tension, not just a description; external facts must be REAL and sourced; never claim you shipped a real customer product; soft CTA only. Use when you want to decode a concept (LLM/RAG/Agents/MCP, AI vs ML vs GenAI, a product's internal architecture) via a layered analogy. NOT for contrarian myth-busts with no decomposition, resource roundups, news breakdowns, how-to systems, or MOFU/BOFU posts."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md`, plus the shared cross-skill rules in `<BRAND_DIR>/linkedin-voice.md` (formatting, hook hard limits, footer convention, credibility beat, humor recalibration, sound-human checklist, mobile geometry, truth/authorship). This file only holds what's SPECIFIC to the Conceptual Explainer archetype — if a rule isn't here, it's in `<BRAND_DIR>/linkedin-voice.md`. If that file's shared rules change, this skill inherits the change automatically; don't fork a copy here.

# TOFU Conceptual Explainer

Write a **conceptual-explainer top-of-funnel post in your own voice**: the archetype where you take a concept everyone name-drops but few understand, and demystify it through ONE sticky metaphor that organizes an N-layer decomposition. This is a **teach-through-analogy** post, not a myth-bust and not a how-to.

The goal of every post: a stranger who's heard the term but never understood it says "oh, THAT'S what that means" — and saves the post to explain it to someone else later.

---

## Classification — is this actually a Conceptual Explainer?

Test: can you name ONE metaphor that organizes the whole post (a body, a stack, a hierarchy, an operating system), and does the post walk through N distinct layers/parts of that metaphor, each with its OWN job and its OWN limit? If yes, it's this archetype.

**Not this archetype if:**
- The post asserts a belief is wrong with no decomposition → Contrarian (`tofu-contrarian`).
- The "layers" are actually a numbered how-to a reader executes today → Tactical How-To (`tofu-howto`).
- The payload is external links/resources → Resource Roundup (`tofu-resource-list`).
- It's musing/observation about something cool with no teach-the-concept structure → not TOFU-explainer at all; likely Relatable Mirror.

---

## The structure (near-verbatim skeleton)

```
[HOOK — 2 lines: the oversimplification, named and rejected]
Most people think [X] is just "[oversimplification]."
They're wrong.
(or)
[X] is a maze of acronyms until you see it as [metaphor].
[the acronyms/parts, named]

[1-2 lines: the metaphor + a credibility beat]
[N] layers. [N] jobs. One system.
[credibility beat — see <BRAND_DIR>/linkedin-voice.md]

Think of [X] in [N] layers:

𝟭/ 𝗔𝗷𝗪𝗘 𝗙𝗆 [layer name] ([role])
[one-line what it is]
[1-2 lines: what it enables / where it hits its limit]

𝟮/ ... (repeat, 3-5 layers)

[THE REFRAME — the recap-quadruplet + a vivid image]
The [layer 1] does X. The [layer 2] does Y. The [layer 3] does Z.
Everyone reaches for [the flashy layer]. But [flashy layer] on top of a broken [foundational layer] just [fails vividly].

[engagement question]

----
♻️ Repost [to help builders in your network]
➕ Follow me ([your name]) for more on building with AI
```

Use when: a concept has genuinely distinct, nameable parts that build on each other, and each part has a real failure mode when the layer below it is missing or broken.

**Real reference examples** (from the golden-dataset pull, all verified tofu_type=conceptual_explainer, likes≥750):
- Alex Wang — "If your Claude Code feels weaker, the `.claude/` setup is not just config. It's where the real leverage lives." (3,648 likes)
- Brij Kishore Pandey — "Claude Code ships with 5 architectural layers most engineers never open. Layer 1: CLAUDE.md → the agent's constitution." (3,379 likes)
- Brij Kishore Pandey — "Not all AI processors are built for the same job. CPU → orchestration, GPU → parallelism, TPU → tensor, NPU → edge." (3,310 likes)
- GenAI Works — "2026 RAG tech stack. Master these 9 agentic layers. Level 0 Deployment ... Level 8 Alignment." (4,260 likes)
- A real example: "AI is a maze of acronyms until you see it as a body. LLM, RAG, Agents, MCP." (908 likes, 91 shares — a canonical example, see the source examples)

---

## Signature voice moves (archetype-specific)

- **The hook.** "Most people think X. They're wrong." is the default, but for hook variety pull a proven alternative template (myth-bust, blunt-claim, named-comparison, numbered stack-map, question, process-journey, contrarian-reveal, everyone/few-split) from `references/hook-template-bank.md` — 8 fixed-word templates with slot tests and real examples extracted from the golden dataset. Fill the slots with something real for the concept at hand; never copy verbatim.
- **The one sticky metaphor.** Body, operating system, stack, constitution, nervous system — pick ONE and don't mix metaphors mid-post.
- **"N layers. N jobs. One system."** — the compression line right after the hook.
- **Bold-unicode numbered layer headers** (𝟭/, 𝟮/ ...) each with a role in parens: "𝟭/ 𝗧𝗔𝗠𝗲 𝗔 (𝗧𝗹𝗲 𝗦𝗺𝗲)".
- **The recap-quadruplet mic drop.** One sentence per layer, in order, then the vivid punch: "The LLM thinks. RAG fact-checks. Agents execute. MCP connects them all. ... Hands on a brain that can't see just flail."
- **Credit the diagram author** when a visual backs the breakdown (per `<BRAND_DIR>/linkedin-voice.md`'s truth/authorship rule).

**Floor-check (run before finalizing):** per `<BRAND_DIR>/hook-floor-check.md`
(cross-creator structural finding, not voice-specific) — does it open a real
loop that's still open at the fold, is it concrete not abstract, is the register
right. Conceptual Explainer's baseline from that analysis: opens_loop ~82%,
takes_a_side ~73%, abstraction ~84% abstract. This checklist is a quality floor, not
a virality predictor — whether the concept itself is compelling enough to save is
your call, not something structure alone can supply.

---

## Judge this archetype by ITS success metric: SAVES, not comments or shares

An explainer wins when readers save it as a reference to come back to and share it as "here's the clearest explanation of X I've seen." It is a **save-and-share teaching asset**, not a debate-starter (that's Contrarian) and not a curated list (that's Resource Roundup). If a draft ends up arguing a point instead of teaching a structure, it has drifted into Contrarian — pull it back.

---

## Length target
1,600-2,200 characters. Each layer needs its own 2-3 line block (what it is + where it hits its limit) — a layer that's just one bare line is under-built. If short, expand a layer's limit/failure mode before padding the wind-up.

## What NOT to do
- ❌ Mixing metaphors mid-post (starting with "body," drifting to "stack").
- ❌ A layer with no limit/tension — every layer needs its own failure mode, not just a definition.
- ❌ More than 5 layers (loses the mobile-skimmable shape); pick the essential ones.
- ❌ Turning the explainer into an argument (that's Contrarian) or a numbered action list (that's How-To).
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
### 2. The metaphor + the N layers, named
### 3. Facts to verify
### 4. Self-Check
- Hook L1 ≤ 62 / L2 ≤ 50, two-part test ✅
- ONE metaphor sustained throughout, no mixing ✅
- Every layer has a role AND a limit ✅
- Credibility beat present (per <BRAND_DIR>/linkedin-voice.md) ✅
- Recap-quadruplet + vivid closer present ✅
- Humor: 0-2 beats max, self-deprecating > pure dry (per <BRAND_DIR>/linkedin-voice.md) ✅
- Anti-AI-pass lint run and clean ✅
- Length 1,600-2,200 ✅
