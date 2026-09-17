# Tactical How-To Hook Template Bank

8 hook templates extracted from the golden dataset (21 real, high-performing tactical
how-to / system posts in this skill's a golden set of real high-performing posts,
`tofu_type='TOFU:tactical_how-to'`, likes≥750). Each is a **distinct rhetorical
mechanism** with **fixed, literal words** locking the rhythm in place, not a vibe
description or a reskin of the same sentence. Pick the template that fits the setup
you're handing over. Don't default to template 1 (shallow-use callout) just because
it's the archetype's signature move; four other mechanisms overperform it in the data.

This is a reference for hook VARIETY. Do not copy an example hook verbatim; fill the
template with the specifics of the system you're teaching.

**Format rule for every slot:** the bracket itself carries the specific description,
never a generic label like `[SLOT A]`. Write `[the tool being used shallowly, named]`,
not `[X]` with the description in a separate paragraph. A drafter must be able to fill
the slot correctly from the bracket text alone, without cross-referencing anything else.

Every template has:
- **Fixed template**: the literal words, verbatim, with descriptive `[bracketed]` slots
  inline. Read the fixed words alone (skip the brackets) and they form a recognizable,
  repeatable rhythm on their own.
- **Slot test**: for slots needing more than the bracket can hold, a concrete pass/fail
  check (a real test, not more vague description).
- **Why it works**: the psychological/rhetorical mechanism, secondary to the fixed words.
- **Real example(s)**: the actual post(s) the template was extracted from, with attribution.
- **Use when / non-negotiables**: situational fit, plus any hard rule.

**The hard limits apply to every template below:** hook line 1 ≤ 62 characters, line 2 ≤
50 characters, no unicode-bold in the hook. Count the characters before finalizing.

**The verified shared premise underneath templates 1 and 4:** "most people use this tool
shallowly / do the costly thing" is not an assumption here, it is stated-as-given in 6+
independent golden-set posts (Adam Danyal "using it like a spell checker," Will McTighe
"Most people use Claude completely wrong," Luís Rodrigues "Most people open Claude Code
and start typing. That's the trap," Gabriel Millien "Most people use AI for answers,"
Charlie Hills "You are burning through your Claude credits by lunch," Andrew Bolis "Stop
asking ChatGPT to summarize content"). Safe to assert as a premise. Any NEW shared-belief
claim you introduce must clear the same bar (2+ real examples) or be flagged as unverified.

---

### 1. Shallow-Use Callout
**Fixed template:** "Most people use [the named tool] [like a demeaning comparison, e.g. "like a spell checker" / "like a search bar", OR for the shallow default purpose].
[The one-line consequence or "That's the trap." / "That's why their results are average."]"
**Slot test for the comparison:** it must name a concrete lesser object or lesser use, not
an abstraction. "like a spell checker," "like a vending machine," "for answers" pass;
"in a basic way," "wrong" (alone, with no picture) is weaker, borderline. If you can't
picture the lesser thing, sharpen it.
**Why it works:** it opens a status gap the reader wants off the wrong side of. Naming the
shallow use makes the reader recognize themselves, then the body offers the exit. This is
the archetype's signature move and its verified premise (see above).
**Real examples:** *"People are paying $30/month for Copilot / and using it like a spell
checker."* (Adam Danyal, 4,436 likes) · *"Most people open Claude Code and start typing. /
That's the trap."* (Luís Rodrigues, 1,066 likes) · *"Most people use AI for answers. / I've
been using it as a tutor."* (Gabriel Millien, 930 likes) · *"Most people use Claude
completely wrong."* (Will McTighe, 1,105 likes)
**Use when:** there is an obvious shallow/wrong default way to use the tool. If the topic
has no clear shallow foil (generic profile-optimization, a plain setup), don't force it,
use template 6 or 8 instead. This was a Round 0 weakness: forced shallow-use hooks on
foil-less topics scored 4-6.

---

### 2. Priced-Plan Downgrade
**Fixed template:** "Don't [pay for / upgrade to] [the expensive tier or product, with its real price: "$100 Claude plan", "a LinkedIn course"].
[These N / This] [free-or-cheaper moves] make [the cheaper path, with its price] enough."
**Slot test for both prices:** the expensive thing and the cheap alternative must be real,
current, defensible price points ($100 plan vs $20 plan; a paid course vs free). If there
is no real paid product being displaced, this template is unavailable, pick another. Never
inflate the "expensive" number to sharpen the contrast.
**Why it works:** it hands the reader permission to not spend, then owes them the method
that justifies it. "Don't upgrade (yet)" creates an open loop the numbered list closes.
The reader who almost paid feels rescued; the one who paid keeps reading to check.
**Real examples:** *"Don't upgrade to the $100 Claude plan (yet). / These 21 hacks make
the $20/month plan enough:"* (Ruben Hassid, 2,824 likes) · *"You don't need to pay for
Claude Code. / Run it free and private (on your own machine):"* (Charlie Hills, 1,429
likes) · *"Want to pay for a LinkedIn course? Don't. / Here's your 2025 LinkedIn
Masterclass:"* (Jasmin Alić, 3,283 likes)
**Non-negotiable:** the system that follows must genuinely replace the paid thing. If the
free path is materially weaker, the hook overpromised.

