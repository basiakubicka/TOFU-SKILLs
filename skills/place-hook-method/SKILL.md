---
name: place-hook-method
description: "Turn a real moment from the user's week into LinkedIn hooks using the PLACE method (Person, Location, Action, Cost, Era) — a found-not-crafted hook system. Two modes: (1) fast mode, run the PLACE prompt directly on a moment the user describes to produce 5 scored hooks; (2) full workflow mode, walk the user through the 6-step process from mining their week to a finished hook (mine moments, pick the highest-emotional-voltage one, tag PLACE, apply lean/fat/lean rhythm, read aloud, ship). Use when the user wants 'PLACE hooks', 'a hook from something that happened to me', asks to run the PLACE method, pastes a moment/story and wants a hook pulled from it, or wants help mining their week for hook material. Hard rules: never invent a missing PLACE element — flag it and ask; every hook needs ≥3 of the 5 elements plus one concrete physical detail; line 1 is 66–110 characters; no 'stop the scroll', no rhetorical-question openers; the hook never resolves the story."
user-invocable: true
---

<!-- writing-style-ref -->
**Writing style:** Apply the `# FOLLOW THIS WRITING STYLE` rules in `<BRAND_DIR>/writing-style.md` to all copy this skill generates (spartan, active voice, short sentences, no em dashes, the banned-word list, etc.). Carve-out: if this skill exists to reproduce a specific named person's voice or your own recorded words, that target voice wins wherever it directly conflicts with those rules.

# PLACE Hook Method — Find the Hook, Don't Write It

## The core idea

A good hook isn't written. It's found. PLACE pulls it out of a moment that already happened:

- **P**erson — who is in this story
- **L**ocation — where it happened
- **A**ction — the main thing that took place
- **C**ost — what went wrong, or what it cost
- **E**ra — when it happened

You don't sit down and craft a clever line. You take something real from the week and interrogate it five ways until the hook falls out. That's also why it can't be copied: two people using the same hook *template* produce the same hook, but two people running PLACE on their own day cannot — the inputs are theirs.

## Two modes — figure out which one the user wants

1. **Fast mode** — the user already has a moment in mind (they paste 3–5 plain sentences describing what happened). Run the 3-step prompt below directly.
2. **Full workflow mode** — the user doesn't have a moment yet, or wants to build the habit. Walk them through the 6-step process, starting with mining their week for candidates.

Ask which one fits if it isn't obvious from what they gave you. If they've pasted a moment, default to fast mode.

---

## Fast mode: the PLACE prompt

### Step 1 — Pull out the PLACE

Read the moment the user described. Extract each element in one line:

- Person: [who]
- Location: [where]
- Action: [main thing that happened]
- Cost: [what went wrong, or what it cost]
- Era: [when]

**If an element isn't in what they told you, write "missing" instead of inventing it.** Never fabricate a detail to fill a gap, even a plausible-sounding one — a made-up cost or location breaks the method's entire premise (it stops being *their* moment). After tagging all five, ask the user directly for whatever came up missing, and wait for their answer before moving to Step 2.

If three or more elements come back missing, say so: the moment isn't sharp enough yet, and ask for a different one (see Step 2 of the full workflow for how to pick a sharper one).

### Step 2 — Write 5 hooks

Once PLACE is filled in (or the user has confirmed they want to proceed with a gap), write 5 hooks. Every hook must pass all of these:

- **Length:** 1 to 2 lines. Line 1 is 66–110 characters.
- **Their words only.** If a phrase isn't in the moment they described, don't add it. No invented dialogue, no invented emotion words they didn't use.
- **≥3 of the 5 PLACE elements** present in the hook, explicitly or implicitly.
- **One concrete physical detail** in every hook — something you could see, hear, or touch in the scene (a ring light, a parking lot, an 11-minute mark). Abstract restatement of the moment doesn't count.
- **Banned:** "stop the scroll", "game-changer", "here's the thing", any rhetorical question as the opener.
- **Don't resolve the story.** The hook creates the pull to keep reading — it doesn't answer its own question or land the lesson. If a hook explains the outcome, cut the explanation and leave the gap open.

### Step 3 — Score each hook

