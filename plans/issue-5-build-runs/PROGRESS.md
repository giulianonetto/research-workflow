# Progress: Build in runs that stop where the plan says, with lighter build rules (#5)
**Status:** drafting · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#5](https://github.com/giulianonetto/research-workflow/issues/5)

## Current state (updated 2026-11-18)
- Drafting: 6 small steps (rules file, `/finalize-plan`, `/implement-next`, `/progress`, `/new-plan` skeleton, docs and version 0.3.0). No open questions.
- Next: `/finalize-plan` (it should also propose the stops for this plan's own steps, once step 1 is agreed).

## 2026-11-18: plan started
Started from building #2 and the talk after it, in this session and in a second chat on stops (its proposal was pasted into this session).
### Next
- `/finalize-plan`, in a fresh session.
### 12:58: plan started
- Issue [#5](https://github.com/giulianonetto/research-workflow/issues/5) (problem only), branch `issue-5-build-runs`; `PLAN.md` drafted in `tmp/new-plan/issue-5-build-runs/` and approved by the user.
- **DECISION 2026-11-18 12:58:** a step that needs the user carries a `- **Stop:** <why>` line in `PLAN.md`, proposed by `/finalize-plan` and confirmed by the user, and `/implement-next` builds up to the next stop after asking once, because then the user agrees to the stops in advance and Claude never judges alone that a step is safe, as happened in #2 under "go on" (second chat's proposal; user: "go ahead")
- **DECISION 2026-11-18 12:58:** a run builds at most 5 steps, a number written in `plans/README.md` so a project can change it, because a long run fills the context (user)
- **DECISION 2026-11-18 12:58:** the full review (`/code-review`, Spec, Research, Style) runs for each step that changes a file that runs and on the whole branch before every PR; a step that changes only text gets a Spec check, because in #2 one full review of the branch found 10 issues while the steps were text-only (user)
- **DECISION 2026-11-18 12:58:** a step's log entry is the commit plus only what the diff can't show, at most 2 bullets plus DECISION lines, because #2's 3-5 bullets per step mostly repeated the commit (user)
- **DECISION 2026-11-18 12:58:** after each step commit, push the task branch and tick the step's box, without asking; pushing or merging into `main` still needs the user, because the user wants to see on GitHub when a step is done, and a box ticked for a local commit says more than is true (user: "if I finish step 7, I want to know"; "pushing to task branch is fine")
- **DECISION 2026-11-18 12:58:** no parallel builds unless the user asks, removing the 2-3 worktree rule in `/implement-next`, because it was never used and the user does not want work built in parallel by default (user)
- **DECISION 2026-11-18 12:58:** `/implement-next` keeps `disable-model-invocation: true` and its name, ruling out removing the flag, because only the user should start a build, and with runs one command covers several steps (user: "I like the safety")
- **DECISION 2026-11-18 12:58:** the folder log gets one entry per task PR, written at the merge; while the PR is open, only the Current state names it, because #2's PR got two folder-log entries on one day (user)
- **DECISION 2026-11-18 12:58:** `/setup-workflow` does not change Claude Code's permission settings; `README.md` gets one line on allowing `git push` there, because that is the user's machine setting, not a workflow rule (user approved the plan's default)
