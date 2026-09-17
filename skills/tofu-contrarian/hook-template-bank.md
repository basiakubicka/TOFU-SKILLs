# Contrarian Hook Template Bank

18 hook templates extracted from the golden dataset (23 real, high-performing contrarian
posts). Each is a **distinct rhetorical mechanism** with **fixed, literal words** locking
the rhythm in place — not a vibe description or a reskin of the same sentence. Pick the
template that fits the belief you're correcting — don't default to template 1 just
because it's first.

**Format rule for every slot:** the bracket itself must carry the specific description —
never a generic label like `[SLOT A]`. Write `[the shiny, trend-having outcome people are
chasing]`, not `[SLOT A]` with the description in a separate paragraph below. A drafter
should be able to fill the slot correctly from the bracket text alone, without needing to
cross-reference anything else.

Every template has:
- **Fixed template** — the literal words, verbatim, with descriptive `[bracketed]` slots
  inline. Read the fixed words alone (skip the brackets) and they must form a
  recognizable, repeatable rhythm on their own.
- **Slot test** — for slots needing more than the bracket can hold, a concrete pass/fail
  check (not additional vague description — a real test you can apply).
- **Why it works** — the psychological/rhetorical mechanism, secondary to the fixed words.
- **Real example** — the actual post the template was extracted from.
- **Use when / non-negotiables** — situational fit, plus any hard safety rule.

---

### 1. Ambition vs. Unglamorous Prerequisite
**Fixed template:** "Everyone wants [the shiny, trend-having, status outcome people are chasing]. / Almost nobody wants [the concrete, assignable task that outcome depends on — one that's boring, time-consuming, or unglamorous enough that people genuinely avoid it, not just a neutral to-do item]."
**Slot test for the prerequisite:** two checks, both must pass. (1) Assignability: could you put it on an employee's Monday-morning to-do list? "The work that produces it" fails (too abstract) — "clean the data before the launch" passes. (2) Genuine avoidance: is this a task people would actually rather skip — slow, tedious, unrewarding in the moment — not just any task that happens to precede the outcome? A quick, easy prerequisite fails this template even if it's concrete, because the whole tension depends on it being something people are avoiding, not just something they haven't gotten to yet.
**Verification for the outcome:** confirm it's a real, commonly-repeated phrase people actually say (see "Finding what most people actually think," below) — don't invent a trend word.
**Why it works:** everyone recognizes wanting the outcome; almost no one has done the prerequisite. The gap between the two is the whole post.
**Real example:** *"Everyone wants AI ROI. Almost nobody wants the work that produces it."*

---

### 2. Flat Denial + Reframe
**Fixed template:** "Most people think [a specific, falsifiable claim about HOW something works, in the exact words a real person would say it]. / It's not."
**Slot test:** the claim must be precise enough to fail a fact-check ("Claude Code is about writing better prompts") — not a vague vibe ("AI tools require good input").
**Mandatory pre-check — do not skip:** verify the belief is real before writing this hook:
  1. **Golden-dataset cross-check** — does this belief (or a close paraphrase) appear stated as assumed-true in 2+ other real posts?
  2. **Comments evidence** — has someone said this unprompted in comments on a related post?
  3. **If neither:** don't publish as-is — flag it: "I believe this is common but haven't verified it — use anyway, or pick a different template?"
**Line 2 must be the literal opposite direction of the claim**, not a hedge ("it's more complicated than that" fails — it needs "it's not").
**Why it works:** a flat denial with zero justification creates maximum tension — the reader needs the proof to resolve the "wait, why not?" reaction.
**Real example:** *"Most people think using Claude Code is about writing better prompts. It's not."*

---

### 3. Authority Bombshell + Quote
**Fixed template:** "[The person's real, independently-verifiable title/credential], just [a short verb phrase for the surprising act, e.g. "dropped a bombshell"]: / '[an exact, word-for-word quote]'"
**Slot test for the quote:** copy-pasted, never paraphrased or invented. If you don't have the exact quote, this template cannot be used — pick another.
**Why it works:** borrowed authority plus a surprising admission from an insider is inherently more credible than an outsider's opinion.
**Real example:** *"Pioneer of modern AI just dropped a bombshell: 'I'm not interested in LLMs anymore.'"* (real Yann LeCun quote)
**Non-negotiable:** if the quote can't be sourced to something real and checkable, do not use this template — pick another.

---

