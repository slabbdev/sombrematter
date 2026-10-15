# SombreMatter schema

Every memory is a Markdown file with YAML frontmatter. One file = one claim
(cortex) or one procedure (striatum). If a note needs an "and", it is two notes.

## Frontmatter fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `<region>.<topic>.<slug>` — stable identifier, never reused |
| `type` | yes | `semantic` \| `procedural` \| `threat` \| `reflex` \| `episodic` |
| `title` | cortex/striatum | The claim, phrased as one sentence |
| `confidence` | yes | `0.0–1.0`. Starts at **0.3**, **+0.1** per re-encounter, cap `0.99` |
| `source` | **always** | Where it came from: `hippocampus/<file>`, `url:<...>`, or `human:sam`. **No source, no memory.** Unverifiable sources cap confidence at `0.3` forever |
| `created` | yes | `YYYY-MM-DD` |
| `last_hit` | yes | Last date a session actually used this note, or `never` |
| `hits` | yes | How many sessions used it. `0` = decay candidate |
| `links` | optional | `[[id]]` references to related notes |
| `supersedes` | corrections | `id` of the contradicted note |
| `status` | yes | `active` \| `decayed` \| `archived` \| `contradicted` |

## Lifecycle

```
new note (0.3) ──reinforcement (+0.1, hits++)──▶ trusted (≥0.7)
     │
     zero hits past --age-days (default 30)
     ▼
  decayed ──second prune, still nothing──▶ archived (out of the maps, file kept)
     │
     contradicted by a sourced note
     ▼
contradicted (kept visible, `supersedes` points here)
```

- `decayed` notes leave the INDEX maps but stay in the repo — deletion is not
  a brain mechanism, forgetting is.
- `brainstem/` and `amygdala/` are **immune to pruning**. Reflexes and threat
  patterns don't decay from disuse; they die by explicit review only.

## Region assignment

| `TYPE:` | Lands in | Because |
|---|---|---|
| `semantic` | `cortex/` | facts, distilled |
| `procedural` | `striatum/` | how-to, playbooks |
| written by hand after review | `amygdala/` | threats — rare, reviewed like code |
| written by hand, almost never | `brainstem/` | reflexes — constitutional |
| session logs | `hippocampus/` | append-only, never distilled in place |

## Invariants (what makes this a brain and not a folder)

1. **Append, never overwrite.** Corrections supersede; mistakes stay visible.
2. **No source, no merge.** The `source:` line is checked at every sleep.
3. **The cortex only changes during sleep.** Live sessions may only write to
   `hippocampus/` and bump `last_hit`/`hits` on notes they used.
4. **One file, one claim.** Files are cheap; retrieval is by link and grep,
   and a 200-line meandering note is unreadable at 3 a.m.
5. **Titles are claims.** "HTTP connections are not free", not "thoughts on
   HTTP". A note you can't falsify is a mood, not a memory.
