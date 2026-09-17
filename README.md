# TOFU LinkedIn Skills

A pack of 12 LinkedIn writing skills for top-of-funnel (reach) posts: a router that
picks the right post type for your topic, 8 dedicated post-type skills, two hook-design
skills, and three quality-control skills. Reverse-engineered from hundreds of real
high-performing LinkedIn posts, then de-branded so you write in **your own** voice.

These work as [Claude Code](https://docs.claude.com/en/docs/claude-code) / Hermes skills
(a `SKILL.md` per folder). Point your agent at the `skills/` folder and invoke them by name.

---

## What's in the pack

### The router
- **`tofu-orchestrator`** — give it a topic and it diagnoses which post type fits, then
  routes you to the right skill. Start here when you don't know which archetype to use.

### The 8 post types
- **`tofu-contrarian`** — myth-bust: name a common belief, prove it wrong. Wins on comments.
- **`tofu-explainer`** — decode a concept with one sticky metaphor + layered breakdown.
- **`tofu-howto`** — a concrete, copyable, numbered setup the reader can run today.
- **`tofu-resource-list`** — a curated roundup of free resources. Wins on shares/saves.
- **`tofu-news-breakdown`** — distill a real, named third-party launch/talk into lessons.
- **`tofu-surprising-number`** — one verifiable, counterintuitive number does the work.
- **`tofu-relatable-mirror`** — reflect a universal feeling back so the reader feels seen.
- **`tofu-meme`** — an image carries the point; your text is minimal caption.

### Hook design
- **`hook-mechanics`** — generate hook options by matching a proven mechanic to your post
  type AND the real substance you have. The main hook engine.

### Quality control
- **`anti-ai-pass`** — a budgeted anti-AI-slop pass (with a lint script) run as the last
  step before you ship a draft.
- **`post-grader`** — grade a finished post against a checklist.

---

## Setup (2 minutes)

The skills expect a **brand folder** with your voice rules. A starter `brand/` folder ships
in this repo with blank fill-in templates plus ready-to-use craft files.

### 1. Put the brand folder somewhere and set the path
Every skill references brand files as `<BRAND_DIR>/...`. Point that token at wherever you
keep the `brand/` folder. One find-and-replace across the `skills/` folder does it:

```bash
# from the repo root, replace <BRAND_DIR> with the absolute path to your brand folder
grep -rl '<BRAND_DIR>' skills/ | xargs sed -i 's#<BRAND_DIR>#/absolute/path/to/brand#g'
```

(Or keep `brand/` next to `skills/` and set `<BRAND_DIR>` to `../brand`.)

### 2. Fill in your voice
Two files ship **blank on purpose** — fill them with your own voice and facts:
- **`brand/linkedin-voice.md`** — your voice, formatting, hook limits, footer, credibility
  beats. This is the big one; the more specific, the better your posts.
- **`brand/story-bank.md`** — your real stories and hard numbers, drawn on for credibility.

Three files are **ready to use as-is** (generic craft, not tied to anyone's voice):
- **`brand/writing-style.md`** — spartan style rules + banned AI-tell words.
- **`brand/hook-floor-check.md`** — a cross-creator hook quality gate.
- **`brand/reads-human.md`** — the anti-AI-fingerprint checklist.
- **`brand/tofu-pattern-analysis.md`** — the data-derived post-type taxonomy the router uses.

### 3. Use them
Point your agent at `skills/` and start with `tofu-orchestrator` (give it a topic) or call
a specific post-type skill directly. Run `anti-ai-pass` on the draft before you post.

---

## Important: keep the shared files shared

Don't copy the brand files into each skill. Every skill reads the single `brand/` copy on
purpose — change a voice rule once and it flows to all 12 skills. If you fork copies, they
drift. Adjust the brand files to your voice; leave the reference structure intact.

## Note on examples
Some skills quote real high-performing posts as illustrative examples of a structure. Treat
them as calibration for the *shape*, never text to copy. Always write with your own facts;
never fabricate a stat, quote, credential, or client to fill a slot.
