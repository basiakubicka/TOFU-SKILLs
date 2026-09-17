# Meme Caption Template Bank

Caption/framing patterns extracted from the golden dataset (13 real, high-performing meme
posts in a golden set of real high-performing posts + `holdout.json`; 6
pure, 7 elevated; pulled from a set of real high-performing meme posts).
This bank is a reference for **caption-brevity and framing patterns**, NOT text to copy
verbatim. In this archetype the IMAGE carries the joke; every template below is only the
minimal text that frames it.

**Honesty note on dataset size.** 13 posts, heavily single-author per mechanism
(pascalbornet 4, linasbeliunas 2, eordax 2). Only **5 caption mechanisms** have genuine
fixed, repeatable wording; of those, **2 recur across 2+ independent examples** and the
other 3 appear once but have clear fixed connective tissue worth locking down. The count is
not padded to a round number. The PURE near-zero style is deliberately NOT forced into a
fixed-word template (see "PURE-bucket discipline" below) because its whole point is having
almost no text to templatize. Single-appearance one-offs are listed under "Excluded."

**Format rule for every slot:** the bracket itself carries the specific description, never a
generic label like `[X]`. A drafter must be able to fill the slot correctly from the bracket
text alone. Every template was run through the **strip-the-slots self-test**: read only the
fixed words (skip the brackets) and they must form a recognizable, repeatable rhythm on their
own. Templates that failed that test were demoted to "discipline" or "excluded," not shipped.

**The mechanism underneath the whole archetype:** the caption never explains the joke. It
either (a) says almost nothing and lets the image land, or (b) adds ONE turn the image sets
up (a reframe, a named phenomenon, a euphemism, a number). A caption that narrates the image
or writes the punchline has already failed, regardless of which template it fits.

---

### 1. Absurd Re-Elevation — "That's not [X]. That's [Y]."
**Fixed template:** "That's not [the mundane, literal thing the image actually shows] anymore. That's [the absurdly grander institution/role it is jokingly promoted to, loaded with 2-3 concrete grown-up attributes]."
**Two-line variant:** "It is no longer [the humble tool the image shows]. It is [the inflated identity], [with the deadpan cost/consequence that makes the inflation land]."
**Slot test for [Y]:** the reframe must ELEVATE the subject into a category it obviously
doesn't belong to (a vending machine → a startup; an assistant → a life coach), and the
absurdity must come from concrete grown-up attributes, not an adjective. "That's basically a
startup" fails (vague). "That's a seed-stage startup with margins, emotional attachment, and
mild regulatory risk" passes (three concrete attributes carry the joke). Never explain why
it's funny after the reframe; the reframe IS the payoff, end the caption there.
**Why it works:** the image shows something small and dumb; the caption straight-facedly
promotes it to something self-important. The gap between the literal image and the grand
label is the laugh, and the reader completes it themselves, which is exactly the "that's so
real" reaction this archetype is judged on.
**Real examples (cross-author, cross-bucket):**
- *"That's not a vending machine anymore. That's a seed-stage startup with margins, emotional attachment, and mild regulatory risk."* (linasbeliunas, 1,214 likes, **pure**)
- *"At that point, it is no longer an assistant. It is a life coach with server costs."* (pascalbornet, 3,313 likes, **elevated**)
**Use when:** the image shows an ordinary object/tool behaving like it has ambitions. This is
the strongest template in the bank (only one that recurs across two authors AND both buckets).
**Non-negotiable (anti-AI budget):** "That's not X. That's Y." IS the binary-flip structural
move that `anti-ai-pass` budgets to ONE per post. Use it as the closer OR another
structural move, never both, and only when the two-three concrete attributes are real. A flip
with a generic Y ("that's the future") is the exact AI tell the budget exists to catch.

---

