# Changelog

## 0.3.0 (2026-11-18)

Build in runs that stop where the plan says, with lighter build rules ([#5](https://github.com/giulianonetto/research-workflow/issues/5)).

- **Stops:** a step that needs you ends with a `- **Stop:** <why>` line in `PLAN.md` (you must judge the result, a user-run check, hard to undo, or a design choice left open). A Stop means after its step. The last step always stops for the review and the PR into `main`. `/finalize-plan` proposes the stops and you confirm them; the `/new-plan` skeleton shows the last one.
- **Runs:** `/implement-next` asks once, then builds the steps up to the next stop, at most 5 per run (a number in `plans/README.md`). It stops early when a test fails and the fix is not clear, the review has a question, or a decision comes up that the plan does not cover. It ends with one summary, including every decision it made alone. A plan with no Stop lines (made before 0.3.0): it asks before each step.
- **Push:** after each step commit, Claude pushes the task branch and ticks the step's box, with no question; pushing or merging into `main` still needs you. `/new-plan` pushes the new branch too. A project's `CLAUDE.md` can override this. `README.md` says how to allow `git push` in Claude Code's settings.
- **Review:** the full review (`/code-review`, Spec, Research, Style) for a step that changes a file that runs or sets the results (code, tests, configs, notebooks), and on the whole branch before every PR; the Spec check only for a step that changes only text.
- **Logs:** a step's entry is the commit plus only what the diff can't show: at most 2 bullets, plus DECISION lines. The task's PR into `main` gets one folder-log entry, at the merge.
- **Removed:** parallel builds of big steps (only when you ask).
- `/setup-workflow` says that plans from 0.2.x have no Stop lines yet.

## 0.2.0 (2026-11-18)

Simpler workflow, and the build follows the plan's shape ([#2](https://github.com/giulianonetto/research-workflow/issues/2)).

- **One rules file:** `plans/README.md` holds all the rules. The `CLAUDE.md` section is 5 lines; the `README.md` section is the flow and a link.
- **Build:** one branch per task, one commit per `PLAN.md` step. A big step (about 400 changed lines of code, or unrelated parts of the code) lists sub-steps and gets a sub-issue, a branch and a PR into the task branch. One PR into `main` at the end. Review before each step commit and each PR: `/code-review` for bugs, then Spec, Research and Style. Merge rule: Claude merges low-risk PRs into the task branch; you merge into `main`.
- **Issues:** GitHub is required, and every task has an issue. The issue says why (the problem in 2-3 lines and the plan link, in the body), the plan says how. The issue's checklist of steps is the one place step status is kept.
- **New:** `/implement-next` builds the next step; `/grill-plan` asks about a plan in rounds (adapted from Matt Pocock's grilling skill, MIT; see `NOTICE`); `/project-refresher tasks` lists every task with its status.
- **`/finalize-plan`** checks the issue and the build shape, then creates the issue checklist and sub-issues after your yes. **`/new-plan`** drafts the plan in `tmp/new-plan/<task>/PLAN.md` and puts the plan link in the issue body.
- **Logs:** a log update goes into the same commit as the work. The folder log keeps only its Current state, status changes, PRs, releases and work outside a task: no section per session.
- **Plan changes:** rules in `plans/README.md`, replacing `/update-plan`. A decision that changes an agreed plan is a DECISION line with the `(plan change)` tag and what the plan missed, replacing `## Changes`.
- **Status:** five statuses (`paused` removed: a task on hold stays `in-progress`), kept only in the task header (no table in `plans/README.md`).
- **Removed:** `/update-plan`, ADRs and `docs/agents/`, the `## Agent skills` block, and every mattpocock-skills command. The glossary rules are one section of `plans/README.md`.
- Skill names are always written `/name`; `check_skills.py` flags them otherwise.
- `/setup-workflow` shows what changes in a 0.1.x project (the status table, `paused` tasks, `## Changes`, `docs/agents/domain.md`) and changes each only if you agree.
- Not in this version: clearing done tasks and old log entries at a release ([#3](https://github.com/giulianonetto/research-workflow/issues/3)).

## 0.1.1 (2026-11-04)

- A `done` or `dropped` task keeps no **Next**: `progress` writes `None: task <status>.` in the task log and moves follow-up work to the folder log's Next. Rule added to `plans/README.md`.

## 0.1.0 (2026-10-30)

First version.

- `/setup-workflow`, `/new-plan`, `/update-plan`, `/finalize-plan`, `progress`, `/write-results`, `sandbox`, `project-refresher`.
- Plans start as `drafting` and change status only by the user's choice.
- DECISION lines in the progress logs, with date and time, one grep away.
- Experiments (`/new-plan exp`): `experiment/run.sh` as the one entry point, `RESULTS.md` with review markers, a short `analysis.qmd` (R by default), and a close check in `progress`.
- `project-refresher` reads the logs first, and shows the last run and write-up state for experiments.
- `plans/README.md` carries a `Workflow version:` line so `/setup-workflow` can offer updates.