### 4. Cheap Fix vs. Real Work (Sarcastic Negation)
**Fixed template:** "[The specific, named tool/product people reach for BECAUSE it feels like the low-effort shortcut] won't [fix the real, underlying structural problem it can't actually touch]. / It will just [make that same underlying problem worse, faster, or bigger]."
**Slot test for the shortcut:** name the actual tool being pitched as the easy button ("AI," "the new CRM") — not a vague category. It only works if people are genuinely choosing it specifically to avoid doing real work.
**Slot test for the acceleration:** must describe the SAME failure named in the "underlying problem" slot, just faster/bigger — not a new, unrelated problem. The sarcasm is that the "fix" amplifies the exact thing it was supposed to solve.
**Why it works:** people expect "it won't work" (a null result); "it'll make it worse" is a sharper, higher-stakes claim that demands the mechanism be explained.
**Real example:** *"AI won't fix bad data. It will just make the mess faster."* — AI is the shortcut everyone wants to skip to; bad data is the real unglamorous problem; "faster mess" is the ironic acceleration of that exact same failure.

---

### 5. Blunt Rejection + Reversal
**Fixed template:** "Everyone says [a specific, repeated doom/hype prediction naming what's claimed and to whom]. / It's [one unhedged rejection word — "bullshit," "wrong," "backwards"]. / [The literal, direction-reversed claim, stated as fact]."
**Slot test for the reversal:** must be the literal opposite direction, not a nuance — if the prediction says "X is dying," this must say "X is growing," never "X is changing in complex ways."
**Verification for the prediction:** same 3-step check as template 2 — confirm it's actually repeated, don't assume.
**Why it works:** the bluntness signals confidence and creates a visible fight — readers who hold the popular belief want to see it defended or refuted.
**Real example:** *"Everyone out there saying AI will kill SaaS and software engineering with it. It's bullshit. The opposite is happening."*

---

### 6. Versus Framing
**Fixed template:** "[A real, named strategic approach organizations are actively choosing] Vs [a second real, named strategic approach they're choosing instead]"
**Slot test:** could you find real companies publicly committing to each side? Both sides must be actual choices people are making right now, not abstract values ("speed vs. quality") and not a strawman nobody actually picks.
**Why it works:** framing it as a binary choice forces the reader to mentally place themselves on a side before reading further — instant self-relevance. No line 2 needed; the title alone does the work.
**Real example:** *"AI First Vs Data First"*
**Use when:** the post's real content is a comparison/tradeoff between two named strategic approaches, not a single myth-bust.

---

### 7. Named Discomfort
**Fixed template:** "Uncomfortable truth most don't want to hear: / [a specific, falsifiable claim that threatens a belief people have real money, time, or identity invested in defending]."
**Slot test:** would naming this claim make someone in the audience visibly uncomfortable, not just mildly disagree? If the claim is something most readers have zero stake in, the "uncomfortable" framing rings false — use template 2 instead.
**Why it works:** pre-labeling the claim as uncomfortable primes the reader to expect resistance in themselves, which paradoxically makes them want to read on to see if they'll actually feel that resistance.
**Real example:** *"Uncomfortable truth most don't want to hear: Building AI agents won't lead to results."*

---

### 8. Delayed Consequence
**Fixed template:** "Everyone says [a specific, repeated prediction naming exactly what's claimed and to whom]. / Then [one concrete, near-term, single-scene event where reality intrudes]."
**Slot test for the reality-check moment:** can you draw it as a single scene? "Then reality sets in" fails (too abstract). "Then they see the API bill" passes — a specific document, a specific moment, a specific reaction.
**Verification for the prediction:** same 3-step check as template 2.
**Why it works:** the two-step structure (claim, then reality-check) mirrors how the reader will actually experience being wrong — creates anticipatory dread about the specific moment.
**Real example:** *"Everyone says AI is replacing developers. Then they see the API bill."*

---

### 9. Faux-Quote / Reality Contrast
**Fixed template:** "Every [a specific, nameable actor category, e.g. "software company"] in [the current year or a named recent period]: / '[a cliché line phrased EXACTLY like real marketing/press-release language — screenshot-able, not softened]' / What they actually did: / [one short, concrete, almost-funny sentence naming what was really built]."
**Slot test for the deflating reality:** must be specific enough to picture — not "they didn't really change anything" but "slapped a chatbot on a broken product."
**Why it works:** mimicking the exact cliché phrasing readers have seen a hundred times creates instant recognition ("oh my god, yes, everyone says that") before undercutting it with a concrete, almost-absurd reality.
**Real example:** *"Every software company in 2026: 'We've added AI Agents!' What they actually did: Slapped a chatbot on a broken product."*

---

