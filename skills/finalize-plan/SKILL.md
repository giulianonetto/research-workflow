---
name: finalize-plan
description: Check that a drafting plan is ready to build, show the gaps, set it to planned only after the user confirms, then prepare the build on GitHub (the task issue checklist, a sub-issue for each big step).
disable-model-invocation: true
---

The user decides when a plan is ready; this skill checks it, makes the status change and prepares the build. It changes nothing without the user's confirmation.

If the folder has no `plans/README.md`, tell the user to run `/setup-workflow` first and stop. Find the task from the branch name or the folder's Current state; if that is not clear, ask. Read `plans/README.md`, `PLAN.md` and the task's `PROGRESS.md`. If the status is not `drafting`, say what it is and stop (a later change goes through `/update-plan`).

## Steps

1. **Grill first?** If open questions or weak spots remain (a thin step, a fact not checked, an assumption nobody stated), offer `/grill-plan` before the check, in one line. The user can skip it.

2. **Check readiness.** Mark each item **ok** or **gap**, with one line on the gap:
   - **Goal:** what is true when done, and what is out of scope. For an experiment: one **Overall objective**, and each **Specific objective** says how it will be answered (which output, which `run.sh` stage); `experiment/run.sh` exists with the planned stages named, even if empty.
   - **Open questions:** none left, or each one the user accepts as an assumption the build can start with (it stays listed, with its "Plan assumes" text).
   - **Ground:** every file, function and dataset the plan names exists as described (check them now).
   - **Steps:** each says what to change and how to know it is done, so a fresh session could build from `PLAN.md` and `PROGRESS.md` alone.
   - **Decisions:** every decision the build depends on is in `PLAN.md`, not only in DECISION lines or the chat; no plan text contradicts a later DECISION line.
   - **Issue:** the task has a GitHub issue; its title matches the plan's title (offer to update it if not); its body holds the problem and the plan link, and no solution text (rules in `plans/README.md`).
   - **Build shape:** each step is one commit, or a big step that lists its sub-steps (the size rule in `plans/README.md`: about 400 changed lines of code, or unrelated parts of the code). Recommend the fewest big steps.

3. **Show the report.** For gaps, offer to fix them now (as `/update-plan` would, and log them the same way) or to stop and keep drafting. Done when every item is **ok**, or the user explicitly says to go ahead with the gaps listed.

4. **Confirm.** Ask: "Set the status to `planned`?" Only on a yes, go on.

5. **Prepare the build.** Show the GitHub structure the plan implies, and create it only after the user confirms:
   - the task issue's checklist: one checkbox per `PLAN.md` step, below the plan link in the body (`gh issue edit <N> --body-file ...`; keep the problem text and the link);
   - for each big step: a sub-issue (3 lines: what, done when, what to review, plus a link to its `PLAN.md` step), linked from its checklist line, and its branch `issue-<M>-<slug>` (`<M>` is the sub-issue number), made from the task branch.

   If the user wants another split later, they ask; the rules are in `plans/README.md`. No separate skill is needed.

6. **Log and commit.** Run `/progress` for the status change (both logs; name any accepted gaps and what was created on GitHub in the task log). Commit: `plan: finalized`.

7. **Next.** Tell the user to start building in a fresh session with `/implement-next`.
