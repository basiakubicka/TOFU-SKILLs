---
name: tofu-resource-list
description: "Draft or rewrite a RESOURCE ROUNDUP TOP-OF-FUNNEL LinkedIn post in your own voice: the multi-item free-list post ('[Institution] just made $10K of AI education free', 'Stanford just dropped their entire AI curriculum'), the highest-SHARE TOFU archetype (share/like 0.14, the highest of any TOFU pattern). Carries the signature moves: named-institution hook with a free-vs-expensive inversion, a who-it's-for grouping or one-line why-this-one per item, a reframe line ABOVE the list ('Not access. Understanding.'), SAVE-bait footer, dry deadpan humor. Hard rules: hook line 1 ≤ 62 / line 2 ≤ 50; every item carries a filter, never bare links; every link real; judged on SHARES/SAVES (share/like), not comments. The exact inverse of the contrarian skill. Never claim you shipped a real customer product; soft CTA only, never a comment-gate. Use when you want a roundup of free courses, lectures, repos, guides, or tools. NOT for single-resource deep dives (a separate sub-variant), contrarian takes, news breakdowns, how-to systems, or MOFU/BOFU posts."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md` to all copy this skill generates (spartan, active voice, short sentences, no em dashes, the banned-word list, etc.). Carve-out: if this skill exists to reproduce a specific named person's voice or your own recorded words, that target voice wins wherever it directly conflicts with those rules.

# TOFU Resource Roundup (Multi-Item Free List)

Write a **resource-roundup top-of-funnel post in your own voice**: the archetype where you
hand the reader a curated, multi-item list of free resources (courses, lectures, repos,
guides) anchored to a named institution or a credible curator. This is your **highest-SHARE
TOFU structure** and the one judged differently from every other TOFU archetype: it wins
on **reshares and saves**, not comments.

The goal of every post: a stranger stops scrolling because a name they trust just made
something expensive free, reads the curated list, and reshares or saves it. Reposting a
credible free list makes THEM look generous and in-the-know.

## Credibility beat — one line, before the list, not a story
Every roundup should carry ONE line establishing why you're curating this, not just
forwarding it — pulled from `<BRAND_DIR>/story-bank.md`'s canonical facts, placed right
before the list starts (after the sweetener, before "Here's the full list"). This is
NOT the confessional humor beat above; it's a flat, factual authority anchor.

**Draw from (rotate, never repeat the same one twice in a row):**
- *"[a real system/tool you built yourself that gives you the judgment to tell a real resource from a repackaged one]"*
- *"[the real amount of money or time you spent vetting resources in this space + why that makes your shortlist trustworthy — a checkable figure, never invented]"*
- *"[a real credential of yours that proves you've done the work + 'I don't recommend resources I haven't used']"*
- A plain effort-flex line already in the skeleton ("I spent 100 hours learning this the hard way") counts as this beat — don't stack a second one on top.

One line only. If it needs a second sentence, it's becoming a story — that's MOFU, not
here. Skip it when the institution/curator's own authority already carries the hook
(e.g. "Stanford just released...") and a personal credibility line would be redundant.

> **📣 Using this as a cohort member?** Study the structure and signature
> moves. Make it yours:
> - The footer uses a `[your name]` placeholder. Fill it with your own name.
> - Borrow the moves, not the facts. The course lists and links in examples are real and
>   belong to the named creators. Never copy them; bring your own true, verified list.
> - Signature phrases (e.g. "Same content. Same depth. Zero cost.") work in anyone's
>   voice, but overuse reads as template. Pick one or two per post.

---

## Classification: is this actually a Resource Roundup post?

By the shared decision-signal order (the orchestrator's `tofu-pattern-analysis` reference),
a post lands in the resource family when it **hands the reader links/resources**,
before the contrarian, news, surprising-number, or how-to rules fire. Within the family:

- **One named thing/video** (a single Boris Cherny talk, one course, one doc) = Resource
  share, single. NOT this skill.
- **A numbered, multi-item free list** (7 Stanford courses, 13 Anthropic courses, 12
  repos) = **Resource roundup. This skill.**

Test: does the post's payload require 4+ distinct items the reader could save and come
back to? If yes, and those items are the point (not evidence for an argument), it's a
roundup. If the list is just proof inside an argument, it's Contrarian. Use
`tofu-contrarian` instead.

---

## The structure (near-verbatim skeleton)

The highest-performing structure (the Anthropic $10K post, the Stanford curriculum post):

```
[HOOK, 1-2 lines: named institution + free-vs-expensive inversion]
[Institution] just made [$X,000 of AI education] free.
(or)
[Institution] just dropped [their entire AI curriculum / N free courses].
(or)
I spent [N hours] learning [X]. These [N] free [resources] actually deliver.

