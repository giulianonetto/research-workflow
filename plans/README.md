# Plans

Workflow version: 0.2.0 ([research-workflow](https://github.com/giulianonetto/research-workflow)). `/setup-workflow` compares this line with its own to offer updates.

This file holds all the rules of the workflow. One folder per task: `plans/<task>/PLAN.md` (what and how) and `plans/<task>/PROGRESS.md` (what was done and decided). Optional `plans/<task>/sandbox/`: code for manual inspection, indexed in its `README.md`; its outputs go to `tmp/sandbox/<task>/` (not in git). The flow is in the [README](../README.md#development-workflow).

## Commands

- `/new-plan`: starts a task as a draft (status `drafting`).
- `/grill-plan`: asks about the plan in rounds, until nothing is left silently assumed. Any time while drafting.
- `/finalize-plan`: checks the plan, sets it to `planned` after you confirm, then prepares the build on GitHub.
- `/implement-next`: builds the next step.
- `/progress`: keeps the logs up to date; changes a status only when you say so.
- `/project-refresher`: says where things stand and what is next. It never starts work.
- `/sandbox`: gives you code to run and look at yourself.

Skill names are always written `/name`.

A task can be an **experiment** (tries something out and ends in an answer): same commands, plus `/write-results` to write up, and the folder layout, `RESULTS.md`, `analysis.qmd` and close check in [EXPERIMENTS.md](EXPERIMENTS.md). Start one with `/new-plan exp`.

## Build

- **One branch per task**, named like its folder: `issue-<N>-<slug>`. Each step of `PLAN.md` is one commit on it. Never several commits for one step by default. Review fixes made before the commit go into it. A fix after the push is one commit, named after the step.
- **Big step:** a step that would pass about 400 changed lines of code (tests and logs not counted), or would touch unrelated parts of the code. It lists clear sub-steps in `PLAN.md`. It gets a sub-issue and its own branch, `<task branch>-step-<n>` (made from the task branch), one commit per sub-step, and a PR into the task branch. More lines are fine for mechanical changes (renames, generated fixtures, moved code) if the commit or PR says so. The number is a guide from code-review studies (SmartBear/Cisco: about 200-400 lines per review); Claude uses judgment.
- **At the end:** one PR from the task branch into `main`. Its description says `Closes #<N>`, so merging closes the task issue.

## The task issue

Every task has a GitHub issue.

- **The issue says why, the plan says how.** The body is the problem in 2-3 lines and the link to `PLAN.md`. It never lists the solution, so it cannot go stale. The link is in the body, not in a comment. After the merge it points to `main` (the branch link breaks when the branch is deleted). The issue title follows the plan's title.
- **Checklist:** below the link, one checkbox per `PLAN.md` step. This is the one place step status is kept. A big step links its sub-issue.
- **Sub-issue:** 3 lines (what, done when, what to review) and a link to its `PLAN.md` step. Never copy the plan into issues.
- **User-run checks:** checks that need something Claude cannot run (a cluster, real data, a GPU, credentials). Keep one only if its answer could change a decision. Bundle them, so one run covers as many as possible. Each one is a checkbox in the task issue.

## Review

Before each step commit and before each PR. Report each part under its own heading:

- **Bugs:** Claude Code's built-in `/code-review`.
- **Spec:** against the `PLAN.md` step: what is missing, what was not asked for, what looks wrong. Adapted from Matt Pocock's Spec axis.
- **Research:** rows silently lost in joins or filters, missing values, coordinate or unit mix-ups, randomness without a seed, numbers that look wrong.
- **Style:** the project's documented style only, plus three smells: unclear names, duplicated code, options nobody asked for.

**Merge rule:** a PR into the task branch: Claude merges it when it is low risk and the tests pass, and asks when it is hard to undo or costly. The PR into `main`: you merge it. A project's `CLAUDE.md` can override this rule.

## Plan changes

For any reason, in any status, at any time:

- Change `PLAN.md` only for what you said or decided. Show the change before writing it.
- Log every decision as a DECISION line, whether or not it changes `PLAN.md`. A settled question leaves **Open questions**.
- While `drafting`, edit `PLAN.md` freely. Once `planned` or later, a decision that changes the Goal or what a step does gets the `(plan change)` tag and says what the plan missed:
  `- **DECISION YYYY-MM-DD HH:MM (plan change):** <what changed>, because <reason>; the plan missed: <what> (<evidence>)`
  Wording fixes need no tag.
- If an open question is added to a `planned` or `in-progress` task, ask once: keep the status, or go back to `drafting`?
- Keep GitHub in step: update the sub-issue of a changed step, and the task issue's checklist or title when they change.
- Commit `PLAN.md` and the log together: `plan: <short summary>`.

## Logs

- The folder's `PROGRESS.md` and each task's have the same structure: a header, a short **Current state** block, then dated entries (`## YYYY-MM-DD: <title>`), newest first; within a date: summary, `### Next`, then time-tagged sections (`### HH:MM: <title>`), newest first.
- A task's `PROGRESS.md` starts with `# Progress: <title> (#<N>)`, then this header line, exactly (tools read the status from it):
  `**Status:** <status> · **Kind:** <task | experiment> · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** <link>`
- **Current state** is rewritten, not appended, at every update (with its date): at most ~6 one-line bullets, readable in a few seconds. Explanations go in the dated entries.
- **The task log** keeps the work, its evidence and every decision of the task.
- **The folder log** keeps only its Current state (the active tasks, with links) and what no task log has: status changes, the task's PR into `main`, releases, work outside any task. No section per session. A step, a big step's PR into the task branch, or a plan change alone does not touch it.
- **Same commit:** a log update goes into the same commit as the work it describes. A commit for the log alone only when nothing else changed (for example, right after merging a PR built in another worktree). When you ask Claude to commit work (also work done by hand), Claude updates the logs in that commit.
- **Next** lives where the work is open: in the task log while the task is open, in the folder log for anything else. A `done` or `dropped` task's Next is `None: task <status>.`; follow-up work goes in the folder log's Next.
- Times are local.

## DECISION lines

Every major decision (an option chosen or ruled out) is one line inside a time-tagged section, in this exact format, so all decisions are one grep away:

```
- **DECISION YYYY-MM-DD HH:MM:** <what was decided>, because <reason> (<evidence: sandbox entry, commit, job>)
```

- One sentence that makes sense alone (grep shows only the line). Log a decision whether or not it changes `PLAN.md`: the plan says what, the line keeps why and when.
- A decision that changes an agreed plan carries the `(plan change)` tag (see Plan changes).
- Never edit or delete an old line. A changed decision gets a new line: `..., replaces YYYY-MM-DD HH:MM, because ...`.
- Task decisions go in the task log; decisions outside any task in the folder log. Never in both.

All decisions: `grep -rn '^- \*\*DECISION' PROGRESS.md plans/*/PROGRESS.md`

## Status

`drafting` (plan being written or discussed) · `planned` (plan agreed, not started) · `in-progress` (plan being built) · `done` (finished, summary in the folder's PROGRESS.md; for an experiment: objective answered, whatever the answer) · `dropped` (abandoned, reason in its PROGRESS.md; for an experiment: stopped without an answer).

- The status is kept in one place only: the header line of the task's `PROGRESS.md`. Not in `PLAN.md`, not in a table. `/project-refresher tasks` lists every task with its status.
- It changes only by your choice: `/new-plan` (→ `drafting`), `/finalize-plan` (→ `planned`, after you confirm), `/implement-next` (→ `in-progress` on the first step of a `planned` task: running it is your choice to start), your answer to the question in Plan changes, or telling `/progress`.
- A task on hold stays `in-progress`, with the reason in its Current state.
- A PR opened or merged is an event, not a status: the task's PR into `main` goes in the folder log, a big step's PR only in the task log. When a task is finished, keep its folder as history.

## Glossary

- `GLOSSARY.md` at the root, created when the first term is agreed. Key terms only, added only when you agree. Use its terms in plans, code and commit messages. A term qualifies when all three hold:
  1. **Project-specific meaning:** we use it in a way a researcher in the field wouldn't assume, or we picked one of several competing definitions. Standard field terms stay out.
  2. **Costly if misread:** confusing it would silently change results.
  3. **Used across tasks:** it appears in more than one plan or module.

  Aim for about 10-15 entries in total.

## Tasks in this repo

- [issue-5-build-runs](issue-5-build-runs/): build in runs that stop where the plan says, with lighter build rules (#5), started 2026-11-18
- [issue-2-right-size-build](issue-2-right-size-build/): simplify the workflow and right-size the build (#2), started 2026-11-17
- [initial-design](initial-design/): initial design of the workflow, started 2026-10-29
