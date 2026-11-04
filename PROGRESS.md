# Progress log

## Current state (updated 2026-11-04)
- **Now:** no active task. Version 0.1.1 released (PR #1 merged, `f889652`; tag `v0.1.1`).
- Last task: [initial-design](plans/initial-design/PROGRESS.md) (done).
- Next: try it on a real project; rough edges become issues.

Times are local.

## 2026-11-04: version 0.1.1 (no Next on done tasks)
### 16:24: 0.1.1 merged and tagged
- [PR #1](https://github.com/giulianonetto/research-workflow/pull/1) merged into `main` (`f889652`); checks pass on `main`. Tag `v0.1.1` pushed for the release workflow.
### 16:30: PR for 0.1.1
- Found on a real project: after "mark done", `progress` left a stale **Next** in the done task's log. `progress` step 3 and 5, `plans/README.md` template (and this repo's copy), CHANGELOG, examples page; version 0.1.1. Checks pass.
- **DECISION 2026-11-04 16:30:** a `done` or `dropped` task keeps no Next (`None: task <status>.`, link to the folder log) and follow-up work goes in the folder log's Next, because a Next in a closed task's log is never read again, so nothing shows when it goes stale (user)

## 2026-10-30: version 0.1.0
- [initial-design](plans/initial-design/PROGRESS.md) done: experiments, `/write-results`, repo with checks and releases.
### 10:30: repo set up
- Skills, plugin manifest, examples page, checks, release workflow.

## 2026-10-29: design
### 22:40: draft-friendly planning
- [initial-design](plans/initial-design/PROGRESS.md): review fixes, `to-plan` split into three commands, DECISION lines.
