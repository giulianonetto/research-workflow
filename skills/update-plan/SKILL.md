---
name: update-plan
description: Change a task's PLAN.md at any time and for any reason - decisions, ruled-out options, new ideas or steps, open questions, rewording, or a review of what looks stale - and log decisions as DECISION lines. Never changes the task status on its own.
disable-model-invocation: true
---

For any change to a plan, in any status, as often as the user likes: in the middle of a brainstorm, during a build session, or in a fresh session just to look at it. It never changes the status, except when the user answers the reopen question in step 4.

If the folder has no `plans/README.md`, tell the user to run `/setup-workflow` first and stop. Find the task from the branch name or the folder's Current state; if that is not clear, ask which task. Before changing anything, read `plans/README.md` (format rules), the task's `PLAN.md`, and the Current state and latest entries of its `PROGRESS.md`.

## Steps

1. **Find what to change.** Sources: what the user says now, and this conversation since the plan was last updated (decisions, options ruled out, sandbox or run results). If the user gives nothing specific, review: compare `PLAN.md` with the recent `PROGRESS.md` entries, sandbox findings and the code, list what looks stale, contradicted or missing, and ask what to change. Never write a decision the user didn't make. Done when the list of changes is agreed, or the user says there is nothing to change (then stop and write nothing).

2. **Sort each change:**
   - **Wording, order, clarification:** edit only.
   - **New idea, step or open question:** edit.
   - **Decision** (an option chosen or ruled out, with its reason): a DECISION line in step 6. Edit `PLAN.md` too when the decision changes what the plan says; an option ruled out may need only the DECISION line. A settled open question leaves **Open questions**.
   - **Real change to an agreed plan:** when the status is `planned` or `in-progress` and the change alters the Goal (for an experiment, an objective) or what a step does, add a line at the top of `## Changes` (create it at the bottom of the file): `YYYY-MM-DD: <what changed>, because <reason> (<evidence link>)`. The reason can be short. No `## Changes` lines while `drafting`, and none for wording.

   Decision records: if a change contradicts an ADR in `docs/adr/`, say so; a new ADR that supersedes it only if the user agrees. If a decision meets the ADR rules in `docs/agents/domain.md`, offer one; its DECISION line then links to it.

3. **Edit `PLAN.md`.** Show the changes and iterate until the user approves them.

4. **Reopen question.** If an open question was added and the status is `planned` or `in-progress`, ask once: keep the status, or go back to `drafting`? Both are valid. This is the only status change this skill makes, and only on the user's answer.

5. **Tickets**, if any: edit the ones the change touches, close the ones it removes (with a comment saying why), create new ones with their blocking edges.

6. **Log it.** Run the `progress` skill for a **plan update**: the task log gets a short note of what changed and the DECISION lines; the folder log is left for the end of the session unless the status changed. Commit `PLAN.md` and the log together: `plan: <short summary>`.