### 10. Category Correction
**Fixed template:** "Most [a plural noun phrase naming the visible, mislabeled thing, e.g. "AI failures"] are [the accurate underlying category/cause], not [the category people default to blaming]."
**Slot test:** are the true category and the assumed category answers to two genuinely different diagnostic questions (architecture vs. model), or just two intensities of the same answer ("a bit broken" vs. "very broken")? If the latter, this isn't a category error — this template fails, pick another.
**Why it works:** miscategorization claims are inherently debatable — readers will want to test the claim against their own example, and a genuine category swap forces them one layer deeper than their default explanation.
**Real example:** *"Most AI failures are architecture failures, not model failures."*

---

### 11. Insider Credential + Direct Claim
**Fixed template:** "I'm [a real, specific, independently-verifiable past role or status the poster genuinely held, e.g. "ex-LinkedIn"]. / [A direct claim naming the real cause, that only someone with this exact vantage point could credibly make]."
**Slot test for the claim:** would an outsider without the credential be able to make this exact claim credibly? If yes, the credential isn't doing real work — reconsider the template.
**Why it works:** first-person insider claims read as leaked information rather than opinion, raising perceived credibility instantly — but only if the credential is real and the claim genuinely requires that vantage point.
**Real example:** *"I'm ex-LinkedIn, and this is the reason why your impressions have plummeted."*
**Non-negotiable:** if the poster does not actually hold the stated credential, never use this template under any circumstance — pick a different one. Never invent or round up a credential to make it fit.

---

### 12. Unpopular Opinion Flag
**Fixed template:** "Unpopular opinion: [one complete, specific, falsifiable claim the poster genuinely expects visible pushback on]."
**Slot test:** would a meaningful share of the audience actually disagree out loud? If everyone secretly already agrees, "unpopular" is false advertising and undercuts the hook's own premise — verify per "Finding what most people actually think," below, before using.
**Why it works:** flagging "unpopular" is a dare — it invites disagreement explicitly, which is exactly what drives the comment-based metric this archetype is judged on.
**Real example:** *"Unpopular opinion: most of the people confidently saying 'AI will replace all devs' ... have never worked inside enterprise IT."*

---

### 12b. Rush vs. Neglect + Stakes
**Fixed template:** "Everyone's rushing to [a specific, visibly-trending activity with real momentum, e.g. "build AI agents"]. / Almost nobody is [the specific safeguard/discipline that activity requires, skipped BECAUSE everyone's focused on the speed of the rush]. / That's [one short stakes word/phrase proportionate to a real, describable risk — "terrifying," "a blast radius"]."
**Slot test for the neglect:** must be causally downstream of the rush (the neglect only matters because of the rush) — not an unrelated criticism bolted on. Test: does slowing down the rush directly fix the neglect? If not, the causal link is missing and this template won't land.
**Why it works:** three-beat structure (activity, gap, consequence) escalates tension across three short lines instead of resolving it in two — reads slower, hits harder.
**Real example:** *"Everyone's rushing to build AI agents. Almost nobody is securing them. That's terrifying."*

---

### 13. Imperative Stop + Reason
**Fixed template:** "Stop [a specific, currently-widespread industry PRACTICE that most practitioners privately wish were different]. / [One fact-based consequence that follows directly from that practice]."
**Slot test for the practice:** would multiple people in the industry, asked privately, agree "yeah, that's kind of broken, but everyone does it"? If it's a one-off personal habit rather than a systemic, widely-participated-in norm, this template reads flat — use template 2 or 5 instead.
**Slot test for the reason:** must be concrete enough to argue with (a specific harm, a specific missed opportunity) — not "...and it's bad for everyone."
**Why it works:** naming a norm everyone quietly resents, and telling the reader to stop participating in it, gives permission to break from a shared, disliked convention — it only lands if the norm is genuinely industry-wide, not personal.
**Real example:** *"Stop hiring based on years of experience."* — a widespread hiring practice many hiring managers privately doubt, not a fringe habit.

---

### 14. Should/Shouldn't Contrast
**Fixed template:** "[A single word/label with one real, commonly-understood definition, e.g. "entry-level"] should mean [that same word repeated]. / Not [the specific, concrete way it's actually being used that violates its own definition]."
**Slot test for the exploited reality:** must be specific enough to fact-check — a number, a requirement, a named practice ("3-5 years of unpaid experience"), not "a watered-down version."
**Why it works:** appeals to definitional integrity feel objective/factual rather than opinion-based, lowering the reader's guard before the argument lands.
**Real example:** *"Entry-level should mean entry-level. Not 3-5 years of unpaid experience."*

---

