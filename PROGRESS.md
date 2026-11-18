# Progress log

## Current state (updated 2026-11-18)
- **Now:** [issue-5-build-runs](plans/issue-5-build-runs/PROGRESS.md) (drafting): build in runs that stop where the plan says, with lighter build rules ([#5](https://github.com/giulianonetto/research-workflow/issues/5)).
- Last release: 0.2.0 (tag `v0.2.0`): one rules file, the build follows the plan's shape ([#2](plans/issue-2-right-size-build/PROGRESS.md)).
- Open: [#3](https://github.com/giulianonetto/research-workflow/issues/3), clear done tasks and old log entries at a release.

Times are local.

## 2026-11-18: workflow review; version 0.2.0
[#2](plans/issue-2-right-size-build/PROGRESS.md) done: simpler workflow, released as 0.2.0.
### Next
- [#3](https://github.com/giulianonetto/research-workflow/issues/3): clear done tasks and old log entries at a release (`/new-plan` when it is worth starting).
### 12:58: #5 started
- Issue [#5](https://github.com/giulianonetto/research-workflow/issues/5) and task [issue-5-build-runs](plans/issue-5-build-runs/PROGRESS.md), status `drafting`; its decisions are logged there.
### 12:25: #2 done; 0.2.0 merged and tagged
- [PR #4](https://github.com/giulianonetto/research-workflow/pull/4) merged into `main` (`37d63c5`); [#2](plans/issue-2-right-size-build/PROGRESS.md) `done`; tag `v0.2.0` pushed for the release workflow.
### 12:22: #2 PR opened
- [#2](plans/issue-2-right-size-build/PROGRESS.md): [PR #4](https://github.com/giulianonetto/research-workflow/pull/4) into `main` opened (0.2.0).
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
