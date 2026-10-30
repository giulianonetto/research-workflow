---
name: setup-workflow
description: Set up a folder for the plans/PROGRESS workflow (task folders, progress logs with DECISION lines, /new-plan, /update-plan, /finalize-plan, sandbox, conservative glossary and ADRs), including the small config the mattpocock skills read.
disable-model-invocation: true
---

Scaffold the files the `progress`, `new-plan`, `update-plan`, `finalize-plan` and `sandbox` skills rely on, plus the config the mattpocock skills read (`/to-tickets` needs to know the issue tracker). `/setup-matt-pocock-skills` is not needed; run it only if the user wants `/triage` and its labels. Explore, show the drafts, confirm, then write. Never overwrite what exists: add to it, and leave the user's own text alone. The one exception: files or sections written by an older version of this workflow (`plans/README.md`, `plans/EXPERIMENTS.md`, the CLAUDE.md `## Planning and progress` section, the README `## Development workflow` section, mentions of `/to-plan`). Show what differs and replace them only if the user agrees; keep the task table and any lines the user added. The `Workflow version:` line in `plans/README.md` tells which version wrote them: if it is missing or older than the one in [PLANS-README.md](PLANS-README.md), say so first.

## Steps

1. **Explore.** Is it a git repo, with a GitHub remote (`git remote -v`)? Do these exist: `CLAUDE.md` (and a `## Agent skills` block), `README.md`, `PROGRESS.md`, `plans/README.md`, `plans/EXPERIMENTS.md`, `docs/agents/`, `GLOSSARY.md`, `docs/adr/`, `.gitignore`? Is `tmp/` ignored (`git check-ignore -q tmp/x`)? Is `docs/` ignored (a pkgdown or site rule)?

2. **Ask the few facts the templates need**, recommending answers from step 1:
   - one line on what the project is;
   - its main language and tools (R / Python, Nextflow / Snakemake, Slurm);
   - where issues live: GitHub Issues on `<owner/repo>` (default when there is a GitHub remote), or none.

3. **Draft and show** (the templates are in this folder; fill the `<...>` parts):
   - `plans/EXPERIMENTS.md` from [EXPERIMENTS.md](EXPERIMENTS.md), if missing (the rules for experiment tasks).
   - `plans/README.md` from [PLANS-README.md](PLANS-README.md), with an empty task table. If it already exists from an older version of this workflow, show what differs (commands, DECISION lines, header line, status rules) and update it only if the user agrees; keep its task table.
   - `PROGRESS.md` (if missing): `# Progress log`, a `## Current state (updated <date>)` block with one bullet `- **Now:** no active task`, the times line from the template, and a first dated entry `## <date>: workflow set up`.
   - `CLAUDE.md`: the two sections in [CLAUDE-SECTION.md](CLAUDE-SECTION.md). If a `## Agent skills` block already exists (from `/setup-matt-pocock-skills`), keep it and only add the Domain docs override sentence to it.
   - `docs/agents/domain.md`: if missing, from [DOMAIN.md](DOMAIN.md); if it exists, insert that file's `## Glossary and ADRs` section right before its `## File structure` heading (or at the end).
   - `README.md`: the section in [README-SECTION.md](README-SECTION.md), at the end. Without an issue tracker, drop the `/to-tickets` branch and say "a task" instead of "a GitHub issue".
   - `.gitignore`: `tmp/` if not ignored (experiments keep big outputs under `tmp/experiments/` by default); Quarto render output: `.quarto/`, `plans/*/analysis_files/`, `plans/*/analysis.html`. If `docs/` is ignored, git can't un-ignore anything inside it, so the existing rule must change to `docs/*`, followed by `!docs/agents/` and `!docs/adr/`. This edits the user's own line: show it separately and ask before making it.

   Iterate until the user approves.

4. **Write and commit** on the current branch (one commit, `workflow: plans/PROGRESS setup`). Don't push. If the folder is not a git repo, ask whether to `git init`; if not, write the files and skip the commit (and the `.gitignore` step). `GLOSSARY.md` and `docs/adr/` are created later, when the first term or decision is agreed.

5. **Done.** Tell the user the next step: open an issue (if any tracker), then `/new-plan` as soon as the idea is worth tracking.
