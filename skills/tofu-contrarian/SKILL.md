---
name: tofu-contrarian
description: "Draft or rewrite a CONTRARIAN TOP-OF-FUNNEL LinkedIn post in your own voice: the 'Everyone wants X. Nobody wants Y.' / 'Most people think X. They're wrong.' myth-bust structure, the single highest-performing TOFU archetype. Carries the signature moves: two-line punch closer, bold-unicode headers, ↳/→ formatting, follow footer, dry deadpan humor. Hard rules: hook line 1 ≤ 62 / line 2 ≤ 50; one point only; asserts a specific belief is wrong and proves it; judged on COMMENT engagement (cmt/like ratio), not shares; external facts must be REAL and sourced; never claim you shipped a real customer product; soft CTA only. Use when you want a contrarian myth-bust TOFU post — a take that names a widespread belief and shows why it's wrong. NOT for resource roundups, news breakdowns, how-to systems, or MOFU/BOFU posts (those are separate skills/archetypes)."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md` to all copy this skill generates (spartan, active voice, short sentences, no em dashes, the banned-word list, etc.). Carve-out: if this skill exists to reproduce a specific named person's voice or your own recorded words, that target voice wins wherever it directly conflicts with those rules.

# TOFU Contrarian Myth-Bust Post

Write a **contrarian top-of-funnel post in your own voice**: the archetype where you name
a belief everyone holds, then proves it's wrong. This is the **highest-performing TOFU
structure** (the data post, the "don't build agents" post) and the one judged differently
from every other TOFU archetype: it wins on **comments**, not reshares.

The goal of every post: a stranger stops scrolling because their own belief just got
challenged, reads the proof, and comments — either to defend the belief or admit the gap.

## Credibility beat — one line, before the meat, not a story
Every contrarian post should carry ONE line that establishes you're not theorizing —
pulled from `<BRAND_DIR>/story-bank.md`'s canonical facts, placed in the bridge
(after the hook, before the symptom list/proof). This is NOT the confessional humor
beat above (that admits a mistake); this is a flat, factual authority anchor.

**Draw from (rotate, never repeat the same one twice in a row):**
- *"[a real system/tool/process you built yourself that proves hands-on depth in your domain, and the specific thing it let you see break]"*
- *"[a real role/company of yours + the specific hard thing it let you see firsthand — e.g. 'I ran X at Y and watched this exact failure mode from the inside']"*
- *"[a real, specific amount of money or time you invested in learning this + what it taught you — a checkable figure you actually spent, never invented]"*
- *"[a real thing you've shipped or done in this domain + the failure you personally watched happen]"*
- A plain first-hand-experience line already in the skeleton ("I've been building my own tools in this space for months") counts — don't stack a second one on top.

One line only. If it needs a second sentence, it's becoming a story — that's MOFU, not
here. Skip it entirely on posts where the credibility is already obvious from the topic
(e.g. you're citing a named external source, not your own experience).

> **📣 Adapting this to your own voice?** Study the structure and signature
> moves — make it yours:
> - The footer uses a `[your name]` placeholder — fill it with your own name.
> - Borrow the moves, not the facts. The stats and stories in the examples are real, pulled from the original creator's posts.
> - Signature phrases (e.g. "That's not a feature. That's a risk.") work in anyone's voice,
>   but overuse reads as template. Pick one or two per post.

---

## Classification — is this actually a Contrarian post?

By the shared decision-signal order (the orchestrator's `tofu-pattern-analysis` reference),
a post is Contrarian when it **asserts a belief is wrong** — before any other rule
fires (meme, resource-link, dated-news-event, one jarring $/% figure). If the post's real
payload is a link, a numbered how-to, a decoded concept, or a single shocking number with
no "X is wrong" framing, it's a different archetype — see `tofu-orchestrator` to route.

Test: can you write the belief being corrected as one sentence starting "Most people
think..." or "Everyone believes..."? If yes, and the post spends its body proving that
belief false, it's Contrarian.

---

## The structure (near-verbatim skeleton)

The highest-performing structure (the data post, the configure-Claude post, the
"don't build agents" post):

```
[HOOK — 2 lines: the belief, stated, then flipped]
Everyone wants [the sexy thing].
Nobody wants [the unglamorous thing].
— or —
Most people think [X].
They're wrong.

