---
name: finalize-plan
description: Check that a drafting plan is ready to build, show the gaps, and set it to planned only after the user confirms.
disable-model-invocation: true
---

The user decides when a plan is ready; this skill checks it and makes the status change. It changes nothing without the user's confirmation.

If the folder has no `plans/README.md`, tell the user to run `/setup-workflow` first and stop. Find the task from the branch name or the folder's Current state; if that is not clear, ask. Read `plans/README.md`, `PLAN.md` and the task's `PROGRESS.md`. If the status is not `drafting`, say what it is and stop (a later change goes through `/update-plan`).

## Steps

1. **Check readiness.** Mark each item **ok** or **gap**, with one line on the gap:
   - **Goal:** what is true when done, and what is out of scope. For an experiment: one **Overall objective**, and each **Specific objective** says how it will be answered (which output, which `run.sh` stage); `experiment/run.sh` exists with the planned stages named, even if empty.
   - **Open questions:** none left, or each one the user accepts as an assumption the build can start with (it stays listed, with its "Plan assumes" text).
   - **Ground:** every file, function and dataset the plan names exists as described (check them now).
   - **Steps:** each says what to change and how to know it is done, so a fresh session could build from `PLAN.md` and `PROGRESS.md` alone.
   - **Decisions:** every decision the build depends on is in `PLAN.md`, not only in DECISION lines or the chat; no plan text contradicts a later DECISION line.

2. **Show the report.** For gaps, offer to fix them now (as `/update-plan` would, and log them the same way) or to stop and keep drafting. Done when every item is **ok**, or the user explicitly says to go ahead with the gaps listed.

3. **Confirm.** Ask: "Set the status to `planned`?" Only on a yes, run the `progress` skill for the status change (both logs; name any accepted gaps in the task log). Commit: `plan: finalized`.

4. **Next.** If the plan clearly spans several sessions and `/to-tickets` is available (mattpocock-skills plugin), suggest `/to-tickets plans/<task>/PLAN.md` now, in this session. Then tell the user to start building in a fresh session, from the task's `PROGRESS.md`.
