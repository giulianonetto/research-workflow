# Plan: Build in runs that stop where the plan says, with lighter build rules (#5)

**Started:** 2026-11-18 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#5](https://github.com/giulianonetto/research-workflow/issues/5) · **Branch:** `issue-5-build-runs`

## Goal
`/implement-next` builds several steps in one run and stops only where the plan says, or when something comes up. The stops are agreed when the plan is finalized, so Claude never decides alone that a step is safe. The build rules match what a build really needs: a full review only where code runs, short log entries, a push and a ticked box after each step, one folder-log entry per PR, and no parallel builds unless the user asks.

Out of scope: clearing done tasks and old log entries at a release ([#3](https://github.com/giulianonetto/research-workflow/issues/3)); changes to experiments (frozen until the first real one); the harness permission for `git push` (a Claude Code setting, not a workflow rule).

Source: building #2 (2026-11-18) and the talk after it, in this session and in a second chat on stops (its proposal was pasted here).

## Where things are now
- Version 0.2.0. `/implement-next` has `disable-model-invocation: true` and builds one step (`skills/implement-next/SKILL.md`, 28 lines).
- **Parallel builds:** `/implement-next` step 4 lets big steps that share no files run at the same time, one agent per worktree, at most 2-3 (`skills/implement-next/SKILL.md:17`, `:22`). Never used.
- **Review:** `PLANS-README.md` Review (`skills/setup-workflow/PLANS-README.md:36-43`) asks for the full review (`/code-review`, Spec, Research, Style) before every step commit and every PR. In #2, steps were checked against the plan by hand; one full review of the branch before the PR found 10 issues.
- **Logs:** `/progress` step 3 (`skills/progress/SKILL.md:26-27`) asks for "what changed and its evidence" with no length limit; #2's step entries were 3-5 bullets, mostly repeating the commit. The folder log gets an entry when the task's PR is opened and another when it is merged (`skills/progress/SKILL.md:11`).
- **Push:** `/implement-next` says "Ask before pushing" (`skills/implement-next/SKILL.md:24`); the issue box is ticked at the commit, even when the commit is only local.
- **Stops:** none. `/finalize-plan` readiness check has Goal, Open questions, Ground, Steps, Decisions, Issue, Build shape (`skills/finalize-plan/SKILL.md:15-22`).
- The `PLAN.md` skeleton is in `skills/new-plan/SKILL.md` (shows a big step with sub-steps, `:34-35`).
- `Workflow version:` lines: `skills/setup-workflow/PLANS-README.md:3` and this repo's `plans/README.md:3`. Checks: `tests/check_skills.py`, `tests/check_scripts.sh`.

## Steps
### 1. Rules file (`setup-workflow/PLANS-README.md` and this repo's `plans/README.md`)
- **Stops:** a step that needs the user ends with `- **Stop:** <why>`. Every other step means "Claude may go on". A step needs a stop when: the user must judge the result (numbers, plots, a method choice that tests can't catch); it needs a user-run check; it is hard to undo (deletes, migrations, a push or merge into `main`); or the plan leaves a design choice open. A Stop always means after its step: build it, commit, push, report, then stop. A step that must not start without the user puts its Stop on the step before, and the why names the next step (the first step of a run is covered by the question at the start of the run). The PR into `main` is always a stop: the last step always carries `- **Stop:** review the branch and open the PR into main`, so every finalized plan has at least one Stop line.
- **Runs:** `/implement-next` builds up to the next stop, at most 5 steps per run, because the context fills up. The limit is written as a number in `plans/README.md`, so a project can change it there. A big step counts as one step. It stops early when a test fails and the fix is not clear, the review finds something to ask about, the "Still needed?" check fires, the merge rule says to ask before merging a big step's PR, or a decision comes up that the plan does not cover. A plan with no stop markers (made before this version): ask before each step (a finalized plan always has a Stop on its last step, so no Stop lines means an old plan).
- **Review:** full review (`/code-review` for bugs, then Spec, Research, Style) for a step that changes a file that runs (code, scripts, pipelines, tests); a Spec check only for a step that changes only text (docs, plans, comments). Before every PR: always the full review, on the whole branch. Skip a heading that does not apply.
- **Push:** after each step commit, push the task branch and tick the step's box, so GitHub is at most one step behind and a ticked box is always on GitHub. Pushing the task branch needs no question; pushing or merging into `main` does. A project's `CLAUDE.md` can override this.
- **No parallel builds** unless the user asks.
- **Logs:** a step's entry is the commit plus only what the diff can't show (deviations from the plan, what was left for later), at most 2 bullets, plus DECISION lines. The folder log gets one entry per task PR, written when it is merged; while it is open, only the Current state names it.
- **Stop:** read the new rules in `plans/README.md` before steps 2-5 copy them into the skills.

### 2. `/finalize-plan` proposes the stops
- Readiness check gains **Stops:** Claude proposes a `**Stop:**` line for each step that meets the rule in step 1, always a Stop on the last step (the PR into `main`); the user confirms or changes them, and they are written into `PLAN.md`.

### 3. `/implement-next` builds a run
- Keeps `disable-model-invocation: true` (only the user starts a build). The name stays. The frontmatter description changes to say it builds the next steps of a task's `PLAN.md`, up to the next stop.
- At the start, asks once: "I will build steps 3, 4 and 5, then stop after step 5 (Stop: look at the plots). OK, or one step at a time?"
- Each step still gets its review (per step 1), one commit with its log update, a push and a ticked box.
- Stops at the stop, at the run limit, or early (step 1 list). At the end, one summary: each step, its review result, and every decision Claude made alone.
- Drop the parallel rule (step 4 and the "Parallel big steps" bullet), and "Ask before pushing".

### 4. `/progress` follows the new log rules
- Step entries: at most 2 bullets plus DECISION lines.
- Folder log: one entry per task PR, at the merge; opening the PR only updates the Current state.

### 5. `/new-plan` skeleton shows a stop
- The `PLAN.md` skeleton gets a step with a `- **Stop:** <why>` line.
- Step 5 drops "(ask before pushing)": the first push of the task branch needs no question either. `/setup-workflow`'s "Don't push" stays (that commit is on `main`).

### 6. Docs, checks, version
- `README.md` (its command-table line too), `docs/examples.html` (workflow 3: a run with a stop; workflows 2 and 3: no question before the first push; the short version), `docs/workflow.html` (the Build card), this repo's `CLAUDE.md` if needed. `README.md` gets one line on allowing `git push` in Claude Code's own settings, so pushes to the task branch don't stop at a prompt; `/setup-workflow` does not change those settings.
- `/setup-workflow`: upgrading from 0.2.x says that existing plans have no stops, so `/implement-next` asks before each step until `/finalize-plan` or the user adds them.
- `check_skills.py`: nothing new expected; add to `STALE` any phrase that step 3 removes, if one fits.
- Version 0.3.0: bump `plugin.json` and both `Workflow version:` lines; add a CHANGELOG section.
- **Stop:** review the branch and open the PR into main.

## Done when
Both checks pass, `PLANS-README.md` has the stop, run, review, push and log rules, and no skill or template still allows parallel builds without the user asking or asks before pushing the task branch.

## Open questions
None.
