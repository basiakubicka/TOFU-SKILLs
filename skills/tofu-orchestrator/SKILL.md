---
name: tofu-orchestrator
description: "Entry point for ANY TOFU (reach) LinkedIn post: given a topic, an idea, a news item, or just 'write me a TOFU post about X', diagnoses which of the 8 dedicated TOFU archetype skills actually fits the substance (Contrarian, Explainer, How-To, Resource Roundup, News Breakdown, Surprising Number, Relatable Mirror, Meme), and routes to it. If more than one angle genuinely fits the same topic, presents 2-3 real angle options with a one-line reason each and asks which to run, rather than silently picking one. Does NOT draft posts itself. Use whenever you give a topic without naming a specific archetype/skill, or asks 'what angle should I take on X' / 'what TOFU post should I write about X.'"
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** This skill is a router — it doesn't generate post copy itself, so
the writing-style rules don't apply to its own output directly. They apply once it
hands off to a specific archetype skill, which carries its own writing-style-ref.

# TOFU Orchestrator

This is the **entry point** for any TOFU (reach) post request that doesn't already name
a specific archetype. Its only job: read the topic, figure out which real archetype(s)
fit, and route to the right dedicated skill — or present the 2-3 that genuinely fit and
let you pick.

**Never draft the post yourself.** Once the archetype is chosen (by you),
hand off to that skill and let it run its own classification check, its own
hook-template-bank, and its own output format. This skill's output is a routing
decision, not a post.

---

## The 8 archetypes it routes to

| Archetype | Skill | Fires when the topic... |
|---|---|---|
| Contrarian myth-bust | `tofu-contrarian` | asserts a specific, common belief is wrong |
| Conceptual explainer | `tofu-explainer` | is a concept people name-drop but don't understand, decomposable into one sticky metaphor + N layers |
| Tactical how-to / system | `tofu-howto` | is a concrete, numbered, runnable setup with real settings/paths/prices |
| Resource roundup | `tofu-resource-list` | the payload is a multi-item list of real, free, linkable resources |
| News / launch breakdown (third-party) | `tofu-news-breakdown` | a real, named, external person/company just did/said something, distilled into lessons |
| Surprising number / stat-shock | `tofu-surprising-number` | one specific, checkable, counterintuitive number is the whole hook |
| Relatable mirror | `tofu-relatable-mirror` | a universal feeling/belief/identity moment, reflected back so the reader feels seen |
| Meme | `tofu-meme` | there's a real image/graphic and the point rides on it, not on prose |

Out of scope for this TOFU pack (flag it, don't force-fit):
- **Your own news / milestone / build announcement** — you announcing your OWN
  milestone is a MOFU (trust) post, not TOFU. Say so plainly rather than forcing it
  into a TOFU archetype.
- **A real personal-arc / cost / turning-point story** — if the topic has a real personal-arc/cost/turning-point
  shape (not a universal point for strangers), it's MOFU. Flag this rather than force-fit.

---

## Step 1 — Ask what's missing, don't guess

If you give a topic with no other context, you usually have enough to route. Only
ask a clarifying question when the routing genuinely depends on a fact you don't have:
- Is there a real image/graphic involved? (needed to rule Meme in or out)
- Is this about something you yourself did, or something external? (TOFU vs MOFU)
- Do you have a real, checkable number/source, or is this a general observation?

Don't turn this into an interview. One quick question only if it changes the routing outcome.

## Step 2 — Run the diagnostic in order

This mirrors the decision-signal order already established in
[`references/tofu-pattern-analysis.md`](./references/tofu-pattern-analysis.md) and echoed in every
archetype skill's own "Classification" section (read the live one if in doubt — this
list is a summary, not a replacement).

1. **Is there a real image/graphic that carries the joke or point, with text as
   secondary caption?** → Meme (`tofu-meme`). If no real image exists, this
   archetype is off the table regardless of how short/punchy the text is.
2. **Is the payload multiple external links/resources (a free course list, a set of
   repos, a roundup)?** → Resource Roundup (`tofu-resource-list`). (A SINGLE named
   resource is a different, not-yet-built skill; treat it as Resource Roundup's
   single-item edge case for now and flag it.)
