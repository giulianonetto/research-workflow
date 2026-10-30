---
name: progress
description: Log work in the task's plans/TASK/PROGRESS.md and the folder's PROGRESS.md, including DECISION lines and changes made by hand. Use at the end of a work session or phase, when the user gives a task a new status, when /new-plan, /update-plan or /finalize-plan call it, when the user reports sandbox findings, or when the user says "log progress".
---

Two logs: the folder's `PROGRESS.md` (what is active; one short section per session) and one `plans/<task>/PROGRESS.md` per task (everything, including every decision). The format rules, the task header line and the DECISION line format are in the folder's `plans/README.md` (if it is missing, tell the user to run `/setup-workflow` and stop). Before writing, read it, the top block of the folder `PROGRESS.md` and the task's `PROGRESS.md`. Times are the user's local time: take them from the commit times (they keep their offset) or `TZ=Europe/Berlin date` (or the user's zone); a cloud session's clock is UTC.

## Which log

- **End of a work session, or the user asks:** both logs.
- **A plan update** (called by `/update-plan`): the task log only, unless the status changed. The folder log covers it in the end-of-session section.
- **A status change, a PR opened or merged:** both logs.
- **Work outside any task:** the folder log only, DECISION lines included.

## Steps

1. **Find the task.** The branch name or the folder Current state names it.

2. **Catch work done outside this session.** The user also works by hand. Check what changed since the last logged entry (its date and time): `git log --since=<that time> --stat`, `git status --short`, `git diff --stat`. Any change this session didn't make goes in the log too, marked **(by hand)**, with its commit or file paths. If its purpose isn't clear from the commit message or the diff, ask the user in one line; don't guess. Not a git repo: ask the user if they changed anything by hand.

3. **Task log** (`plans/<task>/PROGRESS.md`):
   - Today's dated entry (create it if missing): a new time-tagged section right below **Next**, with what changed and its evidence: commits, job IDs, check results, file paths, the `PLAN.md` steps finished. Don't mark steps in `PLAN.md`: status lives only in the logs.
   - **DECISION lines** for every major decision made since the last entry and not yet logged (an option chosen or ruled out, with its reason), in the exact format of `plans/README.md`. Never edit or delete an old DECISION line: a changed decision gets a new line that says which one it replaces.
   - Rewrite **Next**, starting with the exact first action of the next session (the `PLAN.md` step or open question, the file to open, the command to run): the next session starts fresh and reads this first.
   - Rewrite the **Current state** block and its date.

4. **Folder log** (`PROGRESS.md`), when the rules above call for it:
   - Today's dated entry: one short time-tagged section for the session (2-3 bullets + a link to the task's `PROGRESS.md`). Summarize plan updates and decisions in a few words; don't copy DECISION lines here (a grep would show them twice).
   - Rewrite the **Current state** block and its date.

5. **Status.** Change it only when the user says so, or when `/new-plan` or `/finalize-plan` asks after the user confirmed. Use only the six statuses in `plans/README.md`. If this session built steps of a `planned` task, ask once whether to set it to `in-progress`. Set the status in both places (the `plans/README.md` table and the task header line). Also:
   - **New task** (from `/new-plan`): create the task `PROGRESS.md` (the title and header line exactly as in `plans/README.md`, Current state, a first dated entry, same structure as the folder log), add the row to the `plans/README.md` table, and link the folder from the folder Current state.
   - **PR opened / merged** (events, not statuses): name the PR and the merge commit in both Current state blocks.
   - **Done or dropped:** one-line summary (or reason) in the folder log; drop the task from the folder Current state.
   - **Experiment done or dropped** (`**Kind:** experiment`): first run the **Close check** in `plans/EXPERIMENTS.md` and show what is missing; help fill it if the user wants. Change the status only when it passes, or when the user explicitly accepts the gaps (name them in the task log). `done` means the objective was answered, whatever the answer; the final DECISION line states it. `dropped` needs only the short `RESULTS.md`.

6. **Plan change** (a `## Changes` line was added by `/update-plan`): the task log gets a time-tagged section titled `plan change` giving what changed, the evidence (link), and **what the planning missed**, one line each.

7. **Sandbox findings.** Log them in the task log with a link to the entry in `plans/<task>/sandbox/README.md`, and a DECISION line if they settled something.

Done when the logs the rules call for describe the work just logged (by hand or not) and carry today's date, every decision is a DECISION line, and the status matches in every place it is kept.