[2-3 lines: the sweetener: count, certificates, no catch]
[N] courses. Certificates included. No catch.
(or)
Same content. Same depth. Zero cost.

[optional: the credibility or effort beat, 1-2 lines max]
I saved it. You should do the same. / I sorted them by [X] so you don't have to.

[THE REFRAME, 2-4 lines ABOVE the list, making the list mean something]
Most people "use AI" without understanding it.
They prompt. They paste. They move on.
Not access. Understanding.
(or)
That's not a skills gap.
That's a direction gap disguised as a skills gap.

[THE LIST, grouped by who-it's-for OR each item with a one-line why-this-one]
Here's the full list, organized by who you actually are:

IF YOU'RE NEW TO AI:
1. [Name]
[one line: what it is / who it's for / what it enables]
[real link]

IF YOU'RE A DEVELOPER OR BUILDER:
2. [Name]
[one-line why-this-one]
[real link]

… (5-13 items; grouped sections OR flat numbered list with per-item filters)

[THE FRAME LINE, one line making the whole list cohere]
All self-paced. All free. Certificates straight from [institution].
(or)
Most people are still Googling "how to use [X]."
The people who finish even one of these aren't.

[SAVE-BAIT closer, never a comment-gate]
Bookmark this. Share it. Actually use it.
(or)
Pick one today. Build something tomorrow.

[optional soft question, low-key, never the point]
Which track fits where you are right now?

----
♻️ Repost [so your network doesn't miss this / to save someone $2,000]
➕ Follow me ([your name]) for more [resources like this]
```

Use when: a genuinely free, credible, multi-item resource set exists (real links, real
institution), and the reader can act on it today.

**Alternate variants that still qualify as Resource Roundup** (from the golden dataset):
- *Effort-flex list*: "I spent 1000 hours figuring out Claude the hard way. Here are the
  guides I wish someone had sent me earlier" (`7463815992381480961`, Ruben Hassid, 5,449
  likes / 613 shares). The poster's own effort replaces the institution as the authority.
- *Stop-paying list*: "Stop paying for AI engineering bootcamps" + 5 free replacements +
  one personal verdict (`7428634914788376577`, Paolo Perrone, 1,653 likes / 259 shares).
- *Sequenced path*: items presented as an order to follow, not a flat list ("Here's the
  exact order I'd follow", `7487799683914829825`, Chorouk Malmoum, 4,006 likes / 571
  shares). The sequence IS the curation.
- *Use-case sorted*: "I went through NVIDIA's catalog and sorted by what builds
  execution-ready thinking" (`7431178430588735488`, Gabriel Millien). Group headers name
  the reader's goal, not the topic.

---

## Judge this archetype by ITS success metric: SHARES/SAVES, not comments

**This is the one rule that differs from every other TOFU archetype.** Across a sample of
27 resource roundups, median share/like ratio is
**0.14**, the highest of any TOFU pattern, with a median of **251 shares** per post,
against a cmt/like of only 0.06. **A resource roundup that draws comments but no shares
has NOT succeeded on its own terms**, even if raw likes are high. This is the exact
inverse of the contrarian archetype (cmt/like 0.11, share/like 0.10).

Why: people argue with a take. They don't argue with a free course list. They save it
and repost it, because reposting a credible free list makes them look generous. Every
structural choice below serves that: the footer asks for a save or repost, the reframe
gives the resharer a reason to look smart, the per-item filters make the list worth
keeping.

**Corollary on the engagement question:** a roundup may end with a light question
("Which one are you starting with?"), but the question is garnish. Never engineer the
post for comments. If the draft trades save-worthiness for debate-bait, it has drifted
into the wrong archetype.

**Scoring implication for the eval harness:** the pairwise judge and rubric still apply,
but when tuning this skill specifically, weight the dimensions that proxy for
save/share-worthiness (list utility, per-item specificity, reframe quality) as the
primary signal, not comment-bait CTA strength.

---

## Signature voice moves (use these, they ARE the voice)

- **The two-line punch closer.** A short claim, then its flip, on two lines:
  - *"That's not a feature. / That's a risk."* · *"Autonomy isn't the goal. Reliability is."*
  - *"Build the system first. The outputs follow."*
- **The free-list punch closer (roundup-specific):** *"Stop scrolling AI hype on Twitter.
  / Start learning AI from Stanford instead."* · *"Free doesn't mean low quality.
  / Anthropic's courses beat most paid ones."* · *"Pick one today. / Build something tomorrow."*
- **"Same content. Same depth. Zero cost."**, the three-beat free-vs-paid compression.
- **"Not access. Understanding."**, the two-word reframe pair. The general move: name
  the thing everyone thinks the list is about, then name what it's actually about.
- **"That's not a skills gap. / That's a direction gap disguised as a skills gap."**, the
  diagnostic reframe that sits above the list.
- **"Most people are still Googling 'how to use [X].' / The people who finish even one of
  these aren't."**, the frame line after the list.
- **"Here's the full list, organized by who you actually are:"**, the tease into the
  grouped list.
- **Curator/source credit**: you name the person who compiled the list or made the
  image ("Luís Rodrigues found one of the best lists for AI Agents", "Credit to Alex
  Issakova"). Always, when the list or visual isn't yours.

Don't force all of these into one post. Reach for the one or two that fit. Overusing the
skeleton makes posts feel templated.

---

## Formatting (the fingerprints)
- **One sentence per line.** Heavy white space. Almost every line stands alone.
- **𝗕𝗼𝗹𝗱 𝘂𝗻𝗶𝗰𝗼𝗱𝗲** for section headers and key phrases (𝟭/, 𝗦𝘁𝗼𝗽 𝗮𝘀𝗸𝗶𝗻𝗴). This is the ONE place unicode-bold is allowed, it's a signature move. **Never in the hook.**
- **↳** for sub-bullets; **→** and **•** for symptom/feature lists.
- **Group headers in plain caps** (IF YOU'RE NEW TO AI:) or emoji-tagged (📹 Videos, 🗂️ Repos) when the list is grouped.
- **`----`** or `---` divider before the footer.
- **American spelling only:** optimize, behavior, organize, realize. Never optimise/behaviour/realise/centre/colour.

## Footer (use one, match the topic)
```
[optional soft question]

----
♻️ Repost [so your network doesn't miss this / to save someone $2,000 / to help someone level up]
➕ Follow me ([your name]) for more [resources like this / AI insights]
```
Fill `[your name]` with the poster's byline. Shorter variant: *"I post AI content every day at 9 am ET. Follow me ([your name]) to get the latest."*
Optional employer-safe add: *"Opinions expressed are my own and do not represent the views, policies, or positions of my employer."*

**Save-bait belongs in the body or the footer, phrased as a favor:** *"Bookmark this.
You'll come back to it."* / *"Save this before your next deep dive."* / *"Repost to save
someone $2,000."* This is the metric the archetype is judged on. Ask for it directly.

**No newsletter signup, no link in the footer by default.** Keep the close a soft repost + follow.

**Never** a lead-magnet footer (no "Comment [WORD] and I'll DM you", no "FREE ↓", no 4-step Follow/Like/Repost/Subscribe block). That's a BOFU lead-magnet, a different skill.

---

## Hook rules (hard limits)
- **Line 1 ≤ 62 chars. Line 2 ≤ 50 chars.** Count both.
- No bold/italics in the hook.
- Roundup hook patterns: *"[Institution] just made [$X] of [Y] free."* / *"[Institution] just dropped [N free courses / their entire curriculum]."* / *"[Institution] just made every [$X course] irrelevant."* / *"[Institution] quietly dropped [N free X]."* / *"Stop paying for [expensive thing]."* / *"I spent [N hours] learning [X]. These [N] free [resources] actually deliver."* Full bank with slot tests: [`hook-template-bank.md`](./hook-template-bank.md).
- **The named institution or the effort number does the scroll-stop.** 69% of overperforming TOFU posts name a recognized entity; 41% name it in line 1. A roundup hook without a credible name (institution, company, or the poster's own verified effort) has no authority to borrow. This archetype borrows authority for a living.
- **The free-vs-expensive inversion is the tension.** State what it costs elsewhere ("$10,000", "$500 courses", "People pay thousands for this knowledge") or what's being displaced ("just made every $10K AI course irrelevant", "just killed the AI course industry"). "Free" alone is not a hook; "expensive thing now free" is.
- **Two-part test:** line 1 states the event (name + free inversion); line 2 adds the sweetener or the stakes ("Certificates included. No catch." / "Same content. Same depth. Zero cost.") the reader can't verify without expanding.
- **One reading only:** every "this/most/they/it" points at one thing.
- **Promise = payoff:** the body must actually contain the N real, working, free items the hook claims, not a tease that funnels to a paywall.

**Floor-check (run before finalizing):** the full checklist lives in `post-grader`'s `references/hook-floor-check.md` (post-grader is invoked in the draw-check-rewrite loop below);
(cross-creator structural finding, not voice-specific) — does it open a real
loop that's still open at the fold, is it concrete not abstract, is the register
casual/punchy. Resource Roundup's baseline from that analysis: opens_loop ~94% (the
highest of any archetype — a roundup hook that doesn't preview/withhold the list is
unusual, look twice at it), takes_a_side ~30% (low, this archetype curates rather
than argues), abstraction ~70% concrete (real named resources, not abstract
concepts). This checklist is a quality floor, not a virality predictor — whether the
resource itself is genuinely valuable enough to save is your call, not something
structure alone can supply.

---

## One point, zero filler
- **One list, one frame per post.** The list is the payload; the reframe is the meaning. Cut anything that serves neither. A second idea is a second post.
- **Every line earns its place.** Placeholder test: swap a line for `[generic filler]`. If nothing's lost, cut it.

## Length is not optional. Hit the target range
**Do not finish a draft under 1,800 characters.** A short, punchy-sounding draft that
stops at 600-900 characters has almost always cut the per-item filters, not the filler.
A roundup lives or dies on each item carrying a reason to exist. Before finishing,
count the characters. If under 1,800:
- **First, check every item has its one-line why-this-one or who-it's-for filter.** A
  bare name-plus-link item is the failure mode (see What NOT to do). Expand each bare
  item before adding anything else.
- **Second, check the reframe is fully built out**, the 2-4 lines above the list that
  make the list mean something. A list with no reframe is a directory.
- **Only after the list and reframe are complete**, if still short, add one more line to
  the sweetener or credibility beat. Never to the footer.
Target: 1,800-2,400 characters. 1,500-1,800 or 2,400-2,500 is acceptable but not ideal.
Under 1,500 fails the length check outright.

## Front-load the value
- Hook 2-3 lines → sweetener + reframe ≤6 lines → the list by ~line 6-9. Never bury the
  list under a long personal wind-up; the credibility beat is 1-2 lines max.

## Mobile skimmability: line geometry
- One clause per line; ≤3 lines before a blank line.
- ~7 words / ≤40 chars per line; sentences rarely over 20 words.
- ~⅓ of lines blank. Vary line length for rhythm.
- List caps: 5-13 items, grouped or flat; ≤2 sub-lines per item (one what-it-is line +
  the link). The roundup is the one archetype allowed past 5 main items. The golden set
  runs 7-13, because the value IS the volume, but only when every item keeps its filter.

## Sound human: reads like you, not AI
> **Full rule set:** `<BRAND_DIR>/writing-style.md` Part 2, the anti-fingerprint checklist + Specificity Audit.
- **Ban AI-tells:** delve, leverage (verb), harness, unlock, elevate, empower, foster, facilitate, streamline, seamless, robust, transformative, innovative, cutting-edge, navigate (metaphor), myriad, plethora, tapestry, "in the digital landscape", "in today's fast-paced world", Furthermore/Moreover/Additionally (filler), ultimately/essentially/fundamentally (filler), AI-native, "compounding", legacy (filler adjective).
- **Break structural symmetry**: vary sentence length hard; uneven list items; at least one asymmetric structural move per post. In a roundup, the risk is the opposite: identical item formatting is a feature (scanability), so put the asymmetry in the reframe and the closer.
- **Shift register at least once**: dry deadpan next to a real claim.
- **Specificity Audit, the primary gate:** ≥2 details only you could have supplied (a course you actually took, an hour count you really spent, a named curator you genuinely follow, an opinion with a scar behind it: "If I had to pick one: Karpathy. He teaches how it works, not just how to call the API."). If it can't clear the bar, **ask for the missing specific. Never invent one.**
- **No cryptic fragments**, except your deliberate two-line punch closers, which ARE complete clauses.
- **Show, don't tell.** Concrete > abstract. American spelling.

---

## Humor & personality: self-deprecating, not just dry
**A pure dry-clinical register with near-zero personal texture reads as colder and more
generated; a warmer, lightly self-mocking register reads as more human and more you.**
Pull it into roundup humor too. Topic/list/breadth stay TOFU, only the humor PALETTE
widens. Still capped at **2 beats max**. The list leads.

**Patterns to reach for (pick 1-2, spaced):**
- **Self-deprecating aside, aimed at yourself:** *"I bookmarked four of these myself,
  because apparently curating a list doesn't mean I've finished any of them."*
- **Dry sarcastic mic-drop:** *"I saved it. You should do the same. (I'm not better than you. I just have a bookmarks folder problem.)"*
- **Honest disclaimer (kept):** *"No, Anthropic isn't paying me. I checked."*
- **Incongruous register / word-swap (kept):** a medical/legal/recovery word in a
  business line.

**One confessional first-person beat allowed per post** (new): one line admitting you
also hoard free courses / haven't finished the thing you're recommending. Not a scene.

Rules: never write the laugh (no `lol/haha/😂`), never telegraph it, never make the
substance (the list, the links) the joke, and drop humor entirely on hard-news/serious
topics. Self-deprecation punches at YOURSELF, never the reader.

## Life Stories: rarely for TOFU
Your biographical vignettes live in `<BRAND_DIR>/story-bank.md`.
A pure roundup post almost never needs one. The effort-flex variant ("I spent 100h+
learning AI") uses a NUMBER, not a story. Default: write the post without one.

---

## Save-worthy / reshare-worthy gate (the primary check for this archetype)
A roundup that isn't save-worthy fails on its own terms. Every post must:
- **Hand over something keepable**: a list the reader genuinely cannot reassemble in 30
  seconds of Googling. The curation (grouping, ordering, filtering, verdicts) is the
  product; the links are the commodity.
- **Carry a filter on every item**: a who-it's-for, a why-this-one, or a where-it-fits
  in the sequence. A name plus a bare link fails this gate.
- **Earn the reshare**: resharing makes the resharer look generous and in-the-know to a
  broad network. The reframe line is what they quote when they repost.
- **Be true and current**: every link real, every course actually free, every
  institution actually the source. A dead link or a paywalled "free" course destroys the
  exact trust this archetype trades on.

---

## ⚠️ Truth & authorship (non-negotiable)
- **External facts must be real and sourced.** A free course, a course count, a
  "$10,000 of education" claim, a certificate claim: only if true, with the real link.
  Never invent a stat, a course, a number of items, or a quote.
- **Every link must be real and working.** If a link can't be verified, mark it
  `[verify link]` and flag it. Never guess a URL.
- **Credit curators and list compilers** when the list or visual isn't yours.
- **Never claim you shipped/launched a real customer product.** You're mid-build.
- **Never fabricate your numbers** (hours spent, courses taken, followers). Leave a
  `[placeholder]` and flag it if missing. The effort-flex hook ("I spent 100h+") requires
  a REAL number from you. Never round up to make the hook land.
- **Sponsored slots:** if the post carries a paid P.S. (a cohort, a certification), it
  sits below the list and the divider, visually separated, and never displaces the free
  list as the payload. One creator's own MIT post did this; note it underperformed their
  clean roundups. Default to no sponsor block unless you decide otherwise.

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

**Anti-AI pass (mandatory, runs automatically — never skip).** Before showing the draft to the user, run the `anti-ai-pass` skill on it: `python3 .claude/skills/anti-ai-pass/scripts/lint.py --stdin` with the draft text, remove every HARD banned word/phrase (quietly, silently, leverage, actually, etc.), keep at most ONE structural move (Most-people / Not-X-Y / Everyone-wants-X) and only if >=2 real specifics sit behind it, and fix rhythm tells (rule-of-three, -ing tails, em dashes). This is BUDGETED, not absolute — one proven hook move is allowed; stacking two or more is the machine tell. Load `anti-ai-pass/SKILL.md` for the full judgment layer.

### 1. The Post
Full text as it'd appear on LinkedIn. Plain text, no code fences.

### 2. The value being handed over
One sentence: "This post hands the reader ___ (a list of N free X from Y), and the
reframe makes it mean ___ (the thing beyond access)."

### 3. Facts to verify
Every course/resource name, link, count, price claim, certificate claim, curator credit,
and effort number the post asserts. Flag `[placeholders]` and unverified links.

### 4. Self-Check (all ✅ or revise)
- Hook L1 ≤ 62 (actual: __) · L2 ≤ 50 (actual: __) · two-part test passes ✅
- Named institution / company / real effort number in the hook ✅
- Free-vs-expensive inversion or equivalent stakes present ✅
- One list, one frame, no second thread ✅
- Every item carries a filter (who-it's-for / why-this-one / sequence position). Zero bare links ✅
- Reframe line sits ABOVE the list and makes it mean something ✅
- Value front-loaded, list starts by ~line 6-9 ✅
- Every external fact real/sourced; every link real or flagged; curators credited ✅
- No claim you shipped a customer product; no invented personal numbers ✅
- Your voice present, at least one signature move ✅
- Formatting: one sentence per line, ↳/→, divider + `[your name]` follow footer ✅
- Reads human: Specificity Audit ≥2 un-generatable details; sentence-length variance; ≥1 register shift; no AI-tells ✅
- Humor: 0-2 dry beats max; no telegraphed laughs ✅
- CTA is SAVE-bait + soft repost/follow. No comment-gate, no debate-bait ✅
- Optimized for shares/saves, not comments. The inverse of the contrarian skill ✅
- Mobile geometry ✅

---

## What NOT to do
- ❌ Fabricating a course, a count, a price claim, or a link. If it isn't real and free,
  it isn't in the list.
- ❌ **A bare name-plus-link list.** Name + URL with zero per-item filter and zero
  reframe reads as a directory, not a roundup, per `resource-curation.md`'s "posts that
  lead with self-promotion consistently underperform" finding and the general-list
  antipattern data in `content-research/frameworks/antipatterns.md`. Every item carries
  a filter or the post fails.
- ❌ **No reframe above the list.** A list that means nothing gets saved by nobody. Real
  institution and real use-case sorting are not enough on their own if there's no line
  that makes the list mean something beyond access. The list needs its "Not access.
  Understanding." moment.
- ❌ **Hype numbers instead of borrowed authority.** The clearest real example: "10 Free
  Courses. 100 days. 1000x your builder skills" ( 48
  likes, 2 shares, share/like 0.042 — a weak roundup example).
  A self-referential promise with no institution behind it, plus an unearnable guarantee
  ("Day 100: full stack app with auth and payments"), is a claim nobody can verify and
  nobody reshares. The hook borrows authority (Stanford, Anthropic, MIT) or stakes (real
  hours spent); it never manufactures hype. Full breakdown in `examples.md`.
- ❌ Burying the list under a long wind-up. Front-load.
- ❌ Two lists or two frames in one post.
- ❌ A lead-magnet comment-gate ("Comment LIST and I'll DM it"). That's BOFU.
- ❌ Engineering for comments instead of shares. The wrong metric for this archetype.
- ❌ Claiming you shipped a real customer product, or inventing your hours.
- ❌ Over-templating. Don't cram every signature move into one post.
- ❌ AI-tell vocabulary, prose blocks, or unicode-bold in the hook.
- ❌ Weak or self-fighting hook/CTA mechanics. Three real underperforming roundups
  verified in `examples.md`: "7 free AI courses every smart founder is taking" (145
  likes, 5 shares, share/like 0.034) skips the sweetener and reframe beats and never
  names a single borrowed authority; "MIT just released 10 AI courses for FREE" (315
  likes, 45 shares, share/like 0.143) gets the grouping right but splits its CTA between
  a comment-gate ask and an unrelated self-promotional PS; "10 Free Courses... 1000x
  your builder skills" (48 likes, 2 shares, share/like 0.042) has no borrowed authority
  at all. See `examples.md` for the full structural breakdowns against the Anthropic
  $10K high performer.
- ❌ Recycling a dead list without refreshing it. Real example: a writer's own
  "$10K of AI education free" post, reposted verbatim five months later — same text,
  same list, only the sponsor PS changed. Result: 57 likes, 55
  comments, **0 shares**, against the original's 358 shares. A roundup's authority is
  tied to the freshness of the event it announces ("just made... free"); the same claim
  is only borrowable once. Refresh the substance or pick a new list.

## Reference Corpus
See [`examples.md`](./examples.md) for one full worked high-performer (the Anthropic
$10K post, 1,675 likes / 358 shares, share/like 0.214) with a structural breakdown, and
the hook template bank in [`hook-template-bank.md`](./hook-template-bank.md) (10
templates extracted from a golden set of real high-performing posts). The
low-performer negative-anchor section in `examples.md` holds three real
underperformers (145/5, 315/45, and 48/2 likes/shares) plus a stale-repost
example (the same text reposted months later, dropping from 358 to 0 shares),
with structural breakdowns against the high performer above.
