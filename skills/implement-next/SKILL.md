---
name: implement-next
description: Build the next steps of a task's PLAN.md, up to the next stop, under the build rules in plans/README.md - asks once at the start, then for each step reviews, makes one commit with the log update in it, pushes the task branch and ticks the issue checklist. Sets a planned task to in-progress on its first step.
disable-model-invocation: true
---

Builds the next steps of a task in one run, up to the next stop, then stops. Running it is the user's choice to start building. The build rules (stops, runs, commits, big steps, review, push, merge rule, user-run checks, logs) are in `plans/README.md`; if it is missing, tell the user to run `/setup-workflow` and stop.

## Steps

1. **Read first.** `plans/README.md`. If the user names a task, read only that task's `PROGRESS.md` (Current state, Next, recent DECISION lines); if not, take the active task from the folder `PROGRESS.md`, and ask in one line if more than one is active. Then read its `PLAN.md` and the task issue's checklist (`gh issue view <N>`). Check git for work not yet logged, as `/progress` does (`git log --since=<last logged entry> --stat`, `git status --short`); ask in one line about anything unclear.

2. **Pick the run.** Start with unfinished work (Next, uncommitted changes, an open big-step branch), otherwise the next unchecked step in the checklist. The run goes from there up to the first step with a `**Stop:**` line, that step included, and holds at most the number of steps in `plans/README.md` (Runs). A big step counts as one step. A plan with no Stop lines was made before 0.3.0: the run is one step. On the first step of a `planned` task, set the status to `in-progress` (logged with this step, as a status change).

3. **Ask once.** Name the run in one line and ask, for example: "I will build steps 3, 4 and 5, then stop after step 5 (Stop: look at the plots). OK, or one step at a time?" If "Still needed?" (step 4) fires for the first step, ask it in the same message. For "one step at a time", the run is the first step only. Then build the whole run without asking again, unless an early stop comes up (step 7).

4. **Still needed?** Before each step, compare it with the findings and DECISION lines logged after it was written, also those from earlier in this run. If one may make the step obsolete or change it, stop and ask in one line; a change goes through the plan-change rules.

5. **Build each step,** one at a time (no parallel builds unless the user asks).
   - **Simple step:** on the task branch: build, review (step 6), then one commit with the log update in it (`/progress`), named after the step. Push the task branch and tick the step's box in the checklist.
   - **Big step:** on its branch (`<task branch>-step-<n>`, from the task branch; make it if `/finalize-plan` did not): one commit per sub-step, each with its log update in the task log (`/progress`), then review and a PR into the task branch. Merge it or ask, per the merge rule; asking is an early stop. After the merge, pull the task branch, close the sub-issue with a one-line comment and tick the step's box.

   The last commit of each step writes the next pick into the task's **Next** (the step, the file to open, the command to run).

   Keep test discipline: write or update tests with the code, and run them before the commit. Tests are cheap once written and catch real bugs. Pushing the task branch needs no question (unless the project's `CLAUDE.md` says otherwise); pushing or merging into `main` does.

6. **Review** before each commit of a step and before each PR, as `plans/README.md` says: the full review (`/code-review` for bugs, then **Spec**, **Research** and **Style** under their own headings) for a step that changes a file that runs or sets the results, and before every PR; only the **Spec** check for a step that changes only text. Fix what is clear before the commit; anything to ask about is an early stop.

7. **Stop** after the step with the Stop line, at the run limit, or early: a test fails and the fix is not clear, the review finds something to ask about, "Still needed?" fires, the merge rule says to ask, or a decision comes up that the plan does not cover. On an early stop, leave the open work uncommitted (a big step's sub-step commits stay), write the open question into the task's **Next**, and say what is open.

8. **After the run.** Add a user-run check to the task issue only if its answer could change a decision. When every box is ticked, review the whole task branch the same way and offer to open the PR into `main` (`Closes #<N>` in its description); the user merges it. End with one summary: each step built and its review result, every decision Claude made alone (each is a DECISION line in the log), why the run stopped, and what is next.
