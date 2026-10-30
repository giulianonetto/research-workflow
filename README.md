# research-workflow

Claude skills for research repos: plans that start as drafts and grow over many days, a progress log that every session starts from, major decisions one grep away, and experiments that close with a written result and a short notebook to continue by hand.

**Step-by-step examples:** [docs/examples.html](docs/examples.html) (new repo, new task, existing issue, continuing a draft, running an experiment).

## Commands

| When | Command |
|---|---|
| Once per repo | `/setup-workflow` |
| Start of a session | `/project-refresher` |
| New task / experiment | `/new-plan` / `/new-plan exp` |
| Plan text should change (any time, any reason) | `/update-plan` |
| Plan ready to build (status changes only after your yes) | `/finalize-plan` |
| Write up an experiment (as many rounds as you like) | `/write-results` |
| Check something by hand | ask for a sandbox (`sandbox`) |
| End of a session | `progress` (or "log progress") |

All past decisions: `grep -rn '^- \*\*DECISION' PROGRESS.md plans/*/PROGRESS.md`

## What it writes in a project

```
CLAUDE.md, README.md        + a section on the workflow
PROGRESS.md                 the folder log: what is active, one section per session
plans/README.md             format rules, DECISION lines, statuses (and the workflow version)
plans/EXPERIMENTS.md        rules for experiment tasks
plans/<task>/PLAN.md        the plan (Goal, or Objectives for an experiment)
plans/<task>/PROGRESS.md    the task log: work, DECISION lines, Next
plans/<task>/sandbox/       code for you to run and inspect by hand
plans/<task>/experiment/    experiments: code, with run.sh as the one entry point
plans/<task>/RESULTS.md     experiments: answers, methods, results, discussion, appendix
plans/<task>/analysis.qmd   experiments: short walkthrough to continue by hand
```

## Install

**Claude Code** (as a plugin): add this repo as a plugin marketplace and install `research-workflow` from it (see the Claude Code docs on plugins for the exact commands). Skills from a plugin may show with a `research-workflow:` prefix.

**claude.ai**: download the zips from the [latest release](../../releases/latest) (or run `scripts/build-zips.sh`), then upload each one in Settings → Capabilities → Skills, replacing older versions.

**In each project**: run `/setup-workflow`. In a project set up with an older version, run it again: it shows what changed and updates only with your agreement.

## Dependencies

Everything works on its own. These optional commands come from the [mattpocock-skills](https://github.com/mattpocock/skills) plugin, and the workflow mentions them where they help: `/grilling` and `/grill-with-docs` (stress-test an idea), `/domain-modeling` (glossary and ADRs), `/to-tickets` and `/implement` (multi-session builds), `/code-review`. Opening PRs uses `gh pr create`.

## Development

This repo uses its own workflow: see [PROGRESS.md](PROGRESS.md) and [plans/](plans/). Every design decision is a DECISION line.

- `python3 tests/check_skills.py`: frontmatter, plugin manifest, versions, local links, stale names.
- `bash tests/check_scripts.sh`: runs the `run.sh` template and the refresher on a fake project.
- Both run on every push (GitHub Actions). Pushing a tag `vX.Y.Z` builds the zips and attaches them to a release.

Releasing: bump `version` in `.claude-plugin/plugin.json` and the `Workflow version:` line in `skills/setup-workflow/PLANS-README.md` (the checks fail if they differ), add a `## X.Y.Z` section to [CHANGELOG.md](CHANGELOG.md), then tag.
