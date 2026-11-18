# Progress log

## Current state (updated 2026-11-18)
- **Now:** [issue-2-right-size-build](plans/issue-2-right-size-build/PROGRESS.md) (in-progress): simplify the workflow and right-size the build ([#2](https://github.com/giulianonetto/research-workflow/issues/2)); 10 small steps, one PR, no sub-issues.
- Last release: 0.1.1 (tag `v0.1.1`).

Times are local.

## 2026-11-18: workflow review
### 11:56: #2 in-progress
- [#2](plans/issue-2-right-size-build/PROGRESS.md): step 1 built; status `planned` → `in-progress`.
### 11:40: #2 planned
- [#2](plans/issue-2-right-size-build/PROGRESS.md) finalized: status `planned`, six small plan gaps fixed.
### 11:26: #2 plan rewritten; #3 opened
- Reviewed the whole workflow against the real project; [#2's plan](plans/issue-2-right-size-build/PROGRESS.md) rewritten (new title, 21 DECISION lines there).
- Opened [#3](https://github.com/giulianonetto/research-workflow/issues/3): clear done tasks and old log entries at a release.

## 2026-11-17: right-size the build
### 14:15: task started
- Real-project review turned into issue [#2](https://github.com/giulianonetto/research-workflow/issues/2) and task [issue-2-right-size-build](plans/issue-2-right-size-build/PROGRESS.md), status `drafting`; the review's decisions are logged there.

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
