# Plan: Right-size the build: /prep-implementation, implement-next, "what is next?" (#2)

**Started:** 2026-11-17 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#2](https://github.com/giulianonetto/research-workflow/issues/2) · **Branch:** `issue-2-right-size-build`

## Goal
The build stage is sized to the task. By default a task is built on one branch with one PR. It is split into sub-issues only when that is needed, and then into the fewest that keep each PR reviewable. The user follows the build from one table, asking "what is next?" never starts work, and "implement next" follows fixed rules. Out of scope here: how a project runs its user-run checks (sbatch, containers, paths). That belongs in the project's own `CLAUDE.md` or docs.

Source: review of a real project, 2026-11-16/17 (`real-project/tmp/skill-building/workflow-review-2026-11-16.md`, not in git). There, a medium task (a few hundred lines) was split into 10 sub-issues.

## Where things are now
- 8 skills, version 0.1.1. `finalize-plan`, `new-plan`, `update-plan`, `write-results` and `setup-workflow` have `disable-model-invocation: true`. `progress`, `sandbox` and `project-refresher` do not.
- `finalize-plan` step 4 suggests `/to-tickets` (mattpocock-skills) for a multi-session build. `/to-tickets` and `/implement` are also named in `setup-workflow/README-SECTION.md` (flow diagram, steps 4-5), `setup-workflow/CLAUDE-SECTION.md` (lines 12, 19), `README.md:66` and `docs/examples.html` (lines 284, 298).
- No sub-issue concept anywhere: no parent issue table, no status rule for sub-issues, no merge rule.
- `project-refresher` is read-only and makes one tool call (one bash script). It reads the folder and task `PROGRESS.md`, plus the task's **Next**. It makes no `gh` calls.
- `progress` writes PRs and merge commits into both Current state blocks.
- `new-plan` step 3 shows the `PLAN.md` draft in the chat; step 4 writes it to `plans/<task>/` only after approval. A long draft is hard to review in the chat. `/setup-workflow` adds `tmp/` to `.gitignore`.
- `Workflow version:` line: `skills/setup-workflow/PLANS-README.md:3` (template) and this repo's own `plans/README.md:3`.
- Checks: `tests/check_skills.py` (manifest = skill folders, `STALE` patterns) and `tests/check_scripts.sh` (runs the refresher on a fake project).

## Steps
### 1. Rules in the `plans/README.md` template (`setup-workflow/PLANS-README.md`)
- **Sub-issues:** optional; default none. Each one's text is 3 lines: what, done when, what to review, plus a link to its `PLAN.md` step. Never copy the plan into issues.
- **Parent issue table:** the one place sub-issue status is kept. One row per sub-issue: status, PR, next user decision. User gates are checkboxes in the parent issue, not sub-issues.
- **Status in one place:** the task log keeps events, decisions and evidence, and links to the table. It does not copy sub-issue status.
- **User-run checks:** checks that need something Claude cannot run (a cluster, real data, a GPU, credentials). Kept only if the answer could change a decision, and bundled once per milestone.
- **Merge rule:** low risk and tests pass → Claude merges. Hard to undo or costly → Claude asks.

### 2. New skill `prep-implementation`
- Runs after the plan is final; can also run alone (e.g. to re-split after a plan change).
- Default: no sub-issues. Claude checks critically whether a split is needed: easier review, parallel work, or a user gate between parts. Then it recommends the fewest sub-issues, with a reason for each split.
- Review size drives the split: aim for under about 400 changed lines of code per PR (tests and logs not counted), or split when one PR would touch unrelated parts of the code. More is fine for mechanical changes (renames, generated fixtures, moved code) if the PR body says so. The number is a guide, from code-review studies (SmartBear/Cisco: about 200-400 lines per review), and Claude uses judgment.
- The user and Claude decide together; a DECISION line records the choice. No issue is created before the user confirms N.
- It also settles: the branch(es), the user-run checks worth running (bundled per milestone), and the review plan.
- If split: it creates the short sub-issues, the parent issue table and the branch names.

