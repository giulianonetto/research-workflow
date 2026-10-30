# Plans

Workflow version: 0.1.0 ([research-workflow](https://github.com/giulianonetto/research-workflow)). `/setup-workflow` compares this line with its own to offer updates.

One folder per task: `plans/<task>/PLAN.md` (what and how) and `plans/<task>/PROGRESS.md` (what was done and decided). Optional `plans/<task>/sandbox/`: code for manual inspection, indexed in its `README.md`; its outputs go to `tmp/sandbox/<task>/` (not in git). The workflow is in the [README](../README.md#development-workflow).

## Commands

- `/new-plan`: starts a task as a draft (status `drafting`).
- `/update-plan`: changes `PLAN.md` at any time, for any reason. Never changes the status, except when you answer its reopen question.
- `/finalize-plan`: checks the plan and, after you confirm, sets it to `planned`.
- `progress`: keeps both logs up to date; changes a status only when you say so.

A task can be an **experiment** (tries something out and ends in an answer): same commands, plus `/write-results` to write up, and the folder layout, `RESULTS.md`, `analysis.qmd` and close check in [EXPERIMENTS.md](EXPERIMENTS.md). Start one with `/new-plan exp`.

## PROGRESS.md format

- The folder's `PROGRESS.md` and each task's have the same structure: a header, a short **Current state** block, then dated entries (`## YYYY-MM-DD: <title>`), newest first; within a date: summary, `### Next`, then time-tagged sections (`### HH:MM: <title>`), newest first.
- A task's `PROGRESS.md` starts with `# Progress: <title> (#<N>)`, then this header line, exactly (tools read the status from it):
  `**Status:** <status> · **Kind:** <task | experiment> · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** <link, or none>`
- **Current state** is rewritten, not appended, at every update (with its date): at most ~6 one-line bullets, readable in a few seconds. Explanations go in the dated entries.
- The folder's **Current state** names the active task(s) with a link to their folder. Details stay in the task log. The folder log gets one short time-tagged section per work session (2-3 bullets + a link to the task's `PROGRESS.md`), plus status changes, PRs, and work outside any task. A plan update alone does not touch it.
- Times are local. Newest first: dates, and within a date the time-tagged sections (after the summary and Next).

## DECISION lines

Every major decision (an option chosen or ruled out) is one line inside a time-tagged section, in this exact format, so all decisions are one grep away:

```
- **DECISION YYYY-MM-DD HH:MM:** <what was decided>, because <reason> (<evidence: sandbox entry, commit, job, ADR>)
```

- One sentence that makes sense alone (grep shows only the line). Log a decision whether or not it changes `PLAN.md`: the plan says what, the line keeps why and when.
- Never edit or delete an old line. A changed decision gets a new line: `..., replaces YYYY-MM-DD HH:MM, because ...`.
- Task decisions go in the task log; decisions outside any task in the folder log. Never in both.
- A decision that also meets the ADR rules (`docs/agents/domain.md`) gets an ADR too, linked from the line.

All decisions: `grep -rn '^- \*\*DECISION' PROGRESS.md plans/*/PROGRESS.md`

## PLAN.md changes

While `drafting`, `PLAN.md` is edited freely. Once `planned` or later, a change to the Goal or to what a step does adds a dated line at the top of its `## Changes` section (at the bottom of the file): `YYYY-MM-DD: <what changed>, because <reason> (<link>)`. Wording fixes add nothing.

## Status

`drafting` (plan being written or discussed) · `planned` (plan agreed, not started) · `in-progress` (plan being carried out) · `paused` (stopped on purpose, reason in its PROGRESS.md) · `done` (finished, summary in the folder's PROGRESS.md; for an experiment: objective answered, whatever the answer) · `dropped` (abandoned, reason in its PROGRESS.md; for an experiment: stopped without an answer).

A status changes only by your choice: `/new-plan` (→ `drafting`), `/finalize-plan` (→ `planned`, after you confirm), the reopen question of `/update-plan`, or telling `progress`. It is kept in two places only: this table and the header line of the task's `PROGRESS.md` (not in `PLAN.md`). Change both together. A PR opened or merged is an event logged in the entries, not a status. When a task is finished, keep its folder as history.

| Task | Status | Started |
|---|---|---|
| [initial-design](initial-design/) | done | 2026-10-29 |
