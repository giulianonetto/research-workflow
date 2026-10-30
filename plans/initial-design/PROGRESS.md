# Progress: initial design of the workflow
**Status:** done · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** none

## Current state (updated 2026-10-30)
- Done: version 0.1.0, eight skills, checks and release workflow in place.
- Not yet tried on a real project; the R `analysis.qmd` template has not been rendered.

## 2026-10-30: experiments and the repo
Experiments became a kind of task, with `/write-results` for the write-up; the repo was set up.
### Next
- Use it on one real project and one real experiment; open an issue for every rough edge.
### 10:30: repo
- **DECISION 2026-10-30 10:27:** drop `/pr` and `/retro` from the workflow, because they are not published in the mattpocock-skills plugin (only drafts); PRs use `gh pr create`
- **DECISION 2026-10-30 10:27:** keep mattpocock-skills an optional dependency, not copied into this repo, because the core workflow works without it and copies would drift
- **DECISION 2026-10-30 10:27:** add a `Workflow version:` line to `plans/README.md`, because projects keep copies of the templates and `/setup-workflow` needs to know which version wrote them
- Checks: `tests/check_skills.py` (frontmatter, manifest, versions, links, stale names) and `tests/check_scripts.sh` (run.sh and refresher on a fake project); both pass.
### 10:16: write-up
- **DECISION 2026-10-30 10:16:** one `/write-results` command for every write-up round (draft, section, interpret, review comments), with `<!-- unreviewed -->` markers per section, because more commands would add little and the markers give explicit review control
- **DECISION 2026-10-30 10:16:** `run.sh` also writes `tmp/experiments/<task>/last-run.txt`, because the refresher must find the last run even when `OUT` is on scratch
### 10:08: experiment details
- **DECISION 2026-10-30 10:08:** `/new-plan` makes a normal task unless told `exp`; `analysis.qmd` is R by default, and the experiment itself can use any tool
- **DECISION 2026-10-30 10:08:** outputs go to git or not by folder (`$RES` committed, `$OUT` not), not by size, because the stage author knows what RESULTS.md shows
### 09:56: experiment design
- **DECISION 2026-10-30 09:56:** experiments are tasks with `Kind: experiment`, not a new status or command family, because the workflow should stay small
- **DECISION 2026-10-30 09:56:** one committed `analysis.qmd` (Quarto, plain text, R or Python), no gitignored copy, because a gitignored file is not part of the record
- **DECISION 2026-10-30 09:56:** provenance goes in a RESULTS.md Appendix ("what is where"); no exploratory/confirmatory labels, because that judgment belongs to the user, not the workflow
- **DECISION 2026-10-30 09:56:** `experiment/run.sh` (bash) is the one entry point, because bash can call R, Python, Nextflow, targets, Slurm on any machine; at close it is checked, not re-run
- **DECISION 2026-10-30 09:56:** the experiment close check runs in `progress` ("mark done"), not in `/finalize-plan`, because results do not exist when a plan is finalized

## 2026-10-29: from review to draft-friendly plans
Reviewed the five original skills, fixed the contradictions, then redesigned planning around drafts.
### Next
- Add experiments.
### 22:36: logs
- **DECISION 2026-10-29 22:36:** the folder log gets one section per session plus status changes and PRs; plan updates alone go only in the task log, so the folder log stays readable
### 22:31: update-plan
- **DECISION 2026-10-29 22:31:** `/update-plan` runs at any time for any reason; `## Changes` lines only for real changes after `planned`; adding an open question to an agreed plan asks whether to go back to `drafting`
### 22:27: decisions
- **DECISION 2026-10-29 22:27:** no NOTES.md: the brainstorm record goes in PROGRESS.md, because the two overlapped
- **DECISION 2026-10-29 22:27:** major decisions are DECISION lines with date and time, logged whether or not they change PLAN.md, because grep shows only the line
### 22:17: commands
- **DECISION 2026-10-29 22:17:** split `/to-plan` into `/new-plan`, `/update-plan` and `/finalize-plan`, because one command with hidden modes did too many things
- **DECISION 2026-10-29 22:17:** a status changes only by the user's choice, never inferred
### 21:59: review fixes
- Fixed: ticking PLAN.md, status words, CONTEXT.md vs GLOSSARY.md, branch creation, revise-mode order, task header format, non-git setup, `docs/` gitignore rule, UTC times, refresher in subfolders and worktrees.
