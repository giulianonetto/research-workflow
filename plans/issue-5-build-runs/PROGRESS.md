# Progress: Build in runs that stop where the plan says, with lighter build rules (#5)
**Status:** in-progress · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#5](https://github.com/giulianonetto/research-workflow/issues/5)

## Current state (updated 2026-11-18)
- All 6 steps done; version 0.3.0. [PR #6](https://github.com/giulianonetto/research-workflow/pull/6) into `main` is open (`Closes #5`); the user merges it.
- README rewritten after step 6 at the user's request: shorter, three figures, experiments left out.
- Next: after the merge, `/progress` "merged, mark done", then tag `v0.3.0`.

## 2026-11-18: plan started
Started from building #2 and the talk after it, in this session and in a second chat on stops (its proposal was pasted into this session).
### Next
- Wait for the user to merge [PR #6](https://github.com/giulianonetto/research-workflow/pull/6). Then `/progress` "merged, mark done" (one folder-log entry, plan link in #5 to `main`), and tag `v0.3.0` (`git tag v0.3.0 && git push origin v0.3.0`).
### 15:02: PR into main opened
- [PR #6](https://github.com/giulianonetto/research-workflow/pull/6) opened from `issue-5-build-runs` into `main`, `Closes #5`.
### 14:59: step 6, README round 3
- At the user's request: a Get started figure (install → `/setup-workflow` → `/new-plan`, `docs/img/start-*.svg`) with 3 short steps; install cut to Claude Desktop, with Claude Code in a toggle; Command first in the table; the file list as a tree; Credits say the project is heavily inspired by mattpocock-skills; Development folded in a toggle under its heading.
- Dropped from the README: install in chat and Cowork, and the claude.ai route; the push-permission line moved under "How a build runs". Then 24px of space added under each figure (`PAD` in `docs/figures.py`): on GitHub the text sat right against them.
### 14:53: step 6, experiments off the README
- Removed from `README.md`: the experiments bullet, `/new-plan exp` and `/write-results` in the command table, the experiment files in the file tree, and the experiment example in the link line. The skills, `docs/examples.html` and `docs/workflow.html` still describe experiments.
- **DECISION 2026-11-18 14:53:** the README leaves experiments out for now, because the user did not like how they read there and experiments are frozen until the first real one (user)
### 14:47: step 6, README with figures
- The user found the README overwhelming and asked for prettier diagrams. New README: pitch, flow figure, "Why use it" (cut to 4 one-line bullets at the user's request), a runs figure, a 3-line start, the command table; the file tree and install details are folded in `<details>`. Figures: `docs/img/{flow,runs}-{light,dark}.svg`, drawn by `docs/figures.py`, checked by rendering them in headless Chrome.
- **DECISION 2026-11-18 14:47:** the README figures are SVG files drawn by a script (`docs/figures.py`) in a light and a dark version, shown with `<picture>`, ruling out Mermaid and screenshots, because Mermaid cannot match the look of `docs/workflow.html` and screenshots go stale, while a script redraws both versions from one place (user asked for prettier diagrams; Claude chose the form)
### 14:25: step 6, docs, checks, version 0.3.0
- One full review of the whole branch, run before the step 6 commit, served both as step 6's review (it changes `tests/check_skills.py`) and as the review before the PR. Fixed: params/config files and notebooks count as files that set results; an early stop writes its question into Next; "Still needed?" for the first step joins the run question; the CLAUDE.md push override is named in `/new-plan` and `/implement-next`; `docs/workflow.html` is now scanned by `check_skills.py` and its Close card says Claude offers the PR; a stray blank line; the order of the status change in examples workflow 3; the step count left out of the folder Current state. Not fixed: the folder-log commit at the merge lands on `main`, as it already did for "mark done" in 0.2.0.
- Also changed, not named in the plan: `skills/setup-workflow/README-SECTION.md` ("/implement-next in runs"), and `STALE` gained "ask(s) before pushing" and "agent per worktree".
- **DECISION 2026-11-18 14:24:** the full review also covers steps that change config and params files or notebooks, not only code, scripts, pipelines and tests, because those change the results without being code and would otherwise get only the Spec check (review finding; Claude decided alone)
- **DECISION 2026-11-18 14:24:** the `/new-plan` skeleton shows only the last step's fixed Stop line and gives the `- **Stop:** <why>` form in the text below it, ruling out a `<why>` Stop on step 1, because a Stop placeholder on an early step would be copied into drafts and turn runs back into one step at a time (review finding; Claude decided alone)
### 14:15: step 5, `/new-plan` skeleton shows a stop
- The skeleton shows two Stop lines: one with a `<why>` on step 1 and the fixed one on the last step.
- The run was named "steps 2-5, stop before step 6" (in the step 1 Next and at the start of this run); by the new rules it runs up to and including the step with the Stop, so steps 2-6. It stopped after step 5 as agreed with the user.
### 14:15: step 4, `/progress` follows the new log rules
- The 2-bullet limit is for step entries only; other work (plan changes, sessions by hand) still logs what changed and its evidence.
### 14:14: step 3, `/implement-next` builds a run
- Added beyond the plan text: an early stop leaves the open step uncommitted; for a big step, Next is written by its last sub-step commit and the task branch is pulled after the merge.
### 14:14: step 2, `/finalize-plan` proposes the stops
- Run of steps 2-5 started: the user re-ran `/implement-next` after the Next note named the run, so no separate question was asked.
### 14:09: step 1, rules file
- Status `planned` → `in-progress`. Also changed the `/implement-next` line in Commands ("builds the next steps, up to the next stop"); the "Same commit" example (a PR built in another worktree) stays, since parallel builds are still allowed when the user asks.
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
