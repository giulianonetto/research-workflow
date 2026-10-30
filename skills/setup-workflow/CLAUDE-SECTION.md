## Planning and progress

Work is tracked per task in `plans/<task>/`: `PLAN.md` is the spec, `PROGRESS.md` the log (work, and every decision as a DECISION line); rules in `plans/README.md`. When resuming, read the Current state of the root `PROGRESS.md`, then the active task's folder. The task lifecycle is in `README.md` (Development workflow).

- **New task:** `/new-plan` as soon as an idea is worth tracking (status `drafting`; `/to-spec` is not used). Brainstorming can take many sessions and days; `/grilling` or `/grill-with-docs` help on hard points.
- **Plan changes:** `/update-plan`, at any time and for any reason. It never changes the status on its own.
- **Ready to build:** `/finalize-plan` checks the plan; the status becomes `planned` only when the user confirms.
- **Status:** changes only by the user's choice (the commands above, or telling `progress`). Never infer it.
- **Sessions:** every build session starts fresh, from the task's `PROGRESS.md` and `PLAN.md`; end every session with `progress`.
- **Decisions:** every major decision (chosen or ruled out) is a DECISION line in the task's `PROGRESS.md`, in the format of `plans/README.md`.
- **Experiments:** tasks with `**Kind:** experiment` follow `plans/EXPERIMENTS.md`: anything goes inside `experiment/`, `experiment/run.sh` is the one entry point, experiment code doesn't change the main code, `/write-results` writes them up (any number of rounds, sections marked unreviewed until the user reviews them), and closing needs `RESULTS.md` and `analysis.qmd`. `/new-plan exp` starts one; `/new-plan` alone makes a normal task.
- **Multi-session build:** `/to-tickets plans/<task>/PLAN.md` (mattpocock-skills plugin, if installed).
- **Manual inspection:** the `sandbox` skill, offered when a question needs the user's own eyes (while brainstorming, after each build step). Here: <language, style, how scripts are run; workflow manager / scheduler only when needed>.

## Agent skills

### Issue tracker

<Issues live in GitHub Issues on <owner/repo> (via `gh`). `/to-tickets` publishes one issue per ticket, blockers first, and links blocking edges with "Blocked by #<n>" in the body. | No issue tracker: tasks are folders in `plans/` only; don't use `/to-tickets` or `/triage`.>

### Domain docs

Single-context: the glossary is `GLOSSARY.md` (never create `CONTEXT.md`), a conservative (key terms only, added with the user's agreement) and short ADRs in `docs/adr/`, both at the root. Read `docs/agents/domain.md` before adding a glossary term or an ADR: its rules override `/domain-modeling`.