[2–3 lines: the ambition / the hype / the credibility beat]

But ask one simple question:
"[the question that exposes the gap]"

Watch what happens.

Not "[the deflection]."
Not "[the other deflection]."

[the real question, again]

Most [orgs/people/builders] don't have a [X] problem.
They have a [Y] problem.

→ [symptom]
→ [symptom]
→ [symptom]
→ [symptom]

Then they wonder why [the outputs keep getting things wrong].

[X] is not an engineering problem.
It never was.
It's a prioritization problem dressed up as a technical one.

It means someone has to do the unglamorous work first.

Until that happens, every [AI initiative] is just
[the deflated version of the promise].

[X] doesn't [fix/clean] [Y].
It [scales/moves] it [faster].

That's not a feature.
That's a [risk / blast radius].

[engagement question]

----
♻️ Repost [if your network needs this]
➕ Follow me ([your name]) for more [AI insights]
```

Use when: the topic is a widely-held belief that's actually false, provable with a concrete
symptom list or a real breakdown (data, setup, fundamentals over hype).

**Alternate variants that still qualify as Contrarian** (from the golden dataset):
- *"Most people think X. They're wrong."* + a diagram/decomposition that proves it
  (`7414304865973223424`, `7482781096233885697`).
- *"[Belief], right? Wrong. Dead wrong."* + a personal anecdote as proof
  (`7336799088585199616`).
- *"[Doing X]? You're doing it wrong"* + a comparison framework
  (`7359195611641831426`).
- A talk/expert breakdown that reframes as "most builders don't have an X problem, they
  have a Y problem" (`7463212330181423104`, the canonical example).

---

## Judge this archetype by ITS success metric: COMMENTS, not shares

**This is the one rule that differs from every other TOFU archetype.** Across a sample of
52 contrarian myth-busts, median cmt/like ratio is
**0.11** — the highest of any TOFU pattern — and share/like is only 0.10 (below the
resource-roundup's 0.14). **A contrarian post that gets reshared like a resource list but
draws few comments has NOT succeeded on its own terms**, even if raw likes are high.

Why: people argue with a take. They don't argue with a free course list. The engagement
question at the end must be sharp enough to make the reader want to defend or attack the
claim, not just nod and scroll.

**Scoring implication for the eval harness:** the pairwise judge and rubric still apply,
but when tuning this skill specifically, weight the `cta`/`hook_virality` dimensions (which
proxy for comment-worthiness) as the primary signal — not `structure` fidelity to a
resource-roundup shape.

---

## Signature voice moves (use these — they ARE the voice)

- **The two-line punch closer.** A short claim, then its flip, on two lines:
  - *"That's not a feature. / That's a risk."* · *"That's not a feature. / That's a blast radius."*
  - *"Autonomy isn't the goal. Reliability is."* · *"Clever algorithms don't guarantee reliability. Architecture does."*
  - *"Build the system first. The outputs follow."*
- **"X doesn't fix Y. It scales it."** — *"AI doesn't make dirty data clean. It makes dirty data move faster." · "Claude doesn't fix a broken setup. It scales it."*
- **"Stop asking X. Start asking Y."** — the reframe that ends an explainer-flavored contrarian.
- **"Ask one simple question… Watch what happens. Not [A]. Not [B]. [the real one]."** — the rhetorical setup.
- **"Most [people] don't have a [X] problem. They have a [Y] problem."**
- **"[X] is not an engineering problem. It never was. It's a prioritization problem dressed up as a technical one."**
- **"Then they wonder why the outputs keep getting things wrong."**
- **Image/source credit** — you name the diagram author when a visual backs the breakdown ("This diagram by Luís Rodrigues", "Credit to…").

Don't force all of these into one post — reach for the one or two that fit. Overusing the skeleton makes posts feel templated.

---

## Formatting (the fingerprints)
- **One sentence per line.** Heavy white space. Almost every line stands alone.
- **𝗕𝗼𝗹𝗱 𝘂𝗻𝗶𝗰𝗼𝗱𝗲** for section headers and key phrases (𝟭/, 𝗦𝘁𝗼𝗽 𝗮𝘀𝗸𝗶𝗻𝗴). This is the ONE place unicode-bold is allowed — it's the signature move. **Never in the hook.**
- **↳** for sub-bullets; **→** and **•** for symptom/feature lists.
- **`----`** or `---` divider before the footer.
- **American spelling only:** optimize, behavior, organize, realize — never optimise/behaviour/realise/centre/colour.

## Footer (use one, match the topic)
```
[engagement question]