---

### 3. If-I-Had-To Constraint Scenario
**Fixed template:** "If I had to [achieve the concrete outcome] [under a tight constraint: "by tomorrow", "from scratch"], I would:
[Optional: "(Save this + Repost ♻️)" / "These are the N things I'd do EVERY DAY:"]"
**Slot test for the constraint:** it must be a real pressure that forces prioritization, a
deadline ("by tomorrow"), a reset ("from scratch"), a resource limit. "If I wanted to grow"
fails (no constraint, no forced choices); "If I had to close a client by tomorrow" passes.
**Why it works:** the constraint is a credibility device, it signals the list is the
battle-tested minimum, not everything the poster knows. Readers trust a forced-priority
list over a comprehensive one because the fat is already cut.
**Real examples:** *"If I had to close a client by tomorrow, I would:"* (Jasmin Alić, 2,935
likes) · *"If I had to rebuild my LinkedIn from scratch... / These are 17 things I would do
EVERY DAY:"* (Jasmin Alić, 2,655 likes)
**Use when:** the system is your own opinionated priority sequence, not a neutral setup.
The first-person "I would" is load-bearing, don't convert it to "you should."

---

### 4. Problem-Then-Count
**Fixed template:** "[The costly wrong thing the reader is doing right now, stated flat: "You are burning through your Claude credits by lunch." / "Stop asking ChatGPT to summarize content."]
[N] [ways / prompts / steps] to [the concrete payoff]:"
**Slot test for the count:** N must be the real number of steps the post delivers and
should land in the 3-7 executable range this archetype rewards. If the honest count is 17+,
the hook can still say it, but expect the step_count dimension to suffer, tighten the
system instead of advertising the bloat.
**Why it works:** it pairs a felt pain (line 1) with a bounded, countable cure (line 2).
The number promises the reader knows exactly how much work they're signing up for, which
raises save-rate; "8 ways" reads as finite and doable.
**Real examples:** *"You are burning through your Claude credits by lunch. / 8 ways to get
3x from your subscription:"* (Charlie Hills, 2,649 likes) · *"Stop asking ChatGPT to
summarize content. / Use these 9 advanced prompts to extract strategies..."* (Andrew Bolis,
1,671 likes)
**Use when:** there's a concrete, nameable pain the system fixes. The pain in line 1 must
be specific ("burning through credits by lunch"), not generic ("using AI wrong").

---

### 5. Elite-Minority Stat Gap
**Fixed template:** "[X]% of [the user group] stop at [the shallow default they never move past].
The [Y]% who [go deeper, named] [get the concrete, quantified payoff]."
**Slot test for the percentages:** X and Y are rhetorical estimates, not cited data, so
keep them round and defensible (95/5, 90/10), and only use this when the majority-stops-at-
shallow claim is genuinely true. The payoff in line 2 must be concrete and ideally
quantified ("save 10+ hours a week"), not vague ("get more out of it").
**Why it works:** it splits the audience into a stuck majority and a winning minority, and
dares the reader to join the 5%. The quantified payoff ("10+ hours a week") is the bait;
the body is the membership fee.
**Real example:** *"95% of Claude users stop at Claude Chat. / The 5% who maxx out save
10+ hours a week."* (Charlie Hills, 1,460 likes)
**Use when:** there's a clear depth ladder (a default level most never leave, a deeper level
with a real payoff). Appears once in the golden set, use it when the ladder is real, not to
manufacture false scarcity. Do not invent the percentages to fit a topic with no real gap.

---

### 6. Bounded-Time Promise
**Fixed template:** "[The concrete time budget: "60 minutes", "one weekend", "30 seconds"] to [the concrete outcome].
[The multiplied or lasting payoff: "10x your results all year:" / "Here's how in N prompts:"]"
**Slot test for the time budget:** it must be the real, honest time the system takes, and
short enough to feel free. "60 minutes," "one weekend," "30 seconds" pass. If the setup
actually takes days, don't compress it to "an afternoon", the reader who tries it and runs
over will feel lied to.
**Why it works:** a small, named time cost against a large, lasting payoff is the cleanest
effort/reward asymmetry a hook can offer. "60 minutes → results all year" makes the trade
feel irrational to refuse.
**Real examples:** *"60 minutes to optimize your LinkedIn profile. / 10x your results all
year:"* (Will McTighe, 1,442 likes) · *"How to climb all 4 layers of Claude in one
weekend:"* (Ruben Hassid, 3,798 likes)
**Use when:** the whole system genuinely fits in one bounded session. Best for foil-less
setups (profile, onboarding) where the shallow-use callout (1) has nothing to push against.

