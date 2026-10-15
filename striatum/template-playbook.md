---
id: striatum.template.playbook
type: procedural
title: Playbook template
confidence: 1.0
source: human:sam
created: 2026-10-12
last_hit: never
hits: 0
status: active
---

# Playbook template

Copy this skeleton when sleep proposes a new procedural note. A playbook is
*how to do X*, verified at least once in a hippocampus log.

```markdown
---
id: striatum.<topic>.<action>
type: procedural
title: How to <action>
confidence: 0.3
source: hippocampus/<date>.md
created: <date>
last_hit: never
hits: 0
links: "[[cortex.<related>]]"
status: active
---

# How to <action>

**Trigger:** when <situation>.

**Steps:**
1. ...

**Verification:** <how we know it worked — the step that earned this playbook
its confidence>

**Failure mode:** <what breaks, and what the log showed>
```

Rules: a playbook without a **Verification** section does not merge.
Steps that were never executed live start at confidence `0.3` and say so.