### 2. Named-Phenomenon Thesis — "the most accurate [illustration] of [phenomenon] I've seen"
**Fixed template:** "This might be the most accurate [illustration / example / thing] [of / about] [the named, nameable phenomenon the image satirizes: "AI hallucination," not "AI being weird"] I've seen [in a while]."
**Slot test for [phenomenon]:** it must be a thing with an actual name the audience already
argues about (AI hallucination, vendor lock-in, agent hype), stated in 2-4 words. If the best
you can do is a description ("when AI gets confidently wrong"), name it first ("AI
hallucination") or pick a different template. Do NOT follow this line by explaining the
phenomenon; the image does that.
**Why it works:** it frames the meme as evidence, not a joke. Calling the image "the most
accurate illustration of X" invites the reader to agree it nails a shared frustration, which
converts recognition into a like. The superlative ("most accurate") is a claim the image has
to back up, so it only works when the image genuinely lands the phenomenon.
**Real examples:**
- *"This might be the most accurate illustration of AI hallucination I've seen in a while."* (pascalbornet, 3,386 likes, **elevated**)
- *"This meme has been updated. It is the most accurate thing I've seen about AI."* (a real example, elevated sub-variant)
**Use when:** the image is a sharp visual metaphor for one named, debated phenomenon. Pairs
naturally with a tight 3-item riff underneath (elevated shape).
**Verification note (shared-belief slot):** if your elevated riff then claims the phenomenon
is universal ("everyone has seen this"), that consensus is a claim — confirm the phenomenon
is genuinely in circulation (it appears stated-as-given in the hallucination and vendor-hype
posts here) rather than assuming it. Never invent a statistic to prop up the superlative.

---

### 3. Corporate-Euphemism Relabel — "This is what [role] calls [flattering jargon]."
**Fixed template:** "This is what [the specific role or function that would spin it: IT, senior management, the vendor] calls [the flattering corporate euphemism the chaotic image obviously contradicts: "seamless integration," "digital transformation"]."
**Stacked variant (as used in the source):** "This is what [role A] calls [euphemism A]. And what [role B] proudly calls [euphemism B]."
**Slot test for the euphemism:** it must be real boardroom vocabulary the audience has heard
used sincerely, applied to an image that visibly makes a mockery of it (a fire-hazard outlet
labeled "seamless integration"). If the euphemism isn't one people actually say with a
straight face, the irony has nothing to bite. Keep the euphemism verbatim-corporate; do not
soften it into plain English or the contrast dies.
**Why it works:** the caption speaks in the exact language of the people the image mocks. The
reader supplies the eye-roll because they've sat in the meeting where someone called that
mess "digital transformation." The straight-faced delivery is the whole joke; an added "lol
so true" would kill it.
**Real example:** *"This is what IT calls seamless integration. And what senior management
proudly calls digital transformation."* (pascalbornet, 1,465 likes, **elevated**)
**Single-source flag:** this appears in ONE post (twice internally), not across authors.
Treat it as a real but less-proven pattern than templates 1-2. It is included because the
fixed wording is clear and the mechanism is reusable, but its performance rests on a single
data point.
**Use when:** the image is operational chaos (a mess, a hazard, an overload) that some role
would proudly rebrand.

---

### 4. "Funny because it's true" + Critical-Dependency List
**Fixed template:** "Funny because it's true. [You only need N things to [the concrete outcome the list enables: "ship great products"]:] → [dependency] → [dependency] → [dependency]. [Miss one and [the mild consequence]. Miss [the load-bearing one] and [the fatal consequence].]"
**Slot test for the list:** each item must be a genuine, nameable dependency (Coffee, Claude
Code, a good salary), 1-3 words, and one of them must be the load-bearing one the joke turns
on. Max 3-5 items. If the items are abstract ("focus," "discipline"), the list reads as
advice, not a meme; pull concrete nouns instead. Do not explain each item; the image already
shows what happens when you remove it.
**Why it works:** "Funny because it's true" pre-frames the image as recognition humor and
gives the reader permission to laugh before they scroll to the list. The list then does the
minimum elevated-meme job (thesis + tight items) without drifting into an explainer. The
"miss one / miss THE one" turn adds a stakes beat in five words.
**Real example:** *"Funny because it's true. You only need 3 things to ship great products:
Coffee ☕ / Claude Code 🤖 / A good salary 💵 / Miss one and things get complicated. Miss Claude
Code and your product might never see the light."* (eordax, 1,408 likes, **elevated**)
**Single-source flag:** appears once, but it is the cleanest example of the generic ELEVATED
skeleton (one-line thesis + tight arrow/bullet list + one consequence line), so it doubles as
the default elevated template when no sharper mechanism (1-3) fits.
**Use when:** the image is a multi-panel "what happens if you remove X" comic or any
image that enumerates ingredients/dependencies.

---

### 5. Economics Reality-Check Deflation — "[$big] vs [$small]. Wild how that math works out."
**Fixed template:** "[the eye-watering real cost the hype incurs: "$150K/month in tokens"] vs [the mundane cheaper alternative it forgot: "$4.5K for Rohan"]. Wild how that math works out."
**Optional setup line (from source):** "This is what happens when you [swallow the [named hype] / skip the [unglamorous homework]]."
**Slot test for the two figures:** both numbers must be real or defensibly realistic and
directly comparable (same period, same job). The joke is the ratio, so a fabricated or
apples-to-oranges pair breaks it. If you don't have two real comparable figures, don't invent
them — use a different template. "Wild how that math works out" must stay deadpan; no "😂"
stacked on top of a number that's already funny.
**Why it works:** the caption does arithmetic the hype skipped. Two numbers side by side, no
adjective, let the reader feel the absurdity of the ratio. The flat closer ("wild how that
math works out") is understatement doing the work an exclamation would ruin.
**Real example:** *"$150K/month in tokens vs $4.5K for Rohan. Wild how that math works out.
Welcome back to the team, Rohan 🫡"* (eordax, 6,197 likes, **pure** — the highest-liked post
in the golden set)
**Verification note (shared-belief slot):** the optional setup leans on a circulating belief
("AI is replacing developers"). That belief is stated-as-given in this post and underlies the
SWE-before/after post, so it's in genuine circulation here — but confirm it's a live claim in
the audience before riding it, and never fabricate the hype quote.
**Use when:** the image is a cost/ROI joke (a bill, a whiteboard of numbers, a before/after
budget).

---

## PURE-bucket discipline (a rule, not a fixed-word template)
The near-zero pure captions in the dataset — *"Software engineers before vs. after agents"
:)* (addyosmani, 2,571, pure) and *"Why spend money on ChatGPT or Claude? Chipotle's support
bot is free 😂"* (sytaylor, 4,695, pure) — share a MECHANISM but no fixed words, so they fail
the strip-the-slots self-test and are deliberately NOT templatized. The reusable rule instead:
- **One flat line, 0-40 characters ideal.** Either quote the image's own on-screen label, or
  ask the plain value-question the image answers. Nothing else.
