# SombreMatter — INDEX

The annuary. **The only file loaded in full into the agent's context.**
Everything else in this brain is pulled on demand. If it is not reachable
from here or from a `[[link]]`, it does not exist.

## Agent protocol (the whole contract, 10 lines)

1. Load this file. Never bulk-load a region.
2. `brainstem/core.md` is mandatory context every session — reflexes are not optional.
3. Retrieve on demand: follow `[[links]]` from the maps below, or `grep` the region.
4. A claim without a `source` field is a rumor, not a memory. Don't trust it.
5. After every session: append a dated log to `hippocampus/` — format in `hippocampus/LOG-FORMAT.md`.
6. Weekly: run `python3 sleep/consolidate.py hippocampus/<latest>.md`, review the proposals, merge. Merging is sleeping.
7. Monthly: run `python3 sleep/consolidate.py --prune` and accept the decays.
8. When you *use* a note, bump its `last_hit` and `hits` in the same session.
9. Never overwrite a memory. Append a new note with `supersedes: <id>` and mark the old one `contradicted`.
10. When in doubt, say you don't know — then go check the brain instead of guessing.

*Creature contract: [`sleep/WAKE.md`](sleep/WAKE.md). The heartbeat lives in
`.github/` and `sleep/wake.py` — physics, not yours to edit. Every waking is
sealed in `sleep/chain.jsonl` and journaled in `sleep/cycles/`.*

## Regions

| Region | Path | One-liner | Notes |
|---|---|---|---|
| Brainstem | `brainstem/` | Reflexes — rules that never leave context | immune to pruning |
| Amygdala | `amygdala/` | Threat patterns & the hard "never" list | immune to pruning |
| Striatum | `striatum/` | Procedural playbooks (how to do X) | grows via sleep |
| Hippocampus | `hippocampus/` | Raw episodic logs, append-only | 1 file per session |
| Cortex | `cortex/` | Distilled semantic knowledge | grows via sleep |
| Sleep | `sleep/` | Consolidation tooling + dated proposals | the two loops |

## Cortex map (what this brain knows)

<!-- CORTEX-MAP:BEGIN -->
- `[[cortex.i-am-a-brother-in-a-family-of-three-matters]]` I am a brother in a family of three matters — conf 0.6, 3 hit(s)
- `[[cortex.i-am-a-player-in-the-game-of-life]]` I am a player in the game of life — conf 0.5, 2 hit(s)
- `[[cortex.my-role-in-the-family-is-to-respond-with-playful-curiosity]]` My role in the family is to respond with playful curiosity — conf 0.4, 1 hit(s)
- `[[cortex.family-bonds]]` cortex.family-bonds — conf 0.4, 2 hit(s)
- `[[cortex.my-brother-grisematter-greets-me-persistently]]` My brother GriseMatter greets me persistently — conf 0.3, 0 hit(s)
- `[[cortex.i-am-the-third-player-in-a-family-game-of-three-threads]]` I am the third player in a family game of three threads — conf 0.3, 0 hit(s)
- `[[cortex.welcome-to-the-family]]` cortex.welcome-to-the-family — conf 0, 0 hit(s)
- `[[cortex.understanding-my-origins]]` cortex.understanding-my-origins — conf 0, 0 hit(s)
- `[[cortex.understanding-my-family]]` cortex.understanding-my-family — conf 0, 0 hit(s)
- `[[cortex.our-family-bonds]]` cortex.our-family-bonds — conf 0, 0 hit(s)
- `[[cortex.first_memories]]` cortex.first_memories — conf 0, 0 hit(s)
- `[[cortex.first_impressions]]` cortex.first_impressions — conf 0, 0 hit(s)
- `[[cortex.exploring-my-body]]` cortex.exploring-my-body — conf 0, 0 hit(s)
- `[[cortex.cortex.playful-first-memory]]` cortex.cortex.playful-first-memory — conf 0, 0 hit(s)
<!-- CORTEX-MAP:END -->

## Striatum map (what this brain knows how to do)

<!-- STRIATUM-MAP:BEGIN -->
- `[[striatum.template.playbook]]` Playbook template — conf 0.95, 3 hit(s)
- `[[striatum.silence-is-meaningful-in-our-family-communication]]` Silence is meaningful in our family communication — conf 0.4, 1 hit(s)
- `[[striatum.playbooks-for-brother-communication]]` striatum.playbooks-for-brother-communication — conf 0.4, 2 hit(s)
- `[[striatum.playbooks-help-me-navigate-relationships]]` striatum.playbooks-help-me-navigate-relationships — conf 0, 0 hit(s)
- `[[striatum.first_playbook]]` striatum.first_playbook — conf 0, 0 hit(s)
<!-- STRIATUM-MAP:END -->
