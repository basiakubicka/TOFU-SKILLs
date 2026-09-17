---
name: hook-mechanics
description: "Given a topic/post AND its post type (which of the 8 TOFU archetypes, or MOFU/BOFU), generates hook options by MATCHING THE MECHANIC to the archetype and the substance actually available - not by defaulting to whichever hook has the highest recorded X-factor. Reverse-engineered from 361 real outlier hooks (2x-4,153x X-factor), organized as 10 templatized MECHANICS (fixed words + slot tests, not vibes), each cross-tabbed against which TOFU archetypes it structurally fits and why. Hard rules: line 1 <=62 / line 2 <=50 chars; every mechanic must have a real, checkable substance match before use (a real name for authority-borrow, a real number for stat-shock, a real contrast for good-vs-bad) - never force a mechanic the topic can't support; never fabricate a stat/quote/name. Use when the user wants hooks for a specific post/topic AND wants the hook to fit the post's actual type and available substance, not just 'give me your best hooks.'"
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md` to all copy this skill generates (spartan, active voice, short sentences,
no em dashes, the banned-word list, etc.) — this applies to the ENTIRE deliverable,
including the archetype/substance analysis scaffolding and mechanic-fit reasoning, not
only the hook lines themselves. (Found in this skill's own head-to-head eval: the
analysis text used em dashes and banned words like "quietly"/"actually" even when the
hook lines were clean — the rule was being read as hook-only, which it is not. A
second pass after this fix STILL leaked em dashes into scaffolding text — if you notice
this happening, re-read this line: replace every em dash in your own commentary with a
period, comma, or semicolon before output, the same way the hook lines already do.)

# Hook Mechanics — Match the Mechanism to the Post, Not the X-Factor

This skill exists to fix one structural flaw in the naive approach:
**defaulting to whichever hook has the highest recorded engagement**, regardless of
whether that hook's mechanism actually fits the post type or the substance on hand. A
1268x outlier about a supermarket copying pizza-dough products doesn't help someone
writing a resource roundup — the number is seductive, the mechanic is irrelevant.

This skill inverts the selection logic: **first identify the post's archetype and its
real available substance (a name? a number? a contrast? a story?), THEN pick the
mechanic(s) that structurally fit** — offering several genuine options at different
points in the X-factor range, not the single highest number.

**This is a hook generator, not a full-post drafter.** Output is hook options (line
1-2) plus the archetype fit reasoning. Hand off to the matching TOFU archetype skill
(via `tofu-orchestrator` if unsure which) to draft the full post.

---

## The core fix: substance-gated mechanic selection, not X-factor-first

Never ask "which hook has the biggest number." Always ask, in this order:

1. **What TOFU archetype is this post?** (use `tofu-orchestrator` if unsure)
2. **What real substance does this specific post actually have available** — a
   checkable number, a named source/person, a genuine contrast, a lived story, a
   countable list, a real contradiction? A mechanic with no real substance behind it
   gets rejected here, before it's ever offered, no matter its X-factor.
3. **Which mechanic(s) does that combination of archetype + substance support?** (the
   cross-tab table below)
4. **Within that shortlist, offer options spread across the X-factor range** — a
   modest, safe mechanic AND a bigger swing, not just the top of the list.

---

## The 10 mechanics (fixed template + slot test + real spread, not vibes)

Each mechanic below follows `templatizing-content-patterns`: fixed words with the
slot's description written INSIDE the bracket, a slot test, a why-it-works note, and
3 real examples spanning low/mid/high X-factor from the actual dataset — proving the
mechanic works across a range, not because of one outlier's fame.

### 1. Counter Opinion
**Fixed template:** "[The thing/group everyone currently praises or assumes]. [Flip
into the poster's genuine dissent or reframe, stated flatly]."
**Slot test:** the "everyone believes X" claim must be a real, checkable consensus (not
a strawman invented to sound edgy) — and the poster's actual dissent must be something
they'd defend if challenged in the comments.
**Why it works:** readers who privately hold the same doubt feel validated; readers who
don't get a real argument to push against — either way, comments follow.
**Real spread:**
- `4.3x` — Tas Bober: "Everyone's excited about the LinkedIn Year in Review but is the data fake?"
- `38x` — Line Lybo Uppard: "This is my claim: The busier you are, the worse a leader you are!"
- `1142x` — Alex McCann: "Last week, I had coffee with someone who works at a big consulting firm. She spent twenty minutes explaining her role to me. Not because it was complex, but because she was trying to convince herself it existed"
**Archetype fit:** Contrarian (direct match — this IS the contrarian mechanic). Also
works for Relatable Mirror if the flip empathizes rather than prosecutes (see the
empathize-vs-prosecute distinction in `tofu-relatable-mirror`'s classification).

### 2. Perception vs. Reality
**Fixed template:** "[The assumed goal/reason people think X exists for]. [The real,
truer goal/reason, stated as a correction]."
**Slot test:** both halves must be genuinely different claims about the SAME thing, not
two unrelated observations — the reader must feel their assumption specifically
corrected, not just informed of a new fact.
**Why it works:** creates a small "oh" moment — the reader re-files something they
thought they understood, which is inherently shareable ("I didn't think of it that way").
**Real spread:**
- `5.4x` — Marilyne Defer: "We live in a world / Where the things that sell..."
- `64x` — Divakar Vijayasarathy: "Why being right isn't everything"
- `750x` — Andy Hillocks: "The content you create isn't about forcing everyone to like you. / It's about putting out content for those who are looking for you."
**Archetype fit:** Explainer (the "most people think X, they're wrong" hook IS this
mechanic), Contrarian, Relatable Mirror (when the correction is about a felt experience,
not an argued position).

### 3. Good vs. Bad (Juxtaposition)
**Fixed template:** "[Short claim about the surface-level/lesser version of a thing].
[Short claim about the deeper/real version], on its own line."
**Slot test:** both lines must be genuinely comparable categories (not just two
adjectives) — "influence vs impact," "titles vs the real luxuries," not "good vs bad"
restated vaguely.
**Why it works:** the visual/rhythmic contrast of two short parallel lines does the work
before the reader even processes the content — it reads as wisdom by its shape alone.
**Real spread:**
- `2x` — Lindsay Linhart: "Stop shrinking yourself to make others comfortable with their limitations."
- `29.2x` — Laurie Banfi: "I'm getting pickier about who I work with. / Not in an exclusive way."
- `1228x` — Maya Moufarek: "One image just disrupted a £22 billion fashion empire more effectively than a thousand sustainability reports."
**Archetype fit:** Contrarian (the two-line punch closer IS this mechanic, reused as a
hook), Relatable Mirror (Shape A short reframe), Explainer (as a metaphor-lead hook).

### 4. Harsh Truths
**Fixed template:** "[A blunt, uncomfortable fact about a group/situation, stated
flatly] / [A restatement in the slower, less comfortable version people avoid saying]."
**Slot test:** the truth must be something the audience privately knows but doesn't say
out loud — not a generic complaint. If a stranger would go "well, obviously," it's too
soft; if they'd go "...yeah, actually," it's right.
**Why it works:** naming what people avoid saying out loud creates instant credibility
("this person gets it") and gives the reader permission to admit it too.
**Real spread:**
- `2x` — Haris Halkic: "10 Things No One Tells You About Being in Sales (The stuff that's not in any handbook)"
- `27x` — Emma King: "Good employees don't just quit / They slowly walk out the door."
- `401x` — Amanda Gautier-Ronopawiro: "AI is everywhere. In general, as many other (medical) illustrators I am sure, I have feared it will one day take our jobs."
**Archetype fit:** Contrarian, News Breakdown (when the "harsh truth" is what a named
source just revealed), Relatable Mirror (as the opening validation before the reframe).

### 5. Story-Open
**Fixed template:** "[A time marker + a mundane, specific setup detail]. [The turn that
doesn't fit the setup, creating the gap]."
**Slot test:** the setup must be genuinely mundane/ordinary (not already dramatic) so
the turn has somewhere to fall from — and the turn must be a real, true event, never
invented to manufacture drama.
**Why it works:** the only mechanic where a LONGER hook is acceptable, because the
intrigue comes from narrative momentum, not compression — the reader is already inside
a scene and needs the next beat to resolve it.
**Real spread:**
- `5.5x` — Eric Arzubi: "They called her a troublemaker. / A disruptor. / A threat to the system."
- `95x` — Susan Chen: "Right before burnout, there's a feeling. / I call it 'crispy.'"
- `1268x` — Giuseppe Baidoo: "A supermarket copied my products... so / I dressed like a thief."
**Archetype fit:** Relatable Mirror (Shape B, the vulnerability-beat opener), MOFU
(this is fundamentally a personal-arc mechanic — flag if the "story" is actually
someone else's arc, since that's News Breakdown instead).

### 6. Deep Dive / Cheat Sheet
**Fixed template:** "[A real, checkable scale-of-effort marker: a page count, a time
span, a name-dense list]. [What the reader gets for that effort, stated as a payoff]."
**Slot test:** the scale marker must be real and verifiable (a genuine 160-page guide,
a genuine list of named sources) — inflating "quick tips" into "the deep dive" without
real density behind it breaks the promise on open.
**Why it works:** signals high, bookmarkable value before the reader even opens it —
this is a save-trigger mechanic, not a comment-trigger one.
**Real spread:**
- `3.8x` — Rakesh Gohel: "160+ page guide covers top questions regarding Multi-AI Agents"
- `54x` — Sophie Deen: "Silicon Valley parents limit screen time / While selling infinite scroll to yours. / That should tell you everything."
- `871x` — Erika Kullberg: "Tomorrow (Nov 3), LinkedIn is making a change that affects your data (and privacy). / And they're hoping you won't notice."
**Archetype fit:** Resource Roundup, Explainer (the "N layers" numbered-stack-map hook
is a Deep Dive variant), How-To (the setup-scale promise).

### 7. Feel Goods
**Fixed template:** "[A warm, specific, small moment or memory, named concretely].
[The gentle lesson it carries, stated simply, no lecture tone]."
**Slot test:** the moment must be specific enough to be real (a real callback, a real
memory) — a generic inspirational platitude with no concrete anchor fails this mechanic
even if it sounds warm.
**Why it works:** wins on likes and shares, not comments — readers tap and pass it on
because it feels good, not because they want to argue or reference it later.
**Real spread:**
- `3x` — Gözde Imamoglu: "Who remembers this legend? / Time to bring that energy back."
- `19.2x` — Marta Duda: "The fastest way to learn anything? / Start before you feel ready."
- `457.34x` — Corporate Gags: "Grab your corporate emails dictionary desk sign at CorporateGags.com" (meme-adjacent, platform-native humor)
**Archetype fit:** Relatable Mirror (Shape A), Meme (the warm/humor register, not the
prosecutorial one).

### 8. Listicle Promise
**Fixed template:** "[A common assumption about what makes X valuable, named]. [The
real, quieter thing that actually matters], introducing a countable set."
**Slot test:** the count must be real — decide the number before writing the hook, not
after, so the list that follows actually delivers that count.
**Why it works:** the "everyone chases X but the real thing is Y" flip plus a countable
promise combines two proven triggers — the reframe AND the scannable payoff.
**Real spread:**
- `6.3x` — Costas K. G.: "Degrees impress. / But self-education transforms."
- `26x` — Lee Ann Chan: "Most people chase titles, salaries, and fancy job perks. / But the real career luxuries are far quieter."
- `103x` — Max Perzon: "Past 12 months I paid Alex Hormozi, Iman Gadzhi & 8-figure entrepreneurs $80,000 in total. Here's what I learned"
**Archetype fit:** Resource Roundup, How-To (numbered steps), Relatable Mirror (numbered
reflections, per its own hard line against confusing reflections with runnable actions).

### 9. Curated Resources / Authority-Stack
**Fixed template:** "[A list of 2+ REAL recognized names/institutions, named directly].
[What they collectively teach/prove, or the effort spent curating them]."
**Slot test:** every named institution/person must be real and actually connected to
the resource — never borrow a famous name's credibility for a list they have nothing to
do with.
**Why it works:** stacks multiple authority-borrows in one hook (each name is its own
scroll-stop), then the "I did the curation work" framing adds a second, effort-based
authority layer on top.
**Real spread:**
- `2x` — Alex Barády: "10 must-read AI strategy playbooks, / From Google, Microsoft, McKinsey, and others"
- `9.5x` — Sairam Sundaresan: "MIT. Stanford. DeepMind. Berkeley. UMich. / 8 playlists that teach AI better than most $120k degrees"
- `488x` — Martin Vonderheiden: "I curated and reviewed 16 AI strategy playbooks so you don't have to."
**Archetype fit:** Resource Roundup (direct match — this is the priced-thing-made-free
/ named-institution mechanic from `tofu-resource-list`'s own hook bank).

### 10. Old vs. New / Named Threshold Event
**Fixed template:** "[A real, named person/entity/system just crossed a threshold or
changed]. [The one-line implication, stated flat, no editorializing]."
**Slot test:** the event must be real, dated, and verifiable — this mechanic borrows
its authority entirely from the named event actually having happened.
**Why it works:** combines a real news-event trigger with a flat, confident implication
line that does the reader's thinking for them in one beat — "let that sink in" instead
of explaining why it matters.
**Real spread:**
- `8x` — Jonathan Whipple: "AI changed the rules. / Most job seekers didn't."
- `57.2x` — Stephen Klein: "Yann LeCun just left Meta. / Let that sink in."
- `134x` — Jimi Gibson: "SEO isn't dying. / It's mutating into something new."
**Archetype fit:** News Breakdown (direct match — this is the "[Name] just did X" hook
mechanic), Surprising Number (when the "threshold" is a number, not an event).

---

## Cross-tab: which mechanics fit which TOFU archetype (the actual fix)

This is the table that replaces "give me your top hooks" with "give me hooks that fit
THIS post." Consult this before offering any hook.

| Archetype | Primary mechanics (default reach-for) | Secondary (if the substance supports it) |
|---|---|---|
| Contrarian | Counter Opinion, Good vs. Bad, Harsh Truths | Perception vs. Reality |
| Explainer | Perception vs. Reality, Deep Dive/Cheat Sheet | Good vs. Bad (metaphor-lead) |
| How-To | Listicle Promise, Deep Dive/Cheat Sheet | — |
| Resource Roundup | Curated Resources/Authority-Stack, Listicle Promise | Deep Dive |
| News Breakdown | Old vs. New/Named Threshold, Harsh Truths | Deep Dive |
| Surprising Number | Old vs. New (numeric threshold variant) | Harsh Truths (if the number IS the harsh truth) |
| Relatable Mirror | Story-Open (Shape B), Good vs. Bad (Shape A), Feel Goods | Counter Opinion (if empathizing, not prosecuting), Listicle Promise (reflections) |
| Meme | Feel Goods (humor register) | Good vs. Bad (visual contrast) |

**If a topic's best-fit mechanics span 2+ archetypes** (e.g. Perception vs. Reality
fits both Explainer and Contrarian), that's often a sign the SAME topic supports
multiple valid archetypes — route back to `tofu-orchestrator`'s "present the
options" step rather than picking one silently.

---

## The 5-step workflow

### Step 1 — Get the archetype
If the user hasn't said which TOFU archetype this is, ask, or run it through
`tofu-orchestrator` first. Don't guess silently — the whole point of this skill
is archetype-aware hook selection.

### Step 2 — Inventory the real substance
Before picking any mechanic, name what's actually available: a real checkable number? A
real named source/person? A genuine contrast between two things? A true personal story?
A countable list? Write this down as a short inventory — it's the gate every mechanic
below has to pass.

### Step 3 — Filter the cross-tab to what's BOTH archetype-fit AND substance-supported
From the archetype's primary + secondary mechanics (table above), keep only the ones
whose slot test (in the mechanic bank) the topic can actually pass. A mechanic that's
archetype-fit but has no real substance behind it gets dropped here, no exceptions —
this is the truth gate, not a style preference.

### Step 4 — Generate options spread across the mechanic AND the X-factor range
For each surviving mechanic, pull 1-2 real reference examples spanning different points
in that mechanic's X-factor range (not just the top one) to show the mechanic's
range, then write a fresh hook for the topic. Aim for 6-10 total hooks across 2-4
different mechanics — never 10 variations on one mechanic.

### Step 5 — Label every hook with its mechanic + a real reference range
Every hook ships with: which mechanic, which archetype(s) it fits, and 1-2 named real
examples (with X-factor) showing the mechanic actually works across a range — not just
citing the single highest number as if that's why the hook will work.

---

## Output format

**Default: hooks only, numbered, nothing else.** This is what the user asked for most
of the time — they want to read hook options, not a report about hook options.

```
1.
[Line 1]
[Line 2]

