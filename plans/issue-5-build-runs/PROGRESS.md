# Progress: Build in runs that stop where the plan says, with lighter build rules (#5)
**Status:** planned · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#5](https://github.com/giulianonetto/research-workflow/issues/5)

## Current state (updated 2026-11-18)
- Planned: 6 one-commit steps (rules file, `/finalize-plan`, `/implement-next`, `/progress`, `/new-plan` skeleton, docs and version 0.3.0); no big steps.
- Stops: after step 1 (read the rules) and after step 6 (review, PR into `main`).
- Next: step 1 with `/implement-next`, in a fresh session.

## 2026-11-18: plan started
Started from building #2 and the talk after it, in this session and in a second chat on stops (its proposal was pasted into this session).
### Next
- `/implement-next` in a fresh session: step 1, the rules in `skills/setup-workflow/PLANS-README.md` and `plans/README.md`. Stop after it, so the user can read the rules.
### 14:04: plan finalized
- `/finalize-plan`: two gaps fixed with the user's yes (stops added; step 6 now names `docs/workflow.html`, the push lines in `docs/examples.html` workflows 2 and 3, and the `README.md` command table). No gaps accepted. Status `drafting` → `planned`.
- Issue [#5](https://github.com/giulianonetto/research-workflow/issues/5): 6-box step checklist added to the body; no sub-issues (no big steps).
- **DECISION 2026-11-18 14:04:** this plan's stops are after step 1 (read the new rules before steps 2-5 copy them) and after step 6 (review the branch, PR into `main`), ruling out a stop on the last step only, because the rules text is the core of the task and is worth reading before it spreads to four skills (user chose the recommended option)
### 13:54: grill round 1
- `/grill-plan` found 5 weak spots; the user accepted all 5 recommended answers ("yes to all"). `PLAN.md` steps 1, 2, 3 and 5 updated.
- **DECISION 2026-11-18 13:54:** a `**Stop:**` line always means stop after its step (build, commit, push, report); a step that must not start without the user puts its Stop on the step before, because the plan's stop reasons pointed both ways and its example said "stop before step 6" (user: "yes to all")
- **DECISION 2026-11-18 13:54:** `/finalize-plan` always puts a Stop on the last step (review the branch and open the PR into `main`), so a plan with no Stop lines is always one made before 0.3.0, because otherwise a new plan with no step needing the user would ask before every step (user: "yes to all")
- **DECISION 2026-11-18 13:54:** a big step counts as one step toward the run limit, and a merge-rule question before merging its PR is one more early stop, because the plan did not say how big steps count (user: "yes to all")
- **DECISION 2026-11-18 13:54:** `/new-plan` drops "(ask before pushing)" for the first push of the task branch, keeping `/setup-workflow`'s "Don't push" (its commit is on `main`), because the plan's Done-when rules out any skill asking before pushing the task branch (`skills/new-plan/SKILL.md:54`) (user: "yes to all")
- **DECISION 2026-11-18 13:54:** step 3 rewrites `/implement-next`'s frontmatter description to say it builds the next steps up to the next stop, because it still says "Build the next step" (user: "yes to all")
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