### 3. `finalize-plan` calls `prep-implementation` as its last step
- Replace step 4 (the `/to-tickets` suggestion) with this call.

### 4. New skill `implement-next`
- **Read first:** if the user names a task, read only that task's `PROGRESS.md` (Current state, Next, recent DECISION lines) and the parent issue table. If not, find the active task in the folder `PROGRESS.md`; if more than one is active, ask in one line. Check git for work not yet logged, as `progress` does.
- **Still needed?** For each candidate, compare the sub-issue with findings and DECISION lines logged after it was written. If one may make it obsolete or change it, ask in one line before building.
- **More than one unblocked:**
  - Independent (no shared files, module or log edits): build in parallel, one agent per worktree, at most 2-3. Agents don't touch the progress logs; the main session reviews and logs.
  - Shared files: one at a time, in this order: (1) needs a user wait (start it first so the wait overlaps other work); (2) unblocks the most other work; (3) smallest first.
  - Tell the user the choice in one line; ask only when the order needs their judgment.
- **After building:** review (`/code-review`, full tests, smoke test). Merge or ask per the merge rule, then close the issue with a comment. Add a user-run check to the milestone bundle only if its answer could change a decision. Log with `progress` and update the parent issue table.
- Keep test discipline: tests are cheap once written and caught real bugs.

### 5. "What is next?" in `project-refresher`
- Still read-only. Add the unblocked sub-issues, the still-needed check and one recommendation. Asking must not start work.

### 6. `progress` follows the status rule
- Sub-issue status goes in the parent issue table only. The logs keep events and links.

### 7. `new-plan` drafts in a file, not in the chat
- Step 3: write the draft to `tmp/new-plan/<task>/PLAN.md`, give the user the path, and iterate on the file (the user can edit it too). The order stays: nothing goes into `plans/` or git before the user approves.
- Step 4 (after approval): create the branch, move the file to `plans/<task>/PLAN.md`, delete the tmp copy, then log and commit as now.
- Step 1: if `tmp/new-plan/<task>/PLAN.md` already exists (a session ended before approval), offer to continue from it.

### 8. Docs, checks, version
- `README-SECTION.md` flow and steps 4-5, `CLAUDE-SECTION.md`, `README.md`, `docs/examples.html`: new flow; drop `/to-tickets` and `/implement` from the flow.
- `plugin.json` skills list; `check_scripts.sh` covers the refresher's new part.
- New version (template change): bump `plugin.json` and both `Workflow version:` lines; add a CHANGELOG section.

## Open questions
1. **Can `finalize-plan` call `prep-implementation`?** A skill with `disable-model-invocation: true` cannot be invoked by Claude. Plan assumes `prep-implementation` leaves the flag off (as `progress` does), so `finalize-plan` can call it.
2. **Where does the parent table live without a GitHub issue?** (A task with no issue, or no tracker.) Plan assumes: no sub-issues without an issue tracker; the build stays one branch.
3. **How does `project-refresher` read the parent table?** It needs `gh issue view` (network) inside its one script. Plan assumes: only when the task header links an issue, with a short timeout, and the section is skipped silently if offline.
4. **Version number.** Plan assumes 0.2.0 (two new skills and a template change).
5. **`/to-tickets` and `/implement`.** Plan assumes they leave the flow but stay in the README list of optional mattpocock commands. Add `/to-tickets` to `STALE` for the skill files.
6. **Experiments.** Plan assumes `prep-implementation` runs for them too, but they usually stay at one branch; it lists their user-run checks the same way.
7. **Merge rule as a default.** Plan assumes the rule in `plans/README.md` is a default that a project's `CLAUDE.md` can override.
8. **Which `/code-review`.** Both Claude Code and mattpocock-skills have one. Plan assumes `implement-next` uses whichever is installed and says "review the diff" if neither is.
