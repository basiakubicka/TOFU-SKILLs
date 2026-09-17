# FOLLOW THIS WRITING STYLE

*Scope: this governs the copy/content these skills generate for you (LinkedIn posts,
captions, drafts). One carve-out: when a skill exists to reproduce a specific named
person's voice, that target voice wins wherever it directly conflicts with a rule below.
Everywhere else, these rules apply.*

• SHOULD use clear, simple language.
• SHOULD read at a 7th-8th grade comprehension level; no unexplained jargon or acronyms (say "a flowchart of which agent runs when", not "a DAG"). Product names may stay, what they do gets said plainly.
• SHOULD be spartan and informative.
• SHOULD use short, impactful sentences.
• SHOULD use active voice; avoid passive voice.
• SHOULD focus on practical, actionable insights.
• SHOULD use bullet point lists in social media posts.
• SHOULD use data and examples to support claims when possible.
• SHOULD use "you" and "your" to directly address the reader.
• AVOID using em dashes anywhere in your response. Use only commas, periods, or other standard punctuation. If you need to connect ideas, use a period or a semicolon, but never an em dash.
• AVOID constructions like " ...not just this, but also this".
• AVOID metaphors and clichés.
• AVOID generalizations.
• AVOID common setup language in any sentence, including: in conclusion, in closing, etc.
• AVOID output warnings or notes, just the output requested.
• AVOID unnecessary adjectives and adverbs.
• AVOID staccato stop start sentences.
• AVOID rhetorical questions.
• AVOID hashtags.
• AVOID semicolons.
• AVOID markdown.
• AVOID asterisks.
• AVOID these words:

"very, really, literally, actually, certainly, probably, basically, maybe, delve, embark, enlightening, esteemed, shed light, craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket, abyss, not alone, in a world where, revolutionize, disruptive, utilize, utilizing, dive deep, tapestry, illuminate, unveil, pivotal, intricate, elucidate, hence, furthermore, realm, however, harness, exciting, groundbreaking, cutting-edge, remarkable, remains to be seen, glimpse into, navigating, landscape, stark, testament, in summary, in conclusion, moreover, boost, skyrocketing, opened up, powerful, inquiries, ever-evolving"

# IMPORTANT: Review your response and ensure no em dashes.

---

# Part 2 — Reads-Human: the anti-AI-fingerprint layer

**What this is:** the rule set that makes a post read as *written by you*, not *generated*. It's the
craft layer your voice skills load on top of their patterns.

**Why it exists (the honest version):** modern AI-content detectors (e.g. Pangram) are *not* word-list or
"perplexity" checkers you can trick with surface edits. Pangram is a neural net trained on ~28M human docs
plus AI "mirrors" of them — AI text matched to human text on topic, tone, length and style — so it learns
the *residual fingerprint* that survives even when style and content are held constant. It also runs
"hard-negative mining": it harvests every human doc it wrongly flags and retrains on AI copies of them, so
popular evasion tricks become its next training set. **Conclusion: you can't reliably "beat" it with a
humanizer, and chasing that is a losing treadmill.** But the fingerprint it keys on is the *same* thing that
makes writing feel generic — so killing the fingerprint and writing well are the same job. That's what this
doc does. The goal is not evasion; it's writing that could only have come from you.

**One line to remember:** a detector's whole job is spotting text that *no particular person* wrote. The
defense is content that *only you could have written*. Specificity is the moat.

---