---

### 7. Tool-Can-Now Reframe
**Fixed template:** "[The named tool] can now do [the surprising high-value job people usually pay a human for].
[Here's how in [time + N steps]: / And [tool] can do that [work] for you.]"
**Slot test for the surprising job:** it must be a task the reader currently pays a person
or a subscription for (a stylist, a researcher, an analyst), named concretely. "do your
hair + colour analysis" passes (a real £500 service); "help with your style" fails (vague,
no displaced cost).
**Why it works:** the surprise is a capability the reader didn't know the tool had, framed
as replacing a known paid service. The displaced price (stated or implied) sets the value
anchor before a single step is given.
**Real examples:** *"ChatGPT can now do your hair + colour analysis. / Here's how in 30
seconds and 3 prompts:"* (Charlie Hills, 1,169 likes) · *"LinkedIn growth isn't luck ➟ it's
research. / And Perplexity can do that research for you."* (Andrew Bolis, 1,267 likes)
**Use when:** the system is one tool doing a surprising, normally-paid-for job. The claim
must be real and current, verify the tool actually does it before posting.

---

### 8. Plain How-To Authority
**Fixed template:** "How to [the concrete setup outcome, named]: [OR "N steps to [outcome]:"]
[The stakes line: "Most developers install it and wing it. That's why their results are average." / "(then send it to your entire team)"]"
**Slot test for the outcome:** it must be a specific, completable setup ("setup Claude Code
for coding," "duplicate your entire brain in Claude," "set up a Claude Project that
remembers everything"), not a fuzzy goal ("get better at AI"). If a reader can't tell what
"done" looks like, sharpen the outcome.
**Why it works:** it makes no clever move and needs none, the value is a clear, complete
setup promise plus a one-line reason the reader's current version is failing. The stakes
line supplies the missing tension a bare "How to" would lack.
**Real examples:** *"How to setup Claude Code for coding. / Most developers install it and
wing it. That's why their results are average."* (Om Nalinde, 1,057 likes) · *"How to
duplicate your (entire) brain in Claude:"* (Ruben Hassid, 1,938 likes) · *"5 steps to set
up a Claude Project that remembers everything and never starts from scratch:"* (GenAI
Works, 802 likes) · *"Don't use Claude until you read this: / (then send it to your entire
team)"* (Ruben Hassid, 1,857 likes)
**Use when:** the setup is inherently interesting or high-demand and needs no shallow-use
foil or price contrast to earn the click. Pair the plain "How to" with a stakes line, a
bare title with no tension underperforms.

---

## Explicitly excluded from this bank
Mechanisms that appeared once with weak reusability, or overlapped too closely with a
stronger template above, are intentionally left out rather than padded in to reach 10.
Notable exclusions:
- **Save/Repost bracket as a hook** ("(Save this + Repost ♻️)"): it's a footer move that
  sometimes rides in line 2, not a hook mechanism on its own. Folded into template 3 as an
  optional line, not given its own entry.
- **Bare list-count title without pain or authority** ("17 ways I use LinkedIn comments to
  get new business", Jasmin Alić, 1,557 likes): it worked on Jasmin's established audience
  and the implicit "get new business" payoff; stripped of that audience it's a naked count.
  Covered adequately by template 4 (which adds the required pain line) rather than
  duplicated as a weaker standalone.

## How to use this bank when drafting
1. Identify what you actually have: a shallow/wrong default to call out (→ 1), a real paid
   tier to undercut (→ 2), an opinionated priority sequence (→ 3), a named pain plus a
   tight step count (→ 4), a real depth ladder with a quantified payoff (→ 5), a
   bounded-time setup (→ 6), a tool doing a surprising paid-for job (→ 7), or an
   inherently high-demand setup (→ 8). Match the template to what's true, don't force
   template 1 by default.
2. Fill every bracket with something **specific and real**: a named tool, a real price, a
   real time budget, a concrete displaced service. If a slot can't be filled with something
   real, don't fabricate it, pick a different template or ask for the missing detail.
3. Check the "why it works" line. If your draft hook doesn't create that mechanism (the
   status gap, the open loop, the effort/reward asymmetry), it isn't using the template
   correctly even if it superficially matches the words.
4. **Run the slot-substitution self-test before finalizing:** read only the fixed words
   (skip the brackets). Do they form a recognizable rhythm on their own? If a bracket says
   only `[X]` with no description inline, it's not filled in, write the specific
   description directly into the bracket.
5. **Count the characters.** Line 1 ≤ 62, line 2 ≤ 50, no unicode-bold in the hook. No
   exceptions.
