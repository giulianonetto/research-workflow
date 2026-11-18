---
name: setup-workflow
description: Set up a folder for the plans/PROGRESS workflow (task folders, progress logs with DECISION lines, plans/README.md as the one rules file, /new-plan, /finalize-plan, /implement-next, /sandbox, a small glossary). Needs a git repo with a GitHub remote.
disable-model-invocation: true
---

Scaffold the files the workflow's skills rely on. Explore, show the drafts, confirm, then write. Never overwrite what exists: add to it, and leave the user's own text alone. The one exception: files or sections written by an older version of this workflow (`plans/README.md`, `plans/EXPERIMENTS.md`, the CLAUDE.md `## Planning and progress` section, the README `## Development workflow` section, mentions of `/to-plan`). Show what differs and replace them only if the user agrees; keep any lines the user added. The `Workflow version:` line in `plans/README.md` tells which version wrote them: if it is missing or older than the one in [PLANS-README.md](PLANS-README.md), say so first.

## Steps

1. **Explore.** Is it a git repo with a GitHub remote (`git remote -v`)? GitHub is required: every task has an issue. If there is no GitHub remote, say so and stop; offer to create one (`gh repo create`) or to wait until the user adds it. Do these exist: `CLAUDE.md`, `README.md`, `PROGRESS.md`, `plans/README.md`, `plans/EXPERIMENTS.md`, `GLOSSARY.md`, `.gitignore`? Is `tmp/` ignored (`git check-ignore -q tmp/x`)?

2. **Ask the few facts the templates need**, recommending answers from step 1:
   - one line on what the project is;
   - its main language and tools (R / Python, Nextflow / Snakemake, Slurm).

3. **Draft and show** (the templates are in this folder; fill the `<...>` parts):
   - `plans/EXPERIMENTS.md` from [EXPERIMENTS.md](EXPERIMENTS.md), if missing (the rules for experiment tasks).
   - `plans/README.md` from [PLANS-README.md](PLANS-README.md). If it already exists from an older version of this workflow, show what differs (commands, rules, header line, statuses) and update it only if the user agrees.
   - **Upgrading from 0.1.x:** list what 0.2.0 changes in the project and change each only if the user agrees:
     - the status table in `plans/README.md` goes (the status lives only in each task's header line; `/project-refresher tasks` lists them); first check that each row matches its task header, and show any mismatch;
     - tasks with status `paused` (grep the task headers): the status no longer exists; propose `in-progress` with the reason in the task's Current state, or `dropped`;
     - `## Changes` sections in `PLAN.md` files: keep them as history, or turn each line into a DECISION line with the `(plan change)` tag in the task log;
     - `docs/agents/domain.md`, `docs/adr/` and the CLAUDE.md `## Agent skills` block: the glossary rules are now in `plans/README.md`; offer to delete `docs/agents/domain.md` and the block, keep `GLOSSARY.md`, and leave existing ADRs alone (link them from DECISION lines if the user wants);
     - an open task with no GitHub issue: offer to create one.
   - **Upgrading from 0.2.x or older:** say that existing plans have no Stop lines, so `/implement-next` asks before each step until they get them: from `/finalize-plan` for a plan still `drafting`, or from the user, who can ask to add them at any time (the stop rule is in `plans/README.md`, Build).
   - `PROGRESS.md` (if missing): `# Progress log`, a `## Current state (updated <date>)` block with one bullet `- **Now:** no active task`, the times line from the template, and a first dated entry `## <date>: workflow set up`.
   - `CLAUDE.md`: the section in [CLAUDE-SECTION.md](CLAUDE-SECTION.md).
   - `README.md`: the section in [README-SECTION.md](README-SECTION.md), at the end.
   - `.gitignore`: `tmp/` if not ignored (drafts of new plans and big experiment outputs live under `tmp/`); Quarto render output: `.quarto/`, `plans/*/analysis_files/`, `plans/*/analysis.html`.

   Iterate until the user approves.

4. **Write and commit** on the current branch (one commit, `workflow: plans/PROGRESS setup`). Don't push. `GLOSSARY.md` is created later, when the first term is agreed.

5. **Done.** Tell the user the next step: `/new-plan` as soon as an idea is worth tracking (it uses or creates the GitHub issue).
