# Experiments

An experiment is a task that tries something out and ends in an answer: is it worth putting into the main code, or how does it behave? It is messy by design. The rules apply only at its edges: the objectives before it runs, the result package when it closes, and its code kept out of the main code. Inside `experiment/`, anything goes.

It is a normal task in every other way (`/new-plan`, `/finalize-plan`, `/progress`, the plan-change rules in `plans/README.md`, same statuses), with `**Kind:** experiment` in its header line.

## Folder

```
plans/<task>/
├── PLAN.md        Overall objective · Specific objectives · Where things are now · Steps · Open questions
├── PROGRESS.md    log + DECISION lines
├── experiment/    the code, any structure; run.sh is its one entry point
├── results/       small figures and tables, committed
├── RESULTS.md     the answers and the record (template below)
└── analysis.qmd   short walkthrough to continue by hand, committed
```

Big outputs live outside git, under `$OUT` (default `tmp/experiments/<task>/` at the repo root; on the cluster, set `OUT` to a scratch path).

## Rules

1. **Objectives first.** `PLAN.md` has one **Overall objective** and one or more **Specific objectives**, each saying how it will be answered (which output, which `run.sh` stage). Objectives may change under the plan-change rules in `plans/README.md`; `RESULTS.md` answers the final ones and lists the changed or dropped ones.
2. **One entry point.** `experiment/run.sh` is the only documented way to produce `results/` and the big outputs. Its stages are bash functions and can call anything (`Rscript`, `python`, `nextflow run`, `targets::tar_make()`, `make`, a binary, `sbatch`). While exploring you may run things directly; at close, every file in `results/` and every number in `RESULTS.md` comes from a stage, or is marked "by hand" in the Appendix. Each run appends the commit, uncommitted changes, host and arguments to `$OUT/run-info.log`, and keeps a copy of the latest in `tmp/experiments/<task>/last-run.txt` at the repo root (always local, even when `OUT` is elsewhere).
3. **Out of the main code.** Experiment code calls the project's code but doesn't change it. A change the experiment needs in the main code is its own commit, named in `PROGRESS.md`. This is what lets the branch always merge.
4. **Always merge.** Whatever the answer, the task folder goes to `main` (a PR with the folder only is fine), so the record survives.
5. **"No" is `done`.** An experiment that answered its objective is `done`, whatever the answer. `dropped` is for an experiment stopped without an answer. Adopting the result in the main code is usually a new task (`/new-plan`), linked to the final DECISION line.
6. **`analysis.qmd` is minimal and committed.** R by default; Python (or another language Quarto runs) when the user asks. The experiment code itself can be anything. Three parts: load the main objects, show one or two main results, "continue from here". It points to the RESULTS.md Appendix for what is where; it is not a re-run of the experiment. Play in it freely; commit or `git restore` the changes.

## RESULTS.md

```
# Results: <title> (#<N>)

**Status:** <done | dropped> · **Plan:** [PLAN.md](PLAN.md) · **Analysis:** [analysis.qmd](analysis.qmd) · **Closed:** <date>

## Answers
**Overall objective:** <one line>. <the answer in one or two sentences>
1. <specific objective>: <short answer>
(Changed or dropped objectives: <list, with DECISION dates>, or "none".)

## Methods
<brief: data, what was run, key settings>

## Results
<detailed, per specific objective: figures and tables from results/, with numbers>

## Discussion and conclusion
<very short interpretation; then the answer to the overall objective restated formally>

## Appendix: what is where
| Path | What | Made by | In git |
|---|---|---|---|
| experiment/run.sh | entry point | | yes |
| results/<file> | <what it shows> | `run.sh <stage>` or by hand | yes |
| $OUT/<path> | <big output> | `run.sh <stage>` | no |

Provenance: commit <hash> (from `$OUT/run-info.log`), environment (<renv.lock / pixi.toml / container>), data (<version or path>), seeds, Slurm job IDs.
```

A `dropped` experiment needs only a short `RESULTS.md`: Answers ("stopped without an answer"), what was tried and seen, why it stopped, and the Appendix if anything was produced. No `analysis.qmd`.

## Writing up

`/write-results` writes and revises `RESULTS.md` and `analysis.qmd`, as often as needed: a first draft, one section, an interpretation (`/write-results interpret`), or the user's review comments. Every section it writes or changes is marked `<!-- unreviewed -->` under its heading until the user says it is reviewed. Numbers come only from files in `results/` or `$OUT`; interpretation goes only in Discussion and conclusion.

## Close check

Before an experiment is set to `done`, `/progress` checks, and lists what is missing:
- `RESULTS.md` has the five sections, filled (no `<...>` left), every section reviewed (no `<!-- unreviewed -->` left), with the Appendix covering every file in `results/`;
- `experiment/run.sh` parses (`bash -n`) and lists its stages when run with no arguments (nothing is re-run);
- `analysis.qmd` exists and its setup chunk runs, or says clearly which `run.sh` stage recreates missing objects;
- the final DECISION line states the answer to the overall objective.

The status changes only when everything passes, or when the user explicitly accepts the gaps (named in the log).
