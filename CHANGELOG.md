# Changelog

## 0.1.0 (2026-10-30)

First version.

- `/setup-workflow`, `/new-plan`, `/update-plan`, `/finalize-plan`, `progress`, `/write-results`, `sandbox`, `project-refresher`.
- Plans start as `drafting` and change status only by the user's choice.
- DECISION lines in the progress logs, with date and time, one grep away.
- Experiments (`/new-plan exp`): `experiment/run.sh` as the one entry point, `RESULTS.md` with review markers, a short `analysis.qmd` (R by default), and a close check in `progress`.
- `project-refresher` reads the logs first, and shows the last run and write-up state for experiments.
- `plans/README.md` carries a `Workflow version:` line so `/setup-workflow` can offer updates.
