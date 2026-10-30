## Development workflow

Each task is a GitHub issue, a branch and a folder `plans/<task>/` with `PLAN.md` (the spec) and `PROGRESS.md` (the log of work and decisions); the root `PROGRESS.md` says what is active. Rules: [`plans/README.md`](plans/README.md). `/grilling`, `/grill-with-docs`, `/to-tickets`, `/implement` and `/code-review` come from the mattpocock-skills plugin; everything else works without it.

```text
issue ─▶ /new-plan ─▶ brainstorm sessions ─▶ /finalize-plan ─┬─▶ build sessions
           drafting    (/update-plan any time)    planned      └─▶ /to-tickets ─▶ /implement per ticket
      ─▶ /code-review ─▶ PR (gh pr create) ─▶ progress (merged / done)

every session:  /project-refresher at the start ─▶ work ─▶ progress at the end
at any point:   /update-plan (any reason) · /sandbox (you run it and look) · /grilling on a hard point
```

1. **Issue:** every task starts from one.
2. **`/new-plan`:** as soon as the idea is worth tracking. Creates `plans/<task>/` with a draft `PLAN.md` (from the conversation or a draft you have) and `PROGRESS.md`. Status `drafting`.
3. **Brainstorm, over as many sessions and days as needed:** talk it through, use `/grilling` or `/grill-with-docs` on hard points, `/sandbox` to check things by hand. `/update-plan` whenever the plan should change. Every major decision, including options ruled out, is a DECISION line in the task's `PROGRESS.md`.
4. **`/finalize-plan`:** when you think it is ready. It shows the gaps; the status becomes `planned` only when you confirm. For a multi-session build, `/to-tickets plans/<task>/PLAN.md` here.
5. **Build, always in a fresh session:** `/clear`, then start from the task's `PROGRESS.md` (and `/implement #<n>` if there are tickets). End each session with the `progress` skill; the next session resumes from its **Next**.
6. **`/code-review`** against `main`, then open the PR (`gh pr create`, or ask Claude); its description says `Closes #<n>`.
7. **Close out:** progress logged as merged / done.

**Experiments** (try something out, end in an answer) are tasks too: `/new-plan exp`. They keep their code in `plans/<task>/experiment/` (entry point `run.sh`), are written up with `/write-results` (as often as needed, until you have reviewed every section), and close with `RESULTS.md` and a short `analysis.qmd` to continue by hand. Rules: [`plans/EXPERIMENTS.md`](plans/EXPERIMENTS.md).

Status changes only when you choose: `/new-plan`, `/finalize-plan`, the reopen question of `/update-plan`, or telling `progress` (paused, done, dropped…).

All past decisions: `grep -rn '^- \*\*DECISION' PROGRESS.md plans/*/PROGRESS.md`
