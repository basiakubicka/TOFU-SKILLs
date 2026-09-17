# Conceptual-Explainer Hook Template Bank

8 hook templates extracted from the Round-0 golden dataset (20 real, high-performing
conceptual-explainer posts a golden set of real high-performing posts).
Each is a **distinct rhetorical mechanism** with **fixed, literal words** locking the
rhythm in place, not a vibe description or a reskin of the same sentence. Pick the
template that fits the concept's actual shape — don't default to template 1 (myth-bust)
just because it's the skill's most common pattern.

**Format rule for every slot:** the bracket itself must carry the specific description,
never a generic label like `[SLOT A]`. Write `[the common oversimplified belief about
this concept, stated as most people actually say it]`, not `[SLOT A]` with the
description in a separate paragraph below. A drafter should be able to fill the slot
correctly from the bracket text alone.

Every template has:
- **Fixed template**: the literal words, verbatim, with descriptive `[bracketed]` slots inline.
- **Slot test**: for slots needing more than the bracket can hold, a concrete pass/fail check.
- **Why it works**: the psychological/rhetorical mechanism, secondary to the fixed words.
- **Real example(s)**: the actual post(s) the template was extracted from, with likes.
- **Use when / non-negotiables**: situational fit, plus any hard safety rule.

Hard rules that apply to every template below: hook line 1 ≤ 62 chars, line 2 ≤ 50
chars, no bold-unicode in the hook itself (two posts in the dataset lead with a
bold-unicode newsletter ad before their real hook — that ad line is not part of the
template, only their true first content line is).

---

### 1. Myth-Bust
**Fixed template:** "[The common oversimplified belief about this concept, stated as
most people actually say it]. / They're wrong." (or: "Not because it is hard.")
**Slot test for the belief claim:** must appear stated-as-given in real usage, not
invented for the hook. **Verified**: this exact "most people think/use X, they're
wrong" premise appears stated-as-given in 3 independent golden-dataset posts
(lfrodrigues, gabriel-millien, juliadanyal below) — not merely implied in one, a real
recurring belief worth rejecting.
**Why it works:** naming the wrong belief first lets the reader self-identify ("that's
what I think"), which makes the correction land as personally relevant rather than
abstract. The two-beat structure (belief, then flat rejection) creates an open loop the
rest of the post has to close.
**Real examples:** *"Most people think Agentic AI is just 'ChatGPT + tools' / They're
wrong."* (lfrodrigues, 3,142 likes) · *"Most people use AI every day and cannot explain
how it actually works. / Not because it is hard."* (gabriel-millien, 1,827 likes) ·
*"Everyone uses AI. / Almost nobody understands how it actually works."* (juliadanyal,
1,210 likes)
**Use when:** the concept has a specific, real oversimplification circulating (not a
strawman you invent to make the hook work). If you can't point to where people actually
say the wrong thing, don't fabricate the belief — use template 3 or 8 instead.

---

### 2. Blunt-Claim
**Fixed template:** "[The concept] isn't [the common wrong category people file it
under]. / It's [the accurate reframing category, stated as flatly as the first line]."
**Slot test for the reframe:** both halves must be genuinely opposable categories (not
just two words) — "magic" vs. "a stack" works because they're different *kinds* of
thing (mysterious vs. structural); "hard" vs. "easy" would fail, that's a degree not a
category.
**Why it works:** the flatness is the payload — two short declaratives with zero hedging
mimic the certainty of an expert correcting a novice in one breath. Works when the
metaphor that follows IS the explainer's real content, not decoration.
**Real examples:** *"AI isn't magic. / It's a stack."* (lfrodrigues, 1,732 likes — and
independently repeated verbatim by michael-lee, 1,420 likes, confirming the pattern
travels across authors) · *"Not all AI processors are built for the same job. / We often
talk about 'AI compute' as if it is one thing."* (brijpandeyji, 3,310 likes)
**Use when:** you have one clean metaphor category to swap in for the wrong one. Don't
use this if the accurate reframe needs a full sentence to state — that's a sign the
category isn't crisp enough yet.

---