## Tricks that DON'T work (don't waste effort here)
These beat 2023-era detectors and nothing current. Some make writing *worse*.
- ❌ **Banning single words** (delve/leverage/etc.). Worth doing for *taste* — those words are tells to human
  readers too — but detectors were trained with those tells stripped out, so it moves nothing on detection.
  Keep the ban list (it's in the skills) as a *style* rule, not an anti-detection one.
- ❌ **Token-level randomness** ("use the 3rd-most-probable word", high temperature). This is the old
  perplexity hack. It leaves the document's structure untouched, introduces almost-right word choices
  (the uncanny-valley tell), and reads *less* human, not more.
- ❌ **Adding a typo / lowercasing on purpose.** Transparent, and your real posts are clean.
- ❌ **"Humanizer" tools.** They optimize against open detectors, not Pangram, and feed the hard-negative loop.

---

## The residual fingerprint — what actually reads as AI
Four properties. A post that has all four reads generated even if every word is "allowed."

### 1. Structural symmetry → break it
AI defaults to tidy, balanced shapes: uniform sentence lengths, uniform paragraph blocks, a clean
setup → three-balanced-points → neat resolution arc, parallel list items of equal weight.
- **Vary sentence length hard.** A 22-word sentence, then a 3-word one. Then a fragment. Humans lurch.
- **Break the arc.** Open on the messy middle, not the setup. End on a jab, not a bow.
- **Let list items be uneven** — one item two words, the next a full sentence with a `↳` aside. Equal-length
  bullets are a tell.
- **One asymmetric move per post minimum** — a tangent, an aside, a line that doesn't "balance."

### 2. Register flatness → shift gears
AI holds one tone the whole way. Humans jump: deadpan → blunt → earnest → self-deprecating, mid-post.
- Put a dry one-liner next to a serious claim. Undercut a real number with a parenthetical.
- At least one **register shift** per post (your dry layer is the vehicle — see the skills' humor sections).

### 3. Semantic smoothness → add friction
AI is hedged, complete, and never says anything only one person would know. It rounds every edge.
- **Name the un-generatable specific:** the exact breakage (*"filters timed out because nothing was
  indexed"*), the real number from your own dashboard, the named person, the timestamp, the odd true detail
  (*"for roughly 48 hours"*, *"three tanks attached to me"*).
- **Have an actual opinion** with a load-bearing edge — a claim that would make *someone* disagree.
- **Leave one thing unresolved / admit one thing.** Unfinished reads human; tidy reads generated.

### 4. Lexical sameness → widen the band
AI reaches for the single most probable phrasing every time.
- Don't repeat a frame word 4 times; find the varied real word. Prefer the concrete noun over the abstraction
  ("compounding", "landscape", "journey").
- But **don't over-correct into thesaurus-speak** — the most obvious word is often the human word too
  ("the cat sat on the *mat*"). Vary *meaningfully*, not to be strange.

---

## The instinct that DOES work: pick the 3rd-most-probable *decision*
Not the 3rd word — the 3rd *choice*, one level up, where human unpredictability actually lives and no
detector can model it:
- Not the obvious **angle** → the one most people skip.
- Not the obvious **example** → the specific weird one from your actual week.
- Not the obvious **opening** → start in the middle of the scene.
- Not the obvious **structure** → break the balanced arc.
Unlike token-jitter, this makes the writing *better*, not weirder.

---

## The Specificity Audit (the primary gate)
Before a post ships, count the details that **only you could have supplied** — a real number from your work,
a named breakage, a dated moment, a person you DMed, a true life-bank detail, a lived opinion with a scar
behind it.
- **TOFU (reach):** ≥ 2 such details. (Reach posts teach broadly, but still need your fingerprints.)
- **MOFU (trust):** ≥ 3, and one must be the turning-point moment shown as a scene.
- **If it can't clear the bar, find the missing specific from your own experience — never invent one.** A fabricated
  "specific" is worse than a generic line: it's a lie *and* it often reads AI anyway.

> Placeholder test, sharpened: swap any "specific" for `[generic detail]`. If the sentence still stands, it
> was never specific. Rewrite or ask.

---

## Fast pre-ship pass (run mentally, in order)
1. **Specificity count** meets the bar for the funnel stage? (else find the specific, don't invent)
2. **Sentence-length variance** — is there at least one very short line and one long one? Any two adjacent
   sentences near-identical length → break one.
3. **One register shift** present?
4. **One asymmetric / non-obvious structural choice** present (didn't take the tidy default arc)?
5. **A real opinion with an edge**, and **one admitted/unresolved thing**?
6. Taste-level AI-tell words gone (the skills' ban list) — last, and least important.

If 1 and the funnel value-gate pass and 2–5 each have at least one hit, it reads human. #6 is polish.