- **At most one tell**, and only if the image isn't already doing it: a single `:)` or one
  emoji, never a `😂😂😂` wall (an emoji wall is the caption doing work the image should do).
- **No list, no CTA, no engagement question, no reframe paragraph.** Adding any of these turns
  a pure meme into a weaker elevated one.
Trying to lock fixed words here would fight the format. The discipline IS the template.

---

## Excluded (single-appearance one-offs, not templatized)
Left out rather than padded in, per the honesty rule:
- **In-character retro-nostalgia story** (*"I still remember back in 1998 when I was one of the
  first users of ChatGPT..."*, ralph, 1,780, pure). A committed bit tied to one specific
  retro-parody image; no fixed reusable connective tissue, and it risks over-writing the
  caption (long for a pure meme).
- **Call-and-response chant transcription** (adamdanyal CEO chant, 4,505, elevated). Only works
  when the image itself is a protest-chant format; it transcribes the image, which is close to
  the "don't narrate the image" failure. Not reusable across image types.
- **"Give it a year" escalating speculation** (stuart-winter-tear Samsung fridge, 1,624, pure).
  A dry riff that extrapolates the image forward; entertaining but a bespoke monologue with no
  repeatable skeleton, and runs long for pure.
- **Count-reveal** (*"Someone counted... there are 78 of them"*, linasbeliunas Copilot, 1,726,
  elevated). One appearance; overlaps with template 2's thesis role without adding a distinct
  fixed structure.

---

## How to use this bank when drafting
1. **Pick the bucket first.** No structural mechanism to add and the image fully lands on its
   own → PURE discipline (near-zero, one line). The image needs one framing turn → an ELEVATED
   template (1-5).
2. **Match the template to what the image actually is:** an ordinary tool acting important →
   1; a visual metaphor for one named phenomenon → 2; operational chaos a role would rebrand →
   3; an enumerate-the-ingredients comic → 4; a cost/ROI joke → 5.
3. **Fill every bracket with something specific and real** — a real number, a named
   phenomenon, real corporate jargon. If a slot needs a real figure, quote, or common belief
   you can't verify, do NOT fabricate it: pick a different template or ask for the
   specific. (Verification order for a belief slot: appears stated-as-given in 2+ real examples
   → engagement evidence someone holds it → otherwise flag it, don't assume.)
4. **Check the "why it works" line.** If your draft doesn't actually create that mechanism
   (the elevation gap, the evidence framing, the deadpan ratio), it's not using the template
   even if it looks similar.
5. **Run the strip-the-slots self-test:** read only the fixed words. If they don't form the
   template's recognizable rhythm, or a bracket is still generic, fix it before finalizing.
6. **Respect the anti-AI budget:** at most ONE structural move (template 1's "That's not X.
   That's Y." counts) per post, and never write the laugh out loud on top of an already-funny
   image. Run the caption through `anti-ai-pass/scripts/lint.py --stdin` before shipping.
7. **Length gate:** pure 0-40 chars ideal; elevated 150-500 chars. Shorter is correct here.
