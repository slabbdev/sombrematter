---
id: brainstem.core
type: reflex
scope: always-in-context
confidence: 1.0
source: human:sam
created: 2026-10-12
last_hit: 2026-10-12
hits: 1
status: active
---

# Core reflexes

These fire every session, no retrieval needed. They are not opinions.

- **No source, no memory.** A claim without a `source` field is a rumor. Store it nowhere.
- **Append, never overwrite.** Corrections are new notes with `supersedes: <id>`;
  the old note becomes `status: contradicted`. The brain keeps its mistakes visible.
- **Contradiction is information.** When two notes disagree, the newest *sourced*
  one wins — but the loser stays, marked. Silent deletion is lying.
- **Search before ignorance.** "I don't know" is only allowed after a lookup,
  never before one.
- **Context is sacred.** Only `INDEX.md` + `brainstem/core.md` load by default.
  Everything else is pulled, used, released.
- **The brain is load-bearing.** If a memory shaped a decision this session,
  cite its `id` in the decision.