### 3. Named-Comparison / Disambiguation
**Fixed template:** "[Term A] ≠ [Term B] ≠ [Term C, as many as are genuinely conflated —
don't pad to a round number]. / [We / Most people] [need to stop / keep] [conflating them
/ grouping them together]."
**Slot test for the terms:** each must be a real term the audience actually confuses in
practice (check for genuine overlap in usage, not academic hair-splitting nobody does).
**Why it works:** putting the confused terms side-by-side on screen, with the "≠"
literally visible, does the disambiguation work before the reader even reaches line 2 —
it's a diagram compressed into one line of text.
**Real examples:** *"LLM ≠ Generative AI ≠ AI Agents ≠ Agentic AI / We need to stop
grouping them together."* (brijpandeyji, 2,219 likes) · *"Stop calling everything an AI
Agent. / Most people confuse automation with agency."* (lfrodrigues, 2,252 likes)
**Use when:** the concept's core confusion is genuinely terminological (people use
interchangeable words for different things), not conceptual (people understand the words
but not the mechanism — that's template 1 or 6 instead).

---

### 4. Numbered Stack-Map
**Fixed template:** "[The concept/system name], mapped in [N] layers. / [Optional:
★ = the notable variant marker, e.g. open-source options]" or "[The system] ships with
[N] architectural layers most [the audience] never open. / Not [the decoy category].
Layers."
**Slot test for N:** count the actual layers before writing the number — this is the
highest-liked pattern in the dataset precisely because readers verify the count
themselves; an inflated or rounded N breaks trust immediately on inspection.
**Why it works:** stating the exact count up front is a completeness promise (the reader
knows exactly how long the payoff is) and a scannability signal — numbered stacks are the
single most save-worthy shape for a concept because they double as a study reference.
**Real examples:** *"2026 RAG tech stack. / Master these 9 agentic layers to build
applications that actually work."* (genai-works, 4,260 likes — top of the entire
dataset) · *"The 2026 AI stack, mapped in 9 layers. / ★ = open-source option"*
(alexwang2911, 2,054 likes) · *"Claude Code ships with 5 architectural layers most
engineers never open. / Not features. Not settings. Layers."* (brijpandeyji, 3,379
likes)
**Use when:** the concept genuinely decomposes into a fixed, countable set of layers with
real names — not when you're forcing an arbitrary breakdown to hit a "satisfying" number.

---

### 5. Question / Curiosity-Gap
**Fixed template:** "[The concept name]? / [A specific, ordinary moment where the reader
has silently wondered about it]." or a direct bare question: "What is [the concept]?"
**Slot test for the ordinary moment:** must describe a real, common instant (e.g. "when
an AI chatbot outputs text") — not an abstract restatement of the question itself.
**Why it works:** naming the exact moment of latent curiosity (not just asking the
question) makes the reader feel caught mid-thought, which is a stronger hook than the
question alone because it proves the writer has been inside the reader's head.
**Real examples:** *"What is MCP?"* (alexxubyte, 2,159 likes, bare-question variant) ·
*"How LLMs work (minus the heavy math) / Ever wonder what happens under the hood when an
AI chatbot outputs text?"* (addyosmani, 1,906 likes) · *"Three questions decide whether
an AI agent is safe to deploy: Who governs it? What secures it? What proves
compliance?"* (rakeshgohel01, 1,848 likes, multi-question stack variant)
**Use when:** the concept is something readers have definitely wondered about passively
but never looked up — if nobody actually wonders this, the question reads as rhetorical
filler, not a real curiosity gap.

---

### 6. Process-Journey
**Fixed template:** "You [hit / do / trigger] '[the ordinary, familiar action].' /
[a real elapsed time] later you [get / see / receive] [the visible result] — [and then a
reveal that the visible result hides a hidden multi-step pipeline]."
**Slot test for the elapsed time:** must be the genuine real-world latency for the
process being explained, not rounded for rhythm — the credibility of the whole explainer
rests on this number being checkable.
**Why it works:** dropping the reader into the middle of an action they've done
themselves (not narrating from outside) makes the hidden pipeline personally felt rather
than abstractly described — they were just there, a second ago, without knowing.
**Real example:** *"You hit 'Send' on an LLM API call. / ~400 milliseconds later you get
a response."* (brijpandeyji, 2,076 likes)
**Use when:** the concept's real payoff is revealing a multi-step hidden process behind
one familiar, near-instant action. This is currently the only golden-dataset example of
this mechanism — treat it as validated-but-thin; watch whether future rounds confirm it
generalizes before leaning on it heavily.

---

### 7. Contrarian-Reveal
**Fixed template:** "The [magic / power / real driver] of [the system] isn't [the
obvious, most-credited component]. / It isn't [the second most obvious candidate]
either."
**Slot test for the credited-wrong causes:** both rejected candidates must be genuinely
what people commonly credit (check this is a real misattribution, not two strawmen
invented to set up your answer).
**Why it works:** rejecting the two most obvious answers in sequence, before revealing
the real one, builds two full beats of suspense — the reader has already guessed and
been told no twice before the payoff lands, which makes the actual answer feel earned
rather than asserted.
**Real example:** *"The magic of Claude Code isn't Opus. / It isn't Sonnet either."*
(eordax, 1,897 likes)
**Use when:** there are genuinely two commonly-credited-but-wrong answers to reject
before the real mechanism. Like template 6, this is a single validated instance in the
dataset — solid mechanism, thin sample; don't treat it as more proven than it is.

