# TOFU Top-Performer Analysis — data-derived patterns & drivers

**Source:** all **214** posts in Supabase where `funnel_stage = 'tofu'` and `x_factor ≥ 2`
(i.e. TOFU posts that beat their own author's 30-day weighted baseline by ≥2×).
Cross-checked against the top-55 by `x_factor` (read in full).

**Generated:** 2026-06-11. Re-run by re-querying the same filter; numbers are directional.

> ⚠️ **Provenance & honesty note.** The funnel split (`funnel_stage`) and the
> overperformance metric (`x_factor` = weighted score ÷ author's own 30-day baseline,
> weights likes×1 / comments×3 / shares×5) are **computed columns** — real and
> reproducible. The **pattern labels below are NOT a database column.** They were
> derived by (a) a heuristic feature-matcher over all 214, then (b) hand-validation by
> reading the fuzzy buckets. Counts are ±2–3 per bucket. A future `tofu_pattern` column
> populated by a Claude classifier would make this exact and reproducible — this doc is
> the analysis that would seed that taxonomy.

---

## Headline numbers

Median overperforming TOFU post: **1,904 likes · 140 comments · 175 shares · 2.8× baseline.**
Top of set: **14.6×** (Google `agents-cli` launch breakdown).

| Driver (across all 214) | Frequency |
|---|--:|
| Recognized entity named *anywhere* (Google, Apple, NVIDIA, Anthropic, Stanford, Boris Cherny…) | **69%** |
| Recognized entity in **line 1** | **41%** |
| Carries a hard `$` figure | 19% |
| Carries a `%` figure | 20% |
| A digit in line 1 | 31% |
| Contains a link | 47% |
| Says "free" | 30% |
| Line-1 hook ≤ 60 chars | 64% |

Overperformers usually **stack 2+** drivers (e.g. recognized name *and* a hard number;
free resource *and* a credible source).

---

## The data-derived clusters

| Pattern | n (~) | med likes | med cmts | med shares | **share/like** | **cmt/like** | Wins via |
|---|--:|--:|--:|--:|--:|--:|---|
| Contrarian myth-bust | 52 | 1,768 | 182 | 180 | 0.10 | **0.11** | **comments** |
| Resource share — single (one named thing/video) | 38 | 1,813 | 133 | 150 | 0.09 | 0.06 | shares |
| Surprising-number / economics take | 32 | 1,780 | **230** | 154 | 0.08 | 0.08 | **comments** (absolute) |
| Resource roundup — multi-item free list | 27 | 2,052 | 115 | **251** | **0.14** | 0.06 | **shares** |
| News / Launch breakdown | 21 | 1,500 | 113 | 135 | 0.09 | 0.06 | shares + comments |
| Meme / one-liner image | 16 | **2,712** | 134 | 86 | **0.03** | 0.05 | **likes** |
| Tactical how-to / setup tips | 13 | 2,067 | 99 | 182 | 0.10 | 0.07 | shares (saves) |
| Relatable mirror / wisdom | ~13 | 3,040 | 183 | 259 | 0.08 | 0.08 | shares + likes |
| Conceptual explainer | ~7* | high | low-med | high | 0.11 | 0.03 | shares (saves) |

\* heuristic routed most explainers into how-to/resource; top-55 read shows ~7 distinct.

---

## The single most actionable finding: **engagement shape is per-pattern**

The old skill rule — *"judge TOFU by reshares, not comments"* — is right **on average**
but **wrong per-pattern**. The data splits cleanly by *what kind of reaction the pattern earns*:

- **Reshare engines** → **Resource roundup** (share/like **0.14**, med **251 shares**),
  conceptual explainer, tactical how-to. People repost a free list / a clean breakdown to
  look **generous or in-the-know**.
- **Comment engines** → **Contrarian** (cmt/like **0.11**) and **economics** (med **230 comments**).
  People **argue** with a take; they don't argue with a resource.
- **Like engine** → **Memes** (med **2,712 likes**, but share/like only **0.03**).
  Reach comes from likes + algorithmic lift, *not* reshares.

→ **Judge each pattern by its own success metric.** A winning contrarian lives in the
comments; a winning roundup lives in reshares; a winning meme lives in likes.

> **Correction to an earlier read:** memes are NOT a reshare play. One outlier meme
> (the token / player-character post, 626 shares) created that false impression; the
> *typical* meme is high-like / low-share.

---

## Patterns the original 6-pattern skill was hiding

1. **Meme / one-liner image** (~16, 7.5%) — "Every vibe coder 😂😂😂," "McDonald's AI is free,"
   "Me vs ChatGPT." Near-zero body text on an image/joke. Was crammed into "Relatable Mirror"
   but is mechanically different (visual-first, like-driven) and prose-post advice can't teach it.
2. **Single-authority share ≠ multi-item roundup.** Boris Cherny's "master Claude Code in 15 min"
   recurs **3×**. One named expert + one free thing + get out of the way. Highest trust-per-word
   resource play; was folded into "Roundup."
3. **Aphorism / universal wisdom** — "Six real luxuries in life" (3,411L), "Four simple rules that
   solve 90% of problems" (3,630L), "Weak leaders pass pressure down," "13 Lessons from 13 Years."
   Overperform hard; not *about* the topic at all. The 6 had no home for these.
4. **Tactical how-to / setup tips ≠ conceptual explainer.** ".claude folder," "4 habits that make
   Claude Code reliable" (do-this lists) are distinct from "how Mixture-of-Experts works"
   (decode-the-concept). The skill collapsed both into "Explainer."
5. **Branded recurring infographic series** — the "Become better at AI in 1 minute a day" family
   (ChatGPT Cheat Sheet, Claude Cheat Sheet, MCP vs RAG vs Skills, "100+ AI Tools," AI-as-human-analogy).
   A *format+brand wrapper*, not a content type — but repeatable and high-share.

---

## How to tell the patterns apart — decision signals (classify by mechanism, in this order)

The rule the data enforces: **classify by what the post HANDS the reader** — a link, a number,
a belief, a how-to, a laugh — **not by its topic.** A launch full of numbers is still *News* if
line 1 is the event.

1. **< 2 lines of text + image/joke carries it** → **Meme**
2. **Hands over a link/resource** → Resource family →
   *one named thing/video* = **Single-share**; *a numbered free list* = **Roundup**
3. **Line 1 anchored to a dated event** ("just open-sourced," "stepping down," "BREAKING") → **News/Launch**
4. **Core payload is one jarring figure** ($27K, -93%, 98.7%) → **Surprising-number**
5. **Asserts a belief is wrong** ("it's bullshit," "stop hiring on years") → **Contrarian**
6. **Body is a do-this step/tip list** (".claude folder," "4 habits") → **Tactical how-to**
7. **Body decodes how a thing works** (MoE, vectorless RAG) → **Conceptual explainer**
8. **Universal truth, topic-agnostic** ("six real luxuries") → **Aphorism / wisdom**

---

## What drove the overperformance (the x_factor levers)

1. **Borrowed authority.** 69% name a recognized entity; 41% in line 1. The recognized name
   does the scroll-stop for free. No-name posts lean harder on a hard number.
2. **Hard specific numbers.** 19% `$`, 20% `%`. Specificity reads as proof; round/vague numbers
   don't travel. The economics cluster lives entirely on this.
3. **Free + credible source.** 30% "free," 47% a link. The reshare champions.
4. **Tight mobile geometry.** 64% have a line-1 hook ≤60 chars; one short idea above the fold.
   Confirms the skill's existing geometry rules — keep them.

---

## Recommended next steps (not yet built)

- Add `tofu_pattern` + `tofu_pattern_reason` + `success_metric` columns to `posts`; populate via a
  Claude classifier over all TOFU posts (the heuristic here gets ~80% there for free).
- Validate the cluster *count* (this analysis says ~8–9, not 6) with a bottom-up clustering pass.
**Both TOFU skills (structural + voice) were updated from this doc.**