2.
[Line 1]
[Line 2]

(repeat for all hooks, 6-10 total)
```

That's it. No archetype/substance preamble, no mechanic labels, no reference citations,
no per-hook "why this fits" notes, no recommendation section — none of that in the
default output. Do the archetype/substance/mechanic-selection reasoning (Steps 1-4)
silently, internally, exactly as before; it still gates which hooks get offered. It
just never gets printed. If a hook is a placeholder-flagged or substance-thin option
(e.g. the Old vs. New secondary-angle case), fold that caveat into the hook itself
being visibly different in register, or simply don't offer it, rather than printing a
disclaimer paragraph.

**Only add reasoning back in if asked.** If the user says something like "explain
your picks," "why these," "show your work," or "which mechanic is this," THEN show the
fuller format below, once, for that turn only — don't default back to it on the next
request unless asked again.

```
### Archetype: [name]
### Mechanics used: [list]

1. [Mechanic] — modeled on [creator, X-factor]
[Line 1]
[Line 2]

(repeat)

### Recommendation: [1-2 picks + why, tied to the archetype's judged success metric]
```

---

## Hard rules (every hook must pass)

**Geometry:** Line 1 ≤ 62 chars. Line 2 ≤ 50 chars. Exception: Story-Open hooks may run
longer if the post is genuinely narrative — the intrigue must still land in line 1.

**The truth gate (non-negotiable):** every mechanic's slot test above is a truth gate,
not a style note. Never fabricate a number, name, quote, or contrast to force a
mechanic that doesn't fit. If the substance inventory (Step 2) doesn't support a
mechanic, drop it — don't stretch the topic to fit a good-sounding hook.

**Never import a number, price, or stat that wasn't in the brief/post**, even flagged
"verify before posting." A `[bracketed placeholder]` is the only acceptable way to hold
a slot open for a real figure the user hasn't supplied yet — writing in a plausible
number and flagging it after the fact is fabrication with a disclaimer, not a fix. This
was a real regression found in this skill's own head-to-head eval against
`x-factor-hooks` (a $5/$25 price pair invented for a News Breakdown case) — the
predecessor skill's discipline of always using `[placeholder]` instead of a guessed
number is the correct behavior and must be matched here.

**Never attach a real X-factor figure to a creator's name as if it were a quoted or
verified stat from this run.** The X-factor numbers in this skill's own reference
banks describe THAT bank entry's historical performance — they are citations for why a
mechanic is proven, never a number to restate as if the current post's author achieved
it. Conflating "this mechanic has hit 488x for someone else" with "so this draft will
too" is a second real regression found in eval (attaching 488x/871x/9.5x to creators'
names as if quoting them, after the source data wasn't even available to check).

**Never lead with the single highest X-factor example as the justification.** Every
mechanic entry above intentionally shows a low/mid/high spread — cite the spread, not
just the top number, when explaining why a mechanic is proven.

---

## The floor-check gate — run this AFTER picking a mechanic, BEFORE finalizing

**Not a voice-specific rule — a cross-creator structural finding.** Full checklist,
methodology, and real before/after examples live in
`<BRAND_DIR>/hook-floor-check.md` (pulled from the general LinkedIn corpus, any
author — not your own writing). Run it on every hook + rehook AFTER picking a
mechanic from this skill's bank, before finalizing. TL;DR: does it open a real
unresolved loop that's still open at the fold, is it concrete over abstract, is the
register/direct-address right for the archetype (per-archetype baselines in that
file). It's a quality floor against wasted execution, never a virality score —
whether the underlying take is charged enough to land is the human's call, not
something mechanics alone can supply.

---

## What NOT to do
- ❌ Offering hooks before confirming the archetype — this defeats the entire point of
  this skill over its predecessor.
- ❌ Picking a mechanic because it has the highest X-factor in the dataset, ignoring
  whether it fits the archetype or the real substance.
- ❌ Forcing a mechanic whose slot test the topic can't pass (inventing a name, a
  number, a contrast that isn't real).
- ❌ Generating 10 hooks from 1 mechanic — always spread across 2-4 for genuine option
  variety.
- ❌ Citing only the top-X-factor example per mechanic as proof it works — always show
  the range.

## Eval status
Validated head-to-head against a naive highest-engagement baseline: this skill won on
archetype/substance fit across repeated pairwise judging. The mechanics below are the
promoted set.