---

### 8. Everyone/Few Split
**Fixed template:** "Everyone talks about [the visible, popular-but-shallow layer of the
topic]. / Very few talk about [the deeper, more consequential layer that actually
matters]."
**Slot test for the "everyone" claim:** the popular layer must be visibly, verifiably
over-discussed relative to the deeper one — check this is true of the actual discourse
(e.g. count what shows up in your own feed/search), not asserted because it makes a good
hook.
**Why it works:** it's a discourse-volume complaint disguised as an insight — the reader
who already senses this asymmetry feels validated, and the reader who hasn't noticed it
gets curious about what they've been missing while everyone else talked about the
shallow layer.
**Real example:** *"Everyone talks about AI models. / Very few talk about AI systems."*
(clarekitching, 2,059 likes)
**Use when:** you can point to a genuine, checkable discourse imbalance. Single
validated instance in the dataset — same caveat as templates 6 and 7.

---

## Explicitly excluded from this bank
Two mechanisms appeared in the Round-0 dataset but are folded into existing templates
above rather than kept separate, since padding to a round number would misrepresent how
many genuinely distinct mechanisms exist:
- **Analogy-lead** ("AI makes more sense when you treat it like a body" — juliadanyal,
  1,982 likes; "AI Systems: A Human Analogy" — adamdanyal, 2,067 likes): this is really
  template 2 (Blunt-Claim) with the reframe category specifically being a sticky bodily
  metaphor. Kept as a Blunt-Claim variant rather than its own template, since the fixed
  structure is identical — only the slot content (the metaphor) differs.
- **Temporal call-out** ("You're still prompt engineering like it's 2024. / AI has moved
  through three eras:" — charlie-hills, 1,430 likes): a single instance, and its fixed
  words ("You're still X like it's [year]") are closer to a dated-callout variant of
  template 1 (Myth-Bust) than a wholly separate mechanism — the "wrong, outdated belief"
  slot is just time-stamped instead of belief-stamped. Not enough independent evidence in
  this dataset to justify a 9th template; revisit if Round 1+ data surfaces more
  instances.

## Verifying a shared-belief slot (never assume it)
Templates 1, 3, and 8 each rely on a "most people believe/do/discuss X" claim. Before
using: confirm the belief is stated-as-given (not merely implied) in 2+ independent real
examples, as done above for template 1 (three posts) — or flag it as unverified
rather than filling the slot on assumption. Templates 6 and 7 are marked above as
single-instance: use them, but don't treat their mechanism as more validated than the
sample supports.

## How to use this bank when drafting
1. Identify the concept's actual shape: a wrong-belief to correct (→ 1, 3), a clean
   category swap (→ 2), a countable layer structure (→ 4), a latent unanswered question
   (→ 5), a hidden process behind a familiar action (→ 6), a misattributed cause (→ 7),
   or a discourse-volume gap (→ 8). Match the template to the concept you actually have.
2. Fill every bracket with something specific and real: a genuine common
   misconception, a real elapsed time, a verified layer count, an actual discourse
   asymmetry. If a slot can't be filled with something real, don't fabricate it — pick a
   different template or flag the gap.
3. Check the "why it works" line. If your draft hook doesn't actually create that
   mechanism, it's not using the template correctly even if it superficially matches.
4. **Run the slot-substitution test before finalizing:** read only the fixed words (skip
   the brackets). Do they form a recognizable rhythm on their own? Confirmed above for
   all 8 templates (e.g. "___ isn't ___. / It's ___." reads as a rhythm alone).
5. **Count the characters.** Line 1 ≤ 62, line 2 ≤ 50, no exceptions.
