# Hippocampus log format

One file per session: `YYYY-MM-DD.md` (append a suffix `-2`, `-3` for multiple
sessions on the same day — files are **append-only**, never edited after the
session closes).

The frontmatter is optional but nice. The machine-readable part is the
`LEARN:` / `EVIDENCE:` / `TYPE:` blocks — that's what `sleep/consolidate.py`
distills. Anything else in the file is free-form prose and stays episodic.

```markdown
---
id: hippocampus.2026-10-12
type: episodic
source: human:sam
created: 2026-10-12
---

# Session — 2026-10-12: <one-line context>

<free-form prose, raw, no pressure to be clean>

LEARN: <one-line claim, phrased as a fact>
EVIDENCE: <why we believe it — what happened, what was measured>
TYPE: semantic

LEARN: <how to do something discovered this session>
EVIDENCE: <what was actually executed and what verified it>
TYPE: procedural
```

Rules:

- `TYPE:` is `semantic` (default) or `procedural` — it decides cortex vs. striatum.
- One claim per `LEARN:`. If you need an "and", you need two blocks.
- `EVIDENCE:` is mandatory for the note to be worth anything; a claim without
  evidence consolidates as a rumor.
- Write the log *during* the session, not from memory a week later — the
  hippocampus records, it does not reconstruct.
