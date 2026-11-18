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

### 1. Claude Desktop (easiest: works everywhere you sign in)

1. In the Claude Desktop app (or on claude.ai), open **Customize → Plugins**.
2. Click **Add → Add marketplace** and enter `giulianonetto/research-workflow`. If asked, connect GitHub and give the Claude GitHub App access to this repo.
3. Add the **research-workflow** plugin.

That's it: the skills now work in chat, Cowork and Claude Code, on any computer where you are signed in. To get new versions, turn on **Sync automatically** for the marketplace (or click **Check for updates**).

### 2. Claude Code only (a machine where you are not signed in to your claude.ai account)

Once per machine, in your shell:

```bash
gh auth login && gh auth setup-git     # the repo is private: git needs your GitHub login
claude plugin install research-workflow --marketplace giulianonetto/research-workflow
```

Update later with `claude plugin update research-workflow@research-workflow`.

Use only one of the two on the same machine; with both, every command appears twice.

### In each project

Open Claude in the project folder and run `/setup-workflow` (in Claude Code, plugin commands carry the plugin's name: `/research-workflow:setup-workflow`). In a project set up with an older version, run it again: it shows what changed and updates only with your agreement.

## Dependencies

Everything works on its own. These optional commands come from the [mattpocock-skills](https://github.com/mattpocock/skills) plugin, and the workflow mentions them where they help: `/grilling` and `/grill-with-docs` (stress-test an idea), `/domain-modeling` (glossary and ADRs), `/to-tickets` and `/implement` (multi-session builds), `/code-review`. Opening PRs uses `gh pr create`.

## Credits

`/grill-plan` and the Spec part of the review rules are adapted from Matt Pocock's [mattpocock-skills](https://github.com/mattpocock/skills) (MIT License); see [NOTICE](NOTICE).

## Development

This repo uses its own workflow: see [PROGRESS.md](PROGRESS.md) and [plans/](plans/). Every design decision is a DECISION line.

- `python3 tests/check_skills.py`: frontmatter, plugin manifest, versions, local links, stale names.
- `bash tests/check_scripts.sh`: runs the `run.sh` template and the refresher on a fake project.
- Both run on every push (GitHub Actions). Pushing a tag `vX.Y.Z` builds the zips and attaches them to a release.

Releasing: bump `version` in `.claude-plugin/plugin.json` and the `Workflow version:` line in `skills/setup-workflow/PLANS-README.md` (the checks fail if they differ), add a `## X.Y.Z` section to [CHANGELOG.md](CHANGELOG.md), then tag.