### 15. Expected vs. Actual Path
**Fixed template:** "The fastest way to [a specific, desirable outcome readers are actively pursuing this quarter] is not [the specific action/method a meaningful share of the audience currently believes is the path there]. / It is [the actual, less-obvious method, concrete enough to act on immediately]."
**Slot test for the expected route:** must be something people are genuinely doing, not a strawman nobody really tries — verify it's real, don't assume.
**Why it works:** readers actively pursuing the expected route feel direct, personal stakes — this isn't abstract, it's "you're doing this wrong right now."
**Real example:** *"The fastest way to find your AI edge is not to learn another tool. It is to improve one workflow you already understand."*

---

### 16. Insider Tell + Personal Guarantee
**Fixed template:** "The loudest [a specific, recognizable, vocal group — "AI evangelists," not "some people"] have never [one concrete, checkable action whose absence is a genuine, verifiable tell — "opened the tool," not "really understood it"]. / I promise you."
**Slot test:** is the tell something you can actually observe/verify, or is it a cheap shot with no real evidence behind it?
**Why it works:** "I promise you" after a bold claim signals personal conviction backed by direct experience, not secondhand opinion — raises stakes on the poster's own credibility and invites the reader to test the claim.
**Real example:** *"The loudest AI evangelists in the room have never opened the tool. I promise you."*

---

### 17. Difficulty Reallocation
**Fixed template:** "[The specific decision/step people believe is the bulk of the difficulty] is the easy part. / [The actual category of effort that dominates] is [a real, sourced percentage — or explicitly labeled 'roughly X%' if it's your own estimate]%, not [the specific thing people wrongly assume takes the effort]."
**Slot test for the percentage:** never present a guessed number as fact — if it isn't sourced, label it as an estimate explicitly in the copy.
**Why it works:** reallocating perceived difficulty (this part is easy, THAT part is where the real work is, and here's the number) reframes the entire mental model of the task, not just one detail.
**Real example:** *"Choosing the LLM is the easy part. AI agents are 95% plumbing, not prompts."*

---

### 18. Wrong Metric / Wrong Race
**Fixed template:** "Everyone is watching the wrong [a single word/short phrase naming a genuinely trackable metric, leaderboard, or comparison]."
**Slot test:** are there two REAL, nameable, sourceable measurements behind this — a popular one everyone tracks, and a less-visible one that actually matters more — which the post's body will reveal? Both must be genuinely real, never invented for the contrast.
**Why it works:** a single blunt claim with no immediate justification forces the reader to keep reading just to find out what the "right" metric is — the entire tension lives in the withheld answer.
**Real example:** *"Everyone is watching the wrong race."* (re: consumer AI usage vs. enterprise AI spend)

---

## Explicitly excluded from this bank
Templates that only appeared once with weak reusability, or that overlapped too closely
with a stronger template above, are intentionally left out rather than padded in to hit a
round number. Quality of distinct mechanism beats hitting exactly 20.

## Finding what most people actually think (verification, not assumption)
Several templates (2, 5, 8, 12) require a claim about what "most people think" or
"everyone says." Never assume this — an unverified claim about consensus can be wrong,
and a hook built on a false premise fails immediately with any reader who doesn't hold
that belief. Verify using, in order of rigor:
1. **Golden-dataset cross-check.** Does the same belief, or a close paraphrase, appear
   stated as assumed-true in 2+ other real posts (the original creator's or others' in the dataset)? If
   multiple independent creators state it as given, it's real consensus.
2. **Comments evidence.** Has someone said this unprompted in the comments on a related
   post — either holding the belief or reacting to someone else stating it?
3. **If neither confirms it:** do not publish the hook as-is. Flag it explicitly: "I
   believe [X] is a common belief but haven't verified it — want me to use this hook
   anyway, or pick a different template?" Never silently assume consensus exists.

## How to use this bank when drafting
1. Read the belief being corrected. Ask: what's the actual *shape* of the correction —
   ambition-vs-prerequisite? category error? wrong metric? insider tell? Match the
   template to the shape, don't force template 1 by default.
2. Fill every bracket with something **specific and real** — a named tool, a real
   percentage, a verifiable credential, a real quote. If a slot can't be filled with
   something real, don't fabricate it — pick a different template or ask the writer for the
   missing specific.
3. Check the "why it works" line — if your draft hook doesn't actually create that
   mechanism (the tension, the stakes, the recognition), it's not using the template
   correctly even if it superficially matches the pattern.
4. **Run the slot-substitution test before finalizing:** read only the fixed words (skip
   the brackets) — do they form a recognizable rhythm on their own, with no room for
   creative reinterpretation? If a bracket only says something generic like `[SLOT A]`
   with no description inline, it's not filled in correctly — go back and write the
   specific description directly into the bracket.
