# research-workflow

**Claude skills for research repos.** You plan with Claude over days, and every session picks up where the last one stopped. Claude builds the plan step by step and stops where you said you want to look.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/flow-dark.svg">
  <img src="docs/img/flow-light.svg" alt="The life of a task: start a plan, shape it, finalize it, build it in runs, close it. Every session starts with /project-refresher and ends with /progress.">
</picture>

## Why use it

- **Pick up where you left off**, even after weeks.
- **Keep every decision**, with its reason, one `grep` away.
- **Decide where Claude stops.** Between stops, it builds alone.

## How a build runs

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/runs-dark.svg">
  <img src="docs/img/runs-light.svg" alt="A build in runs: /implement-next builds steps 1 and 2, then stops so you can look at the plots; run again, it builds steps 3 to 6 and stops for the review and the PR into main.">
</picture>

Each `/implement-next` asks once, then builds up to the next **Stop** in the plan (at most 5 steps). It also stops early if a test fails or a question comes up that the plan does not answer.

## Get started

1. **Install** in the Claude Desktop app: **Customize → Plugins → Add → Add marketplace**, enter `giulianonetto/research-workflow`, then add the **research-workflow** plugin. (Other ways below.)
2. **In your project** (a git repo with a GitHub remote): run `/setup-workflow`.
3. **Say an idea**, then `/new-plan`.

## Commands

| When | Command |
|---|---|
| Start of a session: "where was I? what is next?" | `/project-refresher` |
| All tasks with their status | `/project-refresher tasks` |
| A new task | `/new-plan` |
| Hard questions about a draft plan | `/grill-plan` |
| The plan is ready to build | `/finalize-plan` |
| Build up to the next stop | `/implement-next` |
| Check something by hand | `/sandbox` |
| Log work, change a status | `/progress` (or "log progress") |

The plan can change at any time: just say what to change. All rules live in one file in your project, `plans/README.md`. All past decisions: `grep -rn '^- \*\*DECISION' PROGRESS.md plans/*/PROGRESS.md`

More: [the workflow on one page](docs/workflow.html) and [step-by-step examples](docs/examples.html) (new repo, new task, existing issue, continuing a draft). Download them and open them in a browser.

<details>
<summary><b>What it writes in a project</b></summary>

```
CLAUDE.md, README.md        + a short section on the workflow
PROGRESS.md                 the folder log: what is active, status changes, PRs, releases
plans/README.md             all the rules: build, issues, review, plan changes, logs, statuses
plans/<task>/PLAN.md        the plan: Goal, steps, stops
plans/<task>/PROGRESS.md    the task log: work, DECISION lines, Next
plans/<task>/sandbox/       code for you to run and inspect by hand
```

</details>

<details>
<summary><b>Install: all the ways, and updates</b></summary>

**Claude Desktop** (easiest: works everywhere you sign in)

1. In the Claude Desktop app (or on claude.ai), open **Customize → Plugins**.
2. Click **Add → Add marketplace** and enter `giulianonetto/research-workflow`. If asked, connect GitHub and give the Claude GitHub App access to this repo.
3. Add the **research-workflow** plugin.

The skills then work in chat, Cowork and Claude Code, on any computer where you are signed in. To get new versions, turn on **Sync automatically** for the marketplace (or click **Check for updates**).

**Claude Code only** (a machine where you are not signed in to your claude.ai account). Once per machine, in your shell:

```bash
gh auth login && gh auth setup-git     # the repo is private: git needs your GitHub login
claude plugin install research-workflow --marketplace giulianonetto/research-workflow
```

Update later with `claude plugin update research-workflow@research-workflow`. Use only one of the two on the same machine; with both, every command appears twice.

**In each project**, run `/setup-workflow` (in Claude Code, plugin commands carry the plugin's name: `/research-workflow:setup-workflow`). In a project set up with an older version, run it again: it shows what changed and updates only with your agreement.

**Pushes:** Claude pushes the task branch after each step. To skip the permission prompt each time, allow `git push` in Claude Code's own settings (`/permissions`); the workflow does not change them.

</details>

## Credits

`/grill-plan` and the Spec part of the review rules are adapted from Matt Pocock's [mattpocock-skills](https://github.com/mattpocock/skills) (MIT License); see [NOTICE](NOTICE).

## Development

This repo uses its own workflow: see [PROGRESS.md](PROGRESS.md) and [plans/](plans/). Every design decision is a DECISION line.

- `python3 tests/check_skills.py`: frontmatter, plugin manifest, versions, local links, stale names.
- `bash tests/check_scripts.sh`: runs the `run.sh` template and the refresher on a fake project.
- `python3 docs/figures.py`: redraws the README figures in `docs/img/` (light and dark).
- Both checks run on every push (GitHub Actions). Pushing a tag `vX.Y.Z` builds the zips and attaches them to a release.

Releasing: bump `version` in `.claude-plugin/plugin.json` and the `Workflow version:` line in `skills/setup-workflow/PLANS-README.md` (the checks fail if they differ), add a `## X.Y.Z` section to [CHANGELOG.md](CHANGELOG.md), then tag.