For every hook, list which PLACE elements it uses and name the one doing the most work (the element that's actually creating the pull — usually Cost or Action, but call it out explicitly rather than assuming).

**Output format for fast mode:**

```
PLACE:
Person: ...
Location: ...
Action: ...
Cost: ...
Era: ...

1. [hook line 1]
   [hook line 2, if used]
   Elements used: [P, C, E] · Doing the most work: Cost

2. ...
```

If you asked for missing elements and the user hasn't answered yet, stop after Step 1 and wait — don't guess ahead to Steps 2–3.

---

## Full workflow mode: 6 steps, blank doc to finished hook

Use this when the user has no moment yet, or wants the whole method, not just the prompt.

### Step 1 — Mine the week, not the brain
Have the user list the last 7 days as plain moments: where they were, who they were with, what changed, how they felt. No filtering, no polishing. Push back on any moment that arrives pre-packaged as a lesson or a metaphor — those are the ones the brain already smoothed over. The boring-sounding moments are usually the strongest, because they sound like real life.

### Step 2 — Pick the highest-emotional-voltage moment
From the list, drop the wins and the lessons already told ten times. The right moment is the one the user would hesitate to share at a dinner party — if it makes them flinch, it'll stop a scroll. If three moments feel safe and one feels exposing, the exposing one is the hook.

### Step 3 — Tag PLACE
Run the moment through the same five fields as fast mode Step 1. If three or more elements come back blank, the moment isn't sharp enough — go back to step 2 and pick a different one instead of forcing it.

### Step 4 — Apply lean/fat/lean rhythm
Strong hooks run short-long-short: a punchy line to stop the scroll, a longer one to fill in the scene, then a short one to land it. Read the draft out loud — if three sentences in a row sound the same length and shape, break one.

### Step 5 — Read it aloud
If it trips on the tongue, it trips on the eye. Fix: cut redundant adverbs and qualifiers. Compare "It wasn't my resume. My website looked too corporate." against a version padded with hedges — the clean one always wins.

### Step 6 — Ship the final hook
The finished hook doesn't explain the story — it drops the reader into one face and one tension, with zero context, and trusts them to want the next line.

Run fast mode Steps 2–3 on whatever comes out of Step 3 here, to produce the actual scored hook options.

---

## Common pitfalls and fixes

When reviewing a user's draft hook (in either mode), check for these five failure modes:

1. **Names the lesson before the moment.** Fix: cut the lesson, drop the reader into the scene with zero context.
2. **Sanitizes the cost.** Fix: name the real stakes — a dollar figure beats "a lot," "I cried in the bathroom" beats "I felt overwhelmed."
3. **Blurs the location.** Fix: pick one specific room or spot, not "at work" — the desk, the corner of the conference room, the parking lot at 7am with the engine still running.
4. **Hides the era.** Fix: anchor a real timestamp — "Tuesday morning" beats "recently," "my 36th birthday" beats "a while back."
5. **Writes about people in general instead of one person.** Fix: name a single human — one client, one friend, one version of themselves from one moment. A crowd is forgettable. A face is felt.

If a hook the user shares trips one of these, name which one and give the specific fix, not a generic "make it more specific" note.

---

## The 7-day PLACE practice loop

Offer this if the user wants to build the habit rather than get a one-off hook:

- Day 1: list 10 moments from the last 7 days.
- Day 2: tag 3 of them with PLACE.
- Day 3: write 2–3 hooks, score each.
- Day 4: pick the highest scorer, build the post around it.
- Day 5: publish.
- Day 6: track which hook pulled the most reach, look for a pattern.
- Day 7: repeat with a new batch of moments.

Run it for four weeks. The tagging becomes automatic well before that — the point of the loop is to make PLACE something the user does in real time, not a worksheet.

---

## Reference: what a strong PLACE hook looks like

Moment: a leadership coach with 15 years of experience almost didn't book a call because the user's website looked too corporate, discovered 11 minutes into a Monday Zoom call, costing an unknown number of leads over time.

- Person: the client (leadership coach, 15 years' experience)
- Location: a Zoom call, her face half-lit by a ring light
- Action: she said she almost didn't book because the site looked "too corporate"
- Cost: months of leads lost to a homepage that looked polished
- Era: this Monday, 11 minutes into the call

Hook: "A leadership coach with 15 years of experience almost didn't hire me. It wasn't my resume. My website looked too corporate."

Three sentences, one face, one tension, no resolution. That's the shape every output from this skill should hit.
