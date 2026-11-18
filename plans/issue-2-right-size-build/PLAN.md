# Plan: Simplify the workflow and right-size the build (#2)

**Started:** 2026-11-17 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#2](https://github.com/giulianonetto/research-workflow/issues/2) · **Branch:** `issue-2-right-size-build`

## Goal
The workflow is simple for people: few commands, one rules file, logs that stay short. The build follows the plan's shape, so the GitHub structure can be read from `PLAN.md`: one branch per task, one commit per step, and a sub-issue only for a big step with sub-steps. Asking "what is next?" never starts work, and `/implement-next` follows fixed rules. GitHub is assumed throughout, and every task has an issue. No dependency on mattpocock-skills: the parts worth keeping are adapted into this plugin, with attribution.

Out of scope here: how a project runs its user-run checks (sbatch, containers, paths), which belongs in the project's own `CLAUDE.md` or docs; clearing done tasks and old log entries at a release ([#3](https://github.com/giulianonetto/research-workflow/issues/3)); changes to experiments (frozen until the first real one).

Sources: the review of a real project, 2026-11-16/17 (`real-project/tmp/skill-building/workflow-review-2026-11-16.md`, not in git), where a 5-step plan became 10 sub-issues; the workflow review of 2026-11-18 (`tmp/review-2026-11-18.md`, not in git).