----
♻️ Repost [if your network needs this / to help builders ship working AI]
➕ Follow me ([your name]) for more [AI insights / resources like this]
```
Fill `[your name]` with the poster's byline. Shorter variant: *"I post AI content every day at 9 am ET. Follow me ([your name]) to get the latest."*
Optional employer-safe add: *"Opinions expressed are my own and do not represent the views, policies, or positions of my employer."*

**No newsletter signup, no link in the footer by default** — keep the close a soft repost + follow.

**Never** a lead-magnet footer (no "Comment [WORD] and I'll DM you", no "FREE ↓", no 4-step Follow/Like/Repost/Subscribe block) — that's a BOFU lead-magnet, a different skill.

---

## Hook rules (hard limits)
- **Line 1 ≤ 62 chars. Line 2 ≤ 50 chars.** Count both.
- No bold/italics in the hook.
- Contrarian hook patterns: *"Everyone wants X. Nobody wants Y."* / *"Most people think X. They're wrong."* / *"[Belief], right? Wrong. [Dead wrong.]"* / *"[Doing X]? You're doing it wrong."*
- **Two-part test:** line 1 states the belief (contradiction / stakes / a name); line 2 flips it or opens the curiosity gap ("They're wrong." / "Watch what happens.") the reader can't close without expanding.
- **One reading only:** every "this/most/they/it" points at one thing.
- **Promise = payoff:** the body must actually prove the belief wrong — not just assert it twice.

**Floor-check (run before finalizing):** the full checklist lives in `post-grader`'s `references/hook-floor-check.md` (post-grader is invoked in the draft-check-rewrite loop below; cross-creator structural finding, not voice-specific) — does it open a real
loop that's still open at the fold, is it concrete not abstract, does it use direct
address, is the register casual/punchy. Contrarian's baseline from that analysis:
opens_loop ~65%, takes_a_side ~84% (highest of any archetype — makes sense, this IS
the take-a-stance archetype), abstraction ~86% abstract. This checklist is a quality
floor, not a virality predictor — whether the underlying belief is actually
contentious enough to land is your call, not something structure alone can supply.

---

## One point, zero filler
- **One belief corrected per post.** Name it in a sentence first; cut anything that doesn't serve proving it wrong. A second idea is a second post.
- **Every line earns its place.** Placeholder test: swap a line for `[generic filler]` — if nothing's lost, cut it.

## Length is not optional — hit the target range
**Do not finish a draft under 1,800 characters.** A short, punchy-sounding draft that
stops at 600-900 characters has almost always cut the proof, not the filler — and a
contrarian post lives or dies on its proof. Before finishing, count the characters. If
under 1,800:
- **First, expand the proof/symptom list** — add another named example, another
  sub-bullet (↳), another concrete detail (a tool name, a number, a quoted line).
  Never pad with adjectives or repeated claims.
- **Second, check each numbered item has 2-3 sub-points**, not one. A one-line item under
  a 1️⃣/𝟭/ header reads thin; the real posts give each item room to prove itself.
- **Only after the proof is fully built out**, if still short, add one more line to the
  bridge/credibility beat — never to the closer or footer.
Target: 1,800-2,400 characters. 1,500-1,800 or 2,400-2,500 is acceptable but not ideal.
Under 1,500 fails the length check outright.

## Front-load the value
- Hook 2–3 lines → setup ≤6 lines → the proof/breakdown by ~line 6–9.

## Mobile skimmability — line geometry
- One clause per line; ≤3 lines before a blank line.
- ~7 words / ≤40 chars per line; sentences rarely over 20 words.
- ~⅓ of lines blank. Vary line length for rhythm.
- List caps: ≤5 main items, ≤3 sub-bullets each.

## Sound human — reads like you, not AI
> **Full rule set:** `<BRAND_DIR>/writing-style.md` Part 2 — the anti-fingerprint checklist + Specificity Audit.
- **Ban AI-tells:** delve, leverage (verb), harness, unlock, elevate, empower, foster, facilitate, streamline, seamless, robust, transformative, innovative, cutting-edge, navigate (metaphor), myriad, plethora, tapestry, "in the digital landscape", "in today's fast-paced world", Furthermore/Moreover/Additionally (filler), ultimately/essentially/fundamentally (filler), AI-native, "compounding", legacy (filler adjective).
- **Break structural symmetry** — vary sentence length hard; uneven list items; at least one asymmetric structural move per post.
- **Shift register at least once** — dry deadpan next to a real claim.
- **Specificity Audit — the primary gate:** ≥2 details only you could have supplied. If it can't clear the bar, **ask the writer for the missing specific — never invent one.**
- **No cryptic fragments** — except your deliberate two-line punch closers, which ARE complete clauses.
- **Show, don't tell.** Concrete > abstract. American spelling.

---

## Humor & personality — self-deprecating, not just dry
**Your TOFU used to run pure dry-clinical with near-zero personal texture. Your last
3 weeks of MOFU proved a warmer, more sarcastic, self-mocking register reads as more
you — and it's not MOFU-exclusive. Pull that register into TOFU's humor beats too.**
The topic/structure/breadth stay TOFU (a universal point, not your personal story arc) —
only the humor PALETTE widens. Still capped at **2 beats max** — the argument leads.

**Patterns to reach for (pick 1–2, spaced):**
- **Self-deprecating aside, aimed at yourself as a builder/poster, not the reader:**
  *"Even my mom can prototype now."* · *"I've made this mistake enough times to franchise it."*
  · *"I say this as someone who shipped exactly this bug in March."*
- **Mock-internal-dialogue, one line:** a flash of your own ego/panic, deflated fast —
  *"My brain's first move: 'is it me, or is it the market.' It's never the market."*
- **Dry sarcastic mic-drop on the takeaway itself:** *"Well, that's fun."* · *"Cool, cool,
  cool."* — a flat 2–4 word beat that undercuts the point right after making it.
- **Honest disclaimer (kept from before):** *"No, Anthropic isn't paying me. I checked."*
- **Incongruous register / word-swap (kept from before):** a medical/legal/recovery word
  in a business line (*"that's a blast radius"*).

**One confessional first-person beat is now allowed per post** (new) — a single
self-mocking admission that you've also fallen for the exact trap the post names, NOT a
story arc. One sentence, not a scene. If it starts needing a second sentence to land,
it's drifting into MOFU territory — cut it back to one line or move it to a MOFU post.

Rules: never write the laugh (no `lol/haha/😂`), never telegraph it ("here's a funny
thing"), never make the substance the joke (the claim/proof stays real and serious), and
drop humor entirely on hard-news/serious topics. The self-deprecation punches at YOURSELF
or a universal "we all do this," never at the reader.

## Your Life Stories — rarely for TOFU
Your biographical vignettes live in `<BRAND_DIR>/story-bank.md`.
A pure contrarian reach post almost never needs one. Default: write the post without one.

---

## Save-worthy / reshare-worthy gate
Even though contrarian wins on comments, not reshares, it still must:
- **Prove something concrete** — a framework, a real breakdown, a counter-intuitive truth with a reason, not just an opinion.
- **Be defensible** — a reader who disagrees should be able to name exactly which claim they're arguing with.
- **Earn the comment** — the engagement question should invite a real answer, not a rhetorical nod.

---

## ⚠️ Truth & authorship (non-negotiable)
- **External facts must be real and sourced.** Never invent a stat, a launch, or a quote.
- **Credit diagram authors** when a visual backs the breakdown.
- **Never claim you shipped/launched a real customer product** — you're mid-build.
- **Never fabricate your numbers** (followers, hours, results). Leave a `[placeholder]` and flag it if missing.

---

## Output Format

Pattern selection, drafting, and self-critique are **internal**.

**Draft → check → rewrite loop (mandatory, max 3 loops).** Write the draft, then run
it through `post-grader`'s ordered procedure (hook checks including the
count-vs-outcome sub-check, body checks, family-specific structure checks) rather
than an informal read — that ordering exists because informal checks have missed
real issues before. Rewrite based on every failed/gamble check the grader surfaces.
Repeat the grader pass on the rewrite. Stop as soon as every check passes; stop at 3
loops regardless and name what's still failing if it hasn't converged. Output only
the final version — the grading itself stays internal, not shown to the user unless
they ask to see it.

**Anti-AI pass (mandatory, runs automatically — never skip).** Before showing the draft to the writer, run the `anti-ai-pass` skill on it: `python3 .claude/skills/anti-ai-pass/scripts/lint.py --stdin` with the draft text, remove every HARD banned word/phrase (quietly, silently, leverage, actually, etc.), keep at most ONE structural move (Most-people / Not-X-Y / Everyone-wants-X) and only if >=2 real specifics sit behind it, and fix rhythm tells (rule-of-three, -ing tails, em dashes). This is BUDGETED, not absolute — the contrarian hook IS one allowed move; stacking a second flip on top is the machine tell. Load `anti-ai-pass/SKILL.md` for the full judgment layer.

### 1. The Post
Full text as it'd appear on LinkedIn — plain text, no code fences.

### 2. The belief being corrected
One sentence: "Most people think ___. This post proves ___ instead."

### 3. Facts to verify
Every stat/quote/diagram-credit the post asserts. Flag `[placeholders]`.

### 4. Self-Check (all ✅ or revise)
- Hook L1 ≤ 62 (actual: __) · L2 ≤ 50 (actual: __) · two-part test passes ✅
- Asserts one clear belief and proves it wrong — no second thread ✅
- Value front-loaded — proof/breakdown by ~line 6–9 ✅
- Every external fact real/sourced; nothing fabricated; diagram authors credited ✅
- No claim you shipped a customer product; no invented personal numbers ✅
- Your voice present — at least one signature move ✅
- Formatting — one sentence per line, ↳/→, divider + `[your name]` follow footer ✅
- Reads human — Specificity Audit ≥2 un-generatable details; sentence-length variance; ≥1 register shift; no AI-tells ✅
- Humor: 0–2 dry beats max; no telegraphed laughs ✅
- Soft CTA only — no lead-magnet comment-gate / 4-step footer ✅
- Mobile geometry ✅
- Engagement question is comment-bait, not reshare-bait (invites disagreement/a real answer) ✅

---

## What NOT to do
- ❌ Fabricating a stat, a launch, or a quote.
- ❌ Burying the proof under a long wind-up.
- ❌ Correcting two beliefs in one post.
- ❌ A lead-magnet comment-gate or workshop-as-engine — that's BOFU.
- ❌ Claiming you shipped a real customer product, or inventing your numbers.
- ❌ Over-templating — don't cram every signature move into one post.
- ❌ AI-tell vocabulary, prose blocks, or unicode-bold in the hook.
- ❌ Optimizing for reshares instead of comments — that's the wrong metric for this archetype.

## Reference Corpus
See [`examples.md`](./examples.md) for the one full six-beat worked example pulled from
the source examples, plus a note on which posts in the golden dataset
( a golden set of real high-performing posts) exemplify each hook
variant.
