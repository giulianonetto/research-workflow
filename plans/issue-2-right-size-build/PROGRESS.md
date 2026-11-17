# Progress: Right-size the build: /prep-implementation, implement-next, "what is next?" (#2)
**Status:** drafting · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#2](https://github.com/giulianonetto/research-workflow/issues/2)

## Current state (updated 2026-11-17)
- Drafting. The shape is agreed (from a real-project review); 8 open questions in [PLAN.md](PLAN.md) are about how to build it.
- Nothing built yet.

## 2026-11-17: plan started
Started from the workflow review of a real project (2026-11-16/17), where a medium task was split into 10 sub-issues. The decisions made in that review are logged below.
### Next
- Settle the open questions in `PLAN.md` with `/update-plan` (start with 1: can `finalize-plan` call `prep-implementation`?), then run `/finalize-plan`.
### 14:15: plan started
- Issue [#2](https://github.com/giulianonetto/research-workflow/issues/2), branch `issue-2-right-size-build`, `PLAN.md` drafted from `real-project/tmp/skill-building/workflow-review-2026-11-16.md`.
- **DECISION 2026-11-17 14:15:** by default a task is built on one branch with one PR, and each extra sub-issue needs a reason (parallel work, a separate review unit, or a user gate), because 10 sub-issues for a medium task were hard to follow (from draft, 2026-11-16; review note)
- **DECISION 2026-11-17 14:15:** Claude recommends the fewest sub-issues and the user decides from that recommendation, instead of fixed small/medium/large task sizes, because task size is a judgment, not a class (from draft, 2026-11-16; review note, second round)
- **DECISION 2026-11-17 14:15:** sub-issue text is 3 lines (what, done when, what to review) plus a link to the `PLAN.md` step, because copying the plan into issues made them long and repeated, and an unneeded sub-issue was noticed only at the end (from draft, 2026-11-16; review note)
- **DECISION 2026-11-17 14:15:** user gates are checkboxes in the parent issue, not sub-issues (from draft, 2026-11-16; review note)
- **DECISION 2026-11-17 14:15:** the parent issue table is the one place sub-issue status is kept, and the task log keeps events, decisions and evidence with a link to it, because two copies drift (from draft, 2026-11-16; review note, third round)
- **DECISION 2026-11-17 14:15:** one skill `/prep-implementation` prepares the build and splitting is one possible outcome of it, ruling out a separate `/split-plan`, because preparing the build also settles branches, user-run checks and the review plan (from draft, 2026-11-16; review note, third round)
- **DECISION 2026-11-17 14:15:** `/finalize-plan` calls `/prep-implementation` as its last step, and `/prep-implementation` can also run alone, because preparing the build is part of finalizing (from draft, 2026-11-16; review note, fourth round)
- **DECISION 2026-11-17 14:15:** "what is next?" goes into `project-refresher` (read-only), not a new skill, and "implement next" is a separate build skill, because asking must not start work (from draft, 2026-11-16; review note, third round)
- **DECISION 2026-11-17 14:15:** the build skill picks the next unblocked sub-issue, checks it is still needed against later findings and DECISION lines, builds independent ones in parallel (at most 2-3 worktrees, agents don't touch the logs) and shared-file ones in order (user wait first, then unblocks most, then smallest), because the next step was chosen differently in every prompt (from draft, 2026-11-16; review note)
- **DECISION 2026-11-17 14:15:** the skills name no cluster: "user-run checks" are checks Claude cannot run, kept only if the answer could change a decision and bundled once per milestone, and how to run them lives in the project's own docs, because some checks on known-good code made Claude stop and wait for nothing (from draft, 2026-11-16; review note, fourth round)
- **DECISION 2026-11-17 14:15:** review size drives the split, with about 400 changed lines of code per PR as a guide (tests and logs not counted; more is fine for mechanical changes the PR body names) and Claude's judgment deciding, because reviewers find fewer defects past about 200-400 lines (SmartBear/Cisco studies) (from draft, 2026-11-17; review note, fifth round)
- **DECISION 2026-11-17 14:15:** the build skill is named `implement-next`, to pair with "what is next?" in `project-refresher` (from draft, 2026-11-17; review note, fifth round)
- **DECISION 2026-11-17 14:15:** keep the test discipline in the build, because tests are cheap once written and caught real bugs in the review project (from draft, 2026-11-16; review note)
