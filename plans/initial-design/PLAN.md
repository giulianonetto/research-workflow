# Plan: initial design of the workflow

**Started:** 2026-10-29 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** none · **Branch:** `main`

## Goal
A set of Claude skills for research repos: plans that grow as drafts over many days, explicit control over status, a progress log every session starts from, major decisions one grep away, and experiments that close with a written result. Out of scope here: packaging for other agents than Claude.

## Where things are now
- Started from five skills (`setup-workflow`, `to-plan`, `progress`, `sandbox`, `project-refresher`) reviewed on 2026-10-29.
- Depends optionally on the mattpocock-skills plugin.

## Steps
### 1. Fix the review findings
- Contradictions between skills (ticking PLAN.md, status words, CONTEXT.md vs GLOSSARY.md, branch creation, header format).
### 2. Replace `to-plan` with draft-friendly commands
- `/new-plan`, `/update-plan`, `/finalize-plan`; DECISION lines; folder-log rule.
### 3. Experiments
- `Kind: experiment`, `plans/EXPERIMENTS.md`, `run.sh`, `RESULTS.md`, `analysis.qmd`, close check, `/write-results`, refresher view.
### 4. Repo
- Plugin manifest, checks, release with zips, examples page, version line.

## Open questions
(none)