3. **Does a real, named, external person/company/event anchor the whole post, distilled
   into lessons you extracted?** → News Breakdown (`tofu-news-breakdown`). If
   you yourself are the news, redirect to MOFU instead (see above).
4. **Is there ONE specific, checkable, counterintuitive number and the body explains
   it?** → Surprising Number (`tofu-surprising-number`). Don't confuse with a
   *count of steps* (How-To) or a *count of layers* (Explainer) — the number itself
   must be the shock, not a container for something else.
5. **Does the post assert a specific, common belief is WRONG and prove it?** →
   Contrarian (`tofu-contrarian`). The prosecutorial register (versus empathy) is
   the tell versus Relatable Mirror.
6. **Is there one sticky metaphor that organizes N distinct layers/parts, each with its
   own job and limit, teaching a concept?** → Explainer (`tofu-explainer`).
7. **Are there numbered steps a reader could execute right now with real settings,
   paths, prices, click-paths?** → How-To (`tofu-howto`). If the "steps" are
   really links, it's Resource Roundup instead; if they're really concept-parts, it's
   Explainer instead.
8. **Does the topic reflect a universal feeling/belief/identity moment back at the
   reader so they feel seen, then reframe it from limitation to possibility?** →
   Relatable Mirror (`tofu-relatable-mirror`). The empathize-then-reframe register
   (versus prosecute) is the tell versus Contrarian.

If NONE of these fit cleanly, stop and say so rather than force the topic into the
nearest archetype. A topic with a real personal cost/turning-point arc is MOFU, not
TOFU — say that plainly and note it's a MOFU (trust) post, out of scope for this TOFU pack.

## Step 3 — If more than one archetype genuinely fits, present the options

Many real topics support 2-3 valid angles. Don't silently pick one. Present each viable
option as:

```
This topic could work as:

1. [Archetype name] — [one-line reason this angle fits, referencing the actual
   substance of the topic, not a generic description of the archetype]
2. [Archetype name] — [one-line reason]
3. [Archetype name] — [one-line reason, if a third genuinely fits]

Which angle do you want to run?
```

Example: "Claude just shipped 4 layers (Chat/Cowork/Skills/Code)" could be:
- **News Breakdown** — if the news IS that Anthropic shipped it (their announcement,
  their event).
- **Explainer** — if the point is teaching a stranger what the 4 layers ARE and how they
  relate (a sticky metaphor + decomposition), independent of it being news.
- **How-To** — if the point is a runnable setup ("do X in each layer this weekend"),
  not teaching the concept or reporting the news.

Same raw material, three different jobs. Naming the real distinction (not a vague
"it depends") is the whole value of this step.

## Step 4 — Route, don't draft

Once an archetype is chosen (by clear single fit, or by your pick from Step 3),
hand off explicitly: name the skill, and let IT run its own classification check
(some topics that look like a fit on the surface get rejected once the target skill's
own harder classification test runs) and its own drafting procedure. If the target
skill's own classification test disagrees with your routing (e.g. it flags the topic
as contamination for a different archetype), trust the target skill and re-route
rather than forcing it through.

---

## What NOT to do
- ❌ Drafting a post yourself instead of routing. This skill routes; it doesn't write.
- ❌ Silently picking one archetype when 2+ genuinely fit — surface the real options.
- ❌ Forcing a MOFU-shaped topic (personal arc, cost, turning point) into a TOFU
  archetype because it's what was asked for. Say plainly when the topic isn't TOFU.
- ❌ Guessing whether a real image exists for Meme, or whether a number is truly
  checkable for Surprising Number — ask if it's a routing-critical unknown.
- ❌ Re-deriving classification logic from scratch. Each archetype skill already has a
  rigorous, tested Classification section — defer to it, don't reinvent it here.

## Output format

```
### Diagnosis
[The topic, restated in one line, to confirm you understood it]

### Best-fit archetype(s)
[One clear fit -> name it and route immediately]
[or, 2-3 genuine fits -> the numbered options from Step 3, with real reasons]

### Routing
Handing off to `[skill name]` to draft.
```
