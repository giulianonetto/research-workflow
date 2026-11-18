---
name: implement-next
description: Build the next step of a task's PLAN.md under the build rules in plans/README.md - one commit per step with the log update in it, review first, tick the issue checklist, write the next pick into Next. Sets a planned task to in-progress on its first step.
disable-model-invocation: true
---

Builds one step (or, for big steps that don't touch the same files, up to 2-3 at once), then stops. Running it is the user's choice to start building. The build rules (commits, big steps, review, merge rule, user-run checks, logs) are in `plans/README.md`; if it is missing, tell the user to run `/setup-workflow` and stop.

## Steps

1. **Read first.** `plans/README.md`. If the user names a task, read only that task's `PROGRESS.md` (Current state, Next, recent DECISION lines); if not, take the active task from the folder `PROGRESS.md`, and ask in one line if more than one is active. Then read its `PLAN.md` and the task issue's checklist (`gh issue view <N>`). Check git for work not yet logged, as `/progress` does (`git log --since=<last logged entry> --stat`, `git status --short`); ask in one line about anything unclear.

2. **Pick what to build.** Unfinished work first (Next, uncommitted changes, an open sub-issue branch). Otherwise the next unchecked step in the checklist. On the first step of a `planned` task, set the status to `in-progress` (logged with this step, as a status change).

3. **Still needed?** Compare the step with the findings and DECISION lines logged after it was written. If one may make the step obsolete or change it, ask in one line before building; a change goes through the plan-change rules.

4. **More than one big step unblocked?** Big steps that share no files or module may run in parallel: one agent per worktree, at most 2-3. The agents don't touch the logs; this session reviews and logs. Otherwise build one at a time: first the one that unblocks the most, then the smallest. Tell the user the choice in one line.

5. **Build.**
   - **Simple step:** on the task branch: build, review (step 6), then one commit with the log update in it (`/progress`), named after the step. Tick its box in the checklist.
   - **Big step:** on its branch (`issue-<M>-<slug>`): one commit per sub-step, then review and a PR into the task branch. Merge it or ask, per the merge rule. Close the sub-issue with a one-line comment and tick the step's box.

   Keep test discipline: write or update tests with the code, and run them before the commit. Tests are cheap once written and catch real bugs. Ask before pushing.

6. **Review** before each commit of a step and before each PR, as `plans/README.md` says: `/code-review` for bugs, then **Spec**, **Research** and **Style** under their own headings. Fix what is clear before the commit; ask about the rest.

7. **After building.** Write the next pick into the task's **Next** (the step, the file to open, the command to run), in the same commit. Add a user-run check to the task issue only if its answer could change a decision. Tell the user what was built, the review result and what is next.
