---
name: progress
description: Log work in the task's plans/TASK/PROGRESS.md (and the folder's PROGRESS.md only when the rules call for it), including DECISION lines and changes made by hand. Use when work is committed, at the end of a work session, when the user gives a task a new status, when a PR is opened or merged, when /new-plan, /finalize-plan, /grill-plan or /implement-next call it, when the user reports sandbox findings, or when the user says "log progress".
---

Two logs: one `plans/<task>/PROGRESS.md` per task (the work, its evidence and every decision) and the folder's `PROGRESS.md` (its Current state, and only what no task log has). The format rules, the task header line and the DECISION line format are in the folder's `plans/README.md` (if it is missing, tell the user to run `/setup-workflow` and stop). Before writing, read it, the top block of the folder `PROGRESS.md` and the task's `PROGRESS.md`. Times are the user's local time: take them from the commit times (they keep their offset) or `TZ=Europe/Berlin date` (or the user's zone); a cloud session's clock is UTC.

## Which log

- **Work on a task** (a step, a plan change, a work session): the task log only.
- **A status change, the task's PR into `main` merged, a release:** the task log and the folder log. The task's PR into `main` opened: the task log, and only the folder's Current state names it. A big step's PR into the task branch goes in the task log only.
- **Work outside any task:** the folder log only, DECISION lines included.

The folder log never gets a section per session.

## Same commit

A log update goes into the same commit as the work it describes. When the user asks Claude to commit work (also work done by hand), update the logs first and commit them together. Make a commit for the log alone only when nothing else changed.

## Steps

1. **Find the task.** The branch name (`issue-<N>-<slug>`, or a big step's `issue-<N>-<slug>-step-<n>`: the part before `-step-`) or the folder Current state names it.

2. **Catch work done outside this session.** The user also works by hand. Check what changed since the last logged entry (its date and time): `git log --since=<that time> --stat`, `git status --short`, `git diff --stat`. Any change this session didn't make goes in the log too, marked **(by hand)**, with its commit or file paths. If its purpose isn't clear from the commit message or the diff, ask the user in one line; don't guess. Not a git repo: ask the user if they changed anything by hand.

3. **Task log** (`plans/<task>/PROGRESS.md`):
   - Today's dated entry (create it if missing): a new time-tagged section right below **Next**. For a step: the commit plus only what the diff can't show (changes from the plan, what was left for later), at most 2 bullets, plus DECISION lines. For other work: what changed and its evidence (commits, job IDs, check results, file paths). Step status lives in the task issue's checklist, not in `PLAN.md` or the logs: tick the box there, and keep events, decisions and links here.
   - **DECISION lines** for every major decision made since the last entry and not yet logged (an option chosen or ruled out, with its reason), in the exact format of `plans/README.md`. Never edit or delete an old DECISION line: a changed decision gets a new line that says which one it replaces.
   - **Plan change:** once the task is `planned` or later, a decision that changes the Goal or what a step does carries the `(plan change)` tag and says what the plan missed (format in `plans/README.md`, Plan changes).
   - Rewrite **Next** (open tasks only: a `done` or `dropped` task has none, see step 5), starting with the exact first action of the next session (the `PLAN.md` step or open question, the file to open, the command to run): the next session starts fresh and reads this first.
   - Rewrite the **Current state** block and its date.

4. **Folder log** (`PROGRESS.md`), only when "Which log" calls for it:
   - Today's dated entry: one short time-tagged section for the event (1-2 bullets + a link to the task's `PROGRESS.md`); for the task's PR into `main`, one entry, written at the merge. Don't copy DECISION lines here (a grep would show them twice).
   - Rewrite the **Current state** block and its date: the active tasks, with links.

5. **Status.** Change it only when the user says so, or when `/new-plan`, `/finalize-plan` or `/implement-next` asks after the user's choice. Use only the five statuses in `plans/README.md`. The status lives only in the task header line. Also:
   - **New task** (from `/new-plan`): create the task `PROGRESS.md` (the title and header line exactly as in `plans/README.md`, Current state, a first dated entry, same structure as the folder log), and link the folder from the folder Current state.
   - **The task's PR into `main` opened / merged** (events, not statuses): name the PR (and, once merged, the merge commit) in both Current state blocks; its description says `Closes #<N>`. When the task's PR into `main` is merged, change the plan link in the task issue's body to point to `main` (`gh issue edit <N> --body-file ...`).
   - **Done or dropped:** one-line summary (or reason) in the folder log; drop the task from the folder Current state. The task log keeps no Next: its Current state bullet and its last `### Next` become `None: task <status>.` with a link to the folder log. Any follow-up work (a run, a new task, open issues) moves to the folder log's **Next**, because a Next nobody reads again goes stale without anyone noticing.
   - **Experiment done or dropped** (`**Kind:** experiment`): first run the **Close check** in `plans/EXPERIMENTS.md` and show what is missing; help fill it if the user wants. Change the status only when it passes, or when the user explicitly accepts the gaps (name them in the task log). `done` means the objective was answered, whatever the answer; the final DECISION line states it. `dropped` needs only the short `RESULTS.md`.

6. **Sandbox findings.** Log them in the task log with a link to the entry in `plans/<task>/sandbox/README.md`, and a DECISION line if they settled something.

Done when the logs the rules call for describe the work just logged (by hand or not) and carry today's date, every decision is a DECISION line, the status in the task header is right, and the log update is in the same commit as the work.
