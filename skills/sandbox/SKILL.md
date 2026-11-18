---
name: sandbox
description: Hand the user a ready-to-run sandbox to inspect something by hand (data to describe, an assumption to check, a config or params file to try). Use when a question needs the user's own eyes, while brainstorming a plan or after a build step, or when the user asks for code to run themselves.
---

In an experiment task, a question about the experiment's own results usually belongs in its `analysis.qmd`; use a sandbox entry for side questions.

A sandbox entry is for the **user's** inspection: they run it, look, and judge. Write it so it is easy to step through and change, not to deliver a verdict. Checks you can judge yourself from printed output are normal work: run them and log the evidence with `/progress`.

Code lives in `plans/<task>/sandbox/` (committed). Everything it writes goes to `tmp/sandbox/<task>/NN-<slug>/`, never to the project's real output folders. An entry belongs to a task; if no task is active, ask which one. Before the first entry in a folder, check that `tmp/` is ignored (`git check-ignore -q tmp/sandbox`); if not, add `tmp/` to `.gitignore` and say so.

## Steps

1. **Name the questions.** One sentence each, in the user's words. Take the next free number `NN` from `plans/<task>/sandbox/README.md`. Done when the user would recognise every question as theirs.

2. **Write the entry** in the project's main language, following its coding style (the folder's `CLAUDE.md`, the user's preferences):
   - One script `NN-<slug>.<ext>`, meant to be run section by section (R console, IPython, VS Code cells):
     - Header comment: the questions, the date, how to run it (interactively, or the command the project uses for its scripts), the output folder.
     - A setup section that loads the data once with the project's own code (import or source the real modules, read the real files), on the smallest case that answers the questions (one chromosome, a few samples, a small subset).
     - One section per question (a comment header per question, e.g. `# ---- <question> ----` or `# %% <question>`), each opening with a `Look at:` comment saying what to check and what would be surprising. Print tables, save plots to the output folder.
   - Only when the question needs the workflow manager or the cluster (Nextflow, Snakemake, Slurm…): a job script and/or a scratch config with every output path under `tmp/sandbox/<task>/NN-<slug>/`, plus the exact command in the header.

3. **Smoke-test it.** Run the setup section (or the whole entry on its smallest case) so the user's first run doesn't fail on a typo. If it only runs on the cluster, or the setup needs real compute (large data, a shared login node), don't run it: check that the code parses and the input paths exist, and say so.

4. **Index it.** Add a row to `plans/<task>/sandbox/README.md` (create it with this table if missing):

   | # | Date | Questions | Run | Findings |
   |---|---|---|---|---|

   Findings stay empty until the user reports back.

5. **Hand it over.** Give the user the file to open or the command to run, and what to look at first.

When the user reports what they saw: fill in **Findings**, then run `/progress` (with a DECISION line if the findings settled something). If they change what the plan should say, offer to change it under the plan-change rules in `plans/README.md`.
