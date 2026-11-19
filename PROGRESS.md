# Progress log

## Current state (updated 2026-11-19)
- **Now:** no active task.
- Last release: 0.3.0 (tag `v0.3.0`): build in runs that stop where the plan says, lighter build rules, a shorter README with figures ([#5](plans/issue-5-build-runs/PROGRESS.md)).
- README figure redrawn with you and GitHub lanes (no task; docs only, no version bump).
- Open: [#3](https://github.com/giulianonetto/research-workflow/issues/3), clear done tasks and old log entries at a release.

Times are local.

## 2026-11-19: README figure shows you and GitHub
### Next
- [#3](https://github.com/giulianonetto/research-workflow/issues/3): clear done tasks and old log entries at a release (`/new-plan` when it is worth starting).
### 14:59: life-of-a-task figure redrawn
- `docs/figures.py` `flow()`: two lanes under the cards (what you do, what you see on GitHub), Finalize drawn as the gate into `planned`, review shown per step and per branch, a record-keeping row for the two logs, `/sandbox` and "change the plan" in an any-time row. `docs/workflow.html` matches it (lanes, gate, `/sandbox` note). README: new alt text, a "Review in small pieces" bullet, a line on experiments and `/write-results`.
- **DECISION 2026-11-19 14:59:** the life-of-a-task figure shows a "you" lane and an "on GitHub" lane under the five stages, because the old figure hid the issue, its checklist, the sub-issues and the PRs, which are how the user follows and reviews Claude's work in small pieces (user review of the README)
- **DECISION 2026-11-19 14:59:** Finalize is drawn under `drafting`, with `planned` as a gate in the gap after it, because the check happens while drafting and the status changes only on the user's yes; `planned` is a waiting state that `/implement-next` leaves on its first step (`skills/finalize-plan/SKILL.md`)
- **DECISION 2026-11-19 14:59:** no rule to push the task branch after each `plan:` commit, and the figure says plan updates are "committed" without push details, because when to push plan edits is the user's choice and commit vs push is too fine a point for the README (user)
- **DECISION 2026-11-19 14:59:** the figure gets a RECORD KEEPING row that tells the repo log (`PROGRESS.md`) from the task log (`plans/<task>/PROGRESS.md`), without archiving at a release, because archiving is not in the workflow yet ([#3](https://github.com/giulianonetto/research-workflow/issues/3)) and the README should not show a feature users cannot use (user asked; left out until #3 ships)
- **DECISION 2026-11-19 14:59:** `/sandbox` moves from the "Shape it" stage to "any time", in the figure and in `docs/workflow.html`, because it is used at every stage, also after build steps (`skills/sandbox/SKILL.md`)

## 2026-11-18: workflow review; versions 0.2.0 and 0.3.0
[#2](plans/issue-2-right-size-build/PROGRESS.md) done: simpler workflow, released as 0.2.0. [#5](plans/issue-5-build-runs/PROGRESS.md) done: build in runs that stop where the plan says, released as 0.3.0.
### Next
- [#3](https://github.com/giulianonetto/research-workflow/issues/3): clear done tasks and old log entries at a release (`/new-plan` when it is worth starting).
### 15:05: #5 done; 0.3.0 merged and tagged
- [#5](plans/issue-5-build-runs/PROGRESS.md): [PR #6](https://github.com/giulianonetto/research-workflow/pull/6) merged into `main` (`8c4c736`); status `done`; tag `v0.3.0` pushed for the release workflow.
### 14:09: #5 in-progress
- [#5](plans/issue-5-build-runs/PROGRESS.md): step 1 built; status `planned` → `in-progress`.
### 14:04: #5 planned
- [#5](plans/issue-5-build-runs/PROGRESS.md) finalized: status `planned`, two plan gaps fixed (stops added, missing doc spots named); checklist in the issue.
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
