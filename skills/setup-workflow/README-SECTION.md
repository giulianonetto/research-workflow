## Development workflow

Each task is a GitHub issue, a branch and a folder `plans/<task>/` with `PLAN.md` (the plan) and `PROGRESS.md` (the log of work and decisions). All rules: [`plans/README.md`](plans/README.md).

```text
issue ─▶ /new-plan ─▶ brainstorm sessions ─▶ /finalize-plan ─▶ /implement-next in runs
           drafting    (/grill-plan)              planned          in-progress
      ─▶ PR into main (you merge) ─▶ /progress (merged / done)

every session:  /project-refresher at the start ─▶ work (logged in the same commit)
at any point:   change the plan (any reason) · /sandbox (you run it and look) · /grill-plan on a hard point
```

Experiments (try something out, end in an answer) are tasks too: `/new-plan exp`; rules in [`plans/EXPERIMENTS.md`](plans/EXPERIMENTS.md).
