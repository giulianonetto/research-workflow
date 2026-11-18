---
name: write-results
description: Write or revise an experiment's RESULTS.md and analysis.qmd - a first draft, one section, an interpretation, or changes after the user's review. Run it as often as needed; tracks which sections the user has reviewed; never changes the status.
disable-model-invocation: true
---

For experiment tasks (`**Kind:** experiment`). Writing up is iterative: draft, review, interpret, review again, in any order. This one command covers every round. Closing is not here: when every section is reviewed, the close check in `progress` ("mark done") finishes the experiment.

If the folder has no `plans/EXPERIMENTS.md`, tell the user to run `/setup-workflow` first and stop. Find the task from the branch name or the folder's Current state; if that is not clear, ask. If it is not an experiment, say so and stop.

## What to do this time

From the words after the command, or what the user says:
- nothing → **update the whole draft**: write missing sections, and update sections whose numbers changed since the last write (newer files in `results/`, or a newer run in `last-run.txt`);
- a section or objective (`/write-results results 2`, `/write-results methods`) → only that;
- `interpret` → propose the Discussion and conclusion;
- `analysis` → only `analysis.qmd`;
- review comments ("Methods is fine", "in Results 1 say X") → apply them, and mark what the user reviewed.

## Rules

- **Numbers come from evidence.** Every number, table and figure comes from a file in `results/` or `$OUT`, or from a logged run; name the file. Never invent, recompute in your head, or round beyond the source. If something the write-up needs is not produced by any `run.sh` stage, say so and ask: add a stage, or mark it "by hand" in the Appendix.
- **Interpretation is the user's.** Interpretation goes only in Discussion and conclusion. Propose it plainly, as a proposal; the wording stays a draft until the user reviews it.
- **Review markers.** Every section you write or change gets `<!-- unreviewed -->` on the line under its heading. Remove it only when the user says that section is reviewed (or ok). The close check fails while any marker is left.
- **Keep the user's own text.** Before writing, check `git diff` on `RESULTS.md` and `analysis.qmd` for hand edits since the last commit; never rewrite them unless asked. A section the user edited by hand: ask once whether it counts as reviewed.

## Steps

1. **Read.** `plans/EXPERIMENTS.md` (the RESULTS.md template and rules), the objectives in `PLAN.md`, the DECISION lines and recent entries in `PROGRESS.md`, the current `RESULTS.md` and `analysis.qmd`, the stages in `experiment/run.sh`, the files in `results/`, and the run history (`$OUT/run-info.log`, or `tmp/experiments/<task>/last-run.txt` at the repo root, which names `OUT`).

2. **Write what this round asks for.** Following the template:
   - **Answers:** high level, one per objective; changed or dropped objectives with their DECISION dates.
   - **Methods:** brief; data, what was run, key settings.
   - **Results:** detailed, per specific objective, with the figures and tables from `results/` (relative links) and their numbers.
   - **Discussion and conclusion:** very short interpretation, then the answer to the overall objective restated formally.
   - **Appendix:** every path with what it is, which stage made it, whether it is in git; then provenance (commit, environment, data, seeds, job IDs) from the run history.
   - **`analysis.qmd`:** the three parts (load the main objects, one or two main results, "continue from here"). If R/Python and Quarto are available, run its setup chunk; otherwise say it was not run.

3. **Show the round.** List the sections changed, the sections still `unreviewed`, and the open items (numbers without a source, objectives without an answer). Apply the user's comments in the same session, as many rounds as they like.

4. **Log it.** Run the `progress` skill: a short task-log note (`results: drafted Methods, Results 1; reviewed Answers`), and a DECISION line when the write-up settled something (for example, the answer to the overall objective). Commit: `results: <short summary>`.

5. **Next.** If sections are still unreviewed, name them. When none are left, tell the user: "Ready to close: tell `progress` to mark it done."