## Where things are now
- 8 skills, version 0.1.1. `finalize-plan`, `new-plan`, `update-plan`, `write-results` and `setup-workflow` have `disable-model-invocation: true`; `progress`, `sandbox` and `project-refresher` do not.
- **The rules are written three times in each project:** `plans/README.md`, a `CLAUDE.md` section (`setup-workflow/CLAUDE-SECTION.md`, 9 bullets plus an `## Agent skills` block) and a `README.md` section (`setup-workflow/README-SECTION.md`, flow plus 7 steps). About 20 places name `/update-plan`.
- **Logs, in the real project:** the folder log (593 lines) is as long as the three task logs together; its Current state bullets are paragraphs. 57 of 343 commits only update logs.
- **Status** is kept twice (the `plans/README.md` table and the task header). Six statuses; `paused` was never used ("#26 on hold" stayed `in-progress`).
- **Plan changes:** `/update-plan` is mostly a rule (log decisions, `## Changes` once `planned`, reopen question, update tickets, only what the user decided, show first). `## Changes` was used twice in the real project, each time a copy of a DECISION line.
- **Build:** `finalize-plan` step 4 suggests `/to-tickets`. No sub-issue concept in the skills. `project-refresher` makes one tool call and no `gh` calls; it reads the `plans/README.md` table.
- **Domain docs:** `setup-workflow` writes `docs/agents/domain.md` (from `DOMAIN.md`) and un-ignores `docs/agents/` and `docs/adr/`. No ADR was ever written; the real `GLOSSARY.md` has 5 lines.
- **Optional mattpocock commands named:** `/grilling`, `/grill-with-docs`, `/domain-modeling`, `/to-tickets`, `/implement`, `/code-review`. mattpocock-skills is MIT-licensed (Copyright (c) 2026 Matt Pocock). Its `/grilling` asks in rounds over a design tree (numbered questions, each with a recommended answer; Claude finds facts, the user makes decisions). Its `/code-review` has two separate axes: Standards (the repo's documented style plus 12 Fowler code smells) and Spec (missing, not asked for, looks wrong, each quoting the spec).
- `new-plan` step 1 makes the issue optional; `setup-workflow` supports "no issue tracker".
- `new-plan` step 3 shows the draft in the chat; step 4 writes it only after approval.
- `Workflow version:` lines: `skills/setup-workflow/PLANS-README.md:3` and this repo's `plans/README.md:3`. Checks: `tests/check_skills.py` (manifest, `STALE`) and `tests/check_scripts.sh` (runs the refresher on a fake project).

## Steps
### 1. `plans/README.md` is the only rules file (template `setup-workflow/PLANS-README.md`)
- **Build structure:**
  - One branch per task.
  - A step is one commit on the task branch. Never several commits for one step by default; review fixes made before the commit go into it; a fix after the push is one commit named after the step.
  - A big step lists clear sub-steps in `PLAN.md`. It gets a sub-issue and its own branch, one commit per sub-step, and a PR into the task branch.
  - At the end, one PR from the task branch into `main`.
- **When a step needs sub-steps:** when it would pass about 400 changed lines of code (tests and logs not counted), or would touch unrelated parts of the code. More is fine for mechanical changes (renames, generated fixtures, moved code) if the commit or PR says so. A guide from code-review studies (SmartBear/Cisco: about 200-400 lines per review); Claude uses judgment.
- **Task issue:** a checklist of the `PLAN.md` steps, the one place step status is kept; a big step links its sub-issue. A sub-issue's text is 3 lines (what, done when, what to review) plus a link to its `PLAN.md` step; never copy the plan into issues. User-run checks are checkboxes in the task issue.
- **User-run checks:** checks that need something Claude cannot run (a cluster, real data, a GPU, credentials). Kept only if the answer could change a decision; bundled so one run covers as many as possible.
- **Review:** before each commit of a step, and before each PR: Claude Code's built-in `/code-review` for bugs, plus our own check, reported under separate headings: **Spec** (against the `PLAN.md` step: missing, not asked for, looks wrong; adapted from Matt Pocock's Spec axis); **Research** (rows silently lost in joins or filters, missing values, coordinate or unit mix-ups, unseeded randomness, numbers that look wrong); **Style** (the project's documented style only, plus three smells: unclear names, duplicated code, options nobody asked for).
- **Merge rule:** a PR into the task branch: low risk and tests pass → Claude merges; hard to undo or costly → Claude asks. The PR into `main`: the user merges. A project's `CLAUDE.md` can override this rule.
- **Plan changes** (replaces `/update-plan`): for any reason, in any status: change `PLAN.md` only for what the user said or decided; show the change before writing; log every decision. Once `planned` or later, a decision that changes the Goal or a step is tagged `- **DECISION <date> <time> (plan change):** <what>, because <why>; the plan missed: <x> (<evidence>)`. If an open question is added to a `planned` or `in-progress` task, ask once whether to go back to `drafting`. If a changed step has a sub-issue, update it. Commit: `plan: <short summary>`.
- **Logs:**
  - The folder log keeps only its Current state (active tasks, with links) and what no task log has: status changes, PRs and releases, work outside any task. No section per session.
  - A log update goes into the same commit as the work it describes. A commit for the log alone only when nothing else changed. When the user asks Claude to commit work (also work done by hand), Claude updates the logs in that commit.
- **Status:** five: `drafting`, `planned`, `in-progress`, `done`, `dropped`. Kept only in the task header line; no table in `plans/README.md`.
- **Glossary:** one bullet: `GLOSSARY.md` at the root, key terms only, added with the user's agreement (the three tests from `DOMAIN.md`).
- **Skill names:** always written `/name`.

### 2. `/finalize-plan` prepares the build
- Starts by offering `/grill-plan` when open questions or weak spots remain.
- Readiness check gains **Build shape:** each step is one commit, or a big step with sub-steps (the size guide in step 1).
- After the user confirms `planned`: show the GitHub structure the plan implies (the task issue checklist, a sub-issue and a branch per big step), and create it only after the user confirms.
- Replaces step 4 (the `/to-tickets` suggestion). No separate `/prep-implementation` skill. To re-split later, the user asks; the rules are in `plans/README.md`.

### 3. New skill `/grill-plan`, adapted from Matt Pocock's `/grilling`
- Keeps from `/grilling`: rounds over a design tree; each round asks every question whose prerequisites are settled, numbered, each with a recommended answer; Claude looks up facts itself and never asks the user for them; decisions are the user's; done when nothing is left silently assumed, and nothing is acted on before the user agrees.
- Adapted to this workflow: reads `PLAN.md`, the task log, `GLOSSARY.md` and the code first; starts from the open questions and weak spots; records each answer under the plan-change rules (DECISION lines, `PLAN.md` edits shown first); proposes a glossary term only when it passes the three tests.
- Usable at any time while drafting; `/finalize-plan` offers it. No `disable-model-invocation` flag, so `/finalize-plan` can call it (as the planning skills call `/progress`).
- Attribution: a line in the skill and in the README; Matt Pocock's MIT notice in a `NOTICE` file. Same for the parts of the review adapted from his `/code-review`.

### 4. New skill `/implement-next`
- **Read first:** if the user names a task, only that task's `PROGRESS.md` (Current state, Next, recent DECISION lines) and its issue checklist; if not, the active task from the folder `PROGRESS.md`, asking in one line if more than one is active. Check git for work not yet logged, as `/progress` does.
- **What to build:** unfinished work first; otherwise the next unchecked step. Running it is the user's choice to start building: on the first step of a `planned` task it sets `in-progress`.
- **Still needed?** Compare the step with findings and DECISION lines logged after it was written. If one may make it obsolete or change it, ask in one line before building.
- **Simple step:** build, review, one commit with the log update, tick the checklist.
- **Big step:** on its branch, one commit per sub-step, then review and a PR into the task branch; merge or ask per the merge rule; close the sub-issue with a comment.
- **More than one big step unblocked:** independent ones (no shared files or module) may run in parallel, one agent per worktree, at most 2-3; agents don't touch the logs; the main session reviews and logs. Otherwise one at a time: the one that unblocks the most first, then the smallest. Tell the user the choice in one line.
- **Review** per the rules in step 1.
- **After building:** write the next pick into the task's **Next**. Add a user-run check only if its answer could change a decision. Keep test discipline: tests are cheap once written and caught real bugs.

### 5. `/project-refresher`
- "What is next?": the task's **Next** already holds the pick (step 3), so no `gh` calls and no network. Asking never starts work.
- New `/project-refresher tasks`: one line per task with its status, from the task headers; open tasks first.
- Drop reading the `plans/README.md` table.

### 6. `/progress` follows the new rules
- The folder-log rule, the same-commit rule, status in the header only, five statuses, the `(plan change)` tag instead of the "plan change" section and `## Changes`.
- Step status lives in the task issue checklist; the logs keep events, decisions and links.

### 7. `/new-plan` drafts in a file, not in the chat
- Step 3: write the draft to `tmp/new-plan/<task>/PLAN.md`, give the user the path, and iterate on the file (the user can edit it too). Nothing goes into `plans/` or git before the user approves.
- Step 4 (after approval): create the branch, move the file to `plans/<task>/PLAN.md`, delete the tmp copy, then log and commit as now.
- Step 1: every task has an issue: use the one the user names, or create one. The folder and branch are always `issue-<N>-<slug>`.
- Step 1: if `tmp/new-plan/<task>/PLAN.md` exists (a session ended before approval), offer to continue from it.
- The `PLAN.md` skeleton shows a big step with sub-steps.

### 8. Remove what the reviews found unneeded
- Delete `skills/update-plan/` (its rules are in step 1). `/finalize-plan`, `/new-plan`, `/sandbox` and `/write-results` point to the plan-change rules instead.
- Remove ADRs and `docs/agents/`: delete `setup-workflow/DOMAIN.md`, the `docs/` un-ignore step and every ADR mention.
- Remove the `## Agent skills` block from `CLAUDE-SECTION.md` (Issue tracker and Domain docs).
- Remove every mattpocock-skills command (`/to-tickets`, `/implement`, `/grilling`, `/grill-with-docs`, `/domain-modeling`, its `/code-review`) and the README "Dependencies" section.
- `/setup-workflow`: GitHub is required (a GitHub remote); drop the "no issue tracker" branch.
- Remove the `paused` status.

### 9. Short project sections
- `CLAUDE-SECTION.md`: about 4 lines: read `plans/README.md`; start from the Current state; log every decision; status only by the user.
- `README-SECTION.md`: the flow diagram and a link to `plans/README.md`.

### 10. Docs, checks, version
- `README.md`, `docs/examples.html`, this repo's `CLAUDE.md`: the new flow and commands.
- `check_skills.py`: add to `STALE`: `/update-plan`, `/to-tickets`, `/implement` not followed by `-`, `/grilling`, `/grill-with-docs`, `/domain-modeling`, `paused`, `## Changes`, `docs/adr` (allowed in `setup-workflow/SKILL.md`, which names them to replace old sections). Flag a skill name in backticks without the slash.
- `check_scripts.sh`: covers `/project-refresher tasks`.
- `/setup-workflow`: upgrading an older project shows what changes (the status table, `paused` tasks, old `## Changes` sections, `docs/agents/domain.md`) and changes it only if the user agrees.
- `plugin.json` skills list (`/grill-plan` and `/implement-next` new, `/update-plan` gone). New version 0.2.0: bump `plugin.json` and both `Workflow version:` lines; add a CHANGELOG section that mentions [#3](https://github.com/giulianonetto/research-workflow/issues/3).

## Open questions
None.
