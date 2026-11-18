# Progress: Right-size the build: /prep-implementation, implement-next, "what is next?" (#2)
**Status:** drafting · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#2](https://github.com/giulianonetto/research-workflow/issues/2)

## Current state (updated 2026-11-18)
- Drafting. The shape is agreed; open question 1 (old numbering) is settled, and a new step 8 removes `/update-plan` (plan changes follow a contract rule). 7 open questions left in [PLAN.md](PLAN.md).
- Nothing built yet.

## 2026-11-18: plan update: prep-implementation callable, /update-plan removed
Settled the old open question 1 and decided to remove `/update-plan`, which came up because running it with nothing to write felt unnecessary.
### Next
- Settle the open questions in `PLAN.md` (start with 1: where the parent table lives without an issue tracker), then run `/finalize-plan`.
### 10:05: plan update
- `PLAN.md`: Goal adds "fewer commands"; new bullet in "Where things are now" on `/update-plan`; step 2 says `prep-implementation` has no `disable-model-invocation` flag; new step 8 (remove `/update-plan`, contract in `plans/README.md`); docs, checks, version became step 9; open question 1 removed, the rest renumbered 1-7.
- Evidence: `finalize-plan`, `new-plan` and `update-plan` have the flag and already run `progress`, which has none (`skills/*/SKILL.md` frontmatter); `progress` already has a "plan update" kind (`skills/progress/SKILL.md:11`); `CLAUDE-SECTION.md:6` already has a plan-changes line.
- **DECISION 2026-11-18 10:05:** `prep-implementation` has no `disable-model-invocation` flag, so `/finalize-plan` can call it, because the flagged planning skills already call `progress` this way, and it creates nothing before the user confirms (user, this session)
- **DECISION 2026-11-18 10:05:** remove `/update-plan`; a plan change follows a contract in `plans/README.md`, pointed to from the always-loaded `CLAUDE-SECTION.md`, that keeps its guards (only what the user decided; show before writing), partly replacing 2026-10-29 22:17, because the command was mostly a rule, it made a discussion feel like it needed a command, and nobody types it in a build session (user, this session)

## 2026-11-17: plan started
Started from the workflow review of a real project (2026-11-16/17), where a medium task was split into 10 sub-issues. The decisions made in that review are logged below.
### Next
- See 2026-11-18.
### 14:53: plan update: new-plan drafts in a file
- New step 7 in `PLAN.md` (docs, checks, version became step 8). Came up while running `/new-plan` for this task: the 90-line draft was shown in the chat.
- **DECISION 2026-11-17 14:53:** `/new-plan` writes the draft to `tmp/new-plan/<task>/PLAN.md` and iterates on that file, keeping the approve-then-write order, because a long plan is hard to review in the chat, and `tmp/` is gitignored, survives sessions and does not depend on the branch; ruled out the session scratchpad (can be cleared on reboot) and writing into `plans/` on the branch before approval (user)
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
