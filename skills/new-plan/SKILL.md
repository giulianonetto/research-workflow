---
name: new-plan
description: Start a new task or experiment as a draft - GitHub issue, a draft PLAN.md in tmp/ to iterate on, then (after approval) branch, plans/TASK/ with PLAN.md and PROGRESS.md, status drafting. Can start from the current conversation or from a draft the user already has.
disable-model-invocation: true
---

Starts a task in status `drafting`. Nothing needs to be settled yet: the plan then grows under the plan-change rules in `plans/README.md` (`/grill-plan` helps), over as many sessions and days as needed, and is made ready with `/finalize-plan`. Run it as soon as an idea is worth tracking.

If the folder has no `plans/README.md`, tell the user to run `/setup-workflow` first and stop. Read `plans/README.md` first: it holds the format rules (task header line, DECISION lines).

## Steps

1. **Name the task.** Every task has a GitHub issue: use the one the user names, or create one (`gh issue create`, with a short working title and a body that is the problem only, in 2-3 lines; never the solution). The issue title follows the plan's title: if the approved plan's title differs, update the issue title in step 5. The folder and branch are always `issue-<N>-<slug>`. If `tmp/new-plan/<task>/PLAN.md` exists (a session ended before approval), offer to continue from it. If `plans/<task>/` already exists, stop: that plan changes under the plan-change rules in `plans/README.md`. It is a normal task unless the user says it is an **experiment** (tries something out and ends in an answer; see `plans/EXPERIMENTS.md`), e.g. `/new-plan exp`, `/new-plan experiment`, or in words; don't ask. If it is an experiment and `plans/EXPERIMENTS.md` is missing, tell them to re-run `/setup-workflow` first and stop. Done when the folder name, the kind and the issue number are fixed.

2. **Gather the starting material.** This conversation so far, the issue's title, body and comments when it already existed (`gh issue view <N> --comments`), and/or a draft the user points to (a file, a note, pasted text). Read the code and data it names, and `GLOSSARY.md` if the folder has one, enough to write **Where things are now** correctly. Don't interview: anything unsettled becomes an open question. Done when every file, function and dataset the draft names has been checked.

3. **Draft `PLAN.md` in a file.** Write the draft to `tmp/new-plan/<task>/PLAN.md` (`tmp/` is not in git and survives sessions), give the user the path, and iterate on that file; the user can edit it too. Nothing goes into `plans/` or git before the user approves. If other `plans/*/PLAN.md` exist, match their shape. Otherwise:

   ```
   # Plan: <title> (#<N>)

   **Started:** <date> · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** <link> · **Branch:** `<branch>`

   ## Goal
   <what is true when this is done>. Out of scope here: <...>.

   ## Where things are now
   - <facts the steps build on: files, functions, data, sizes>

   ## Steps
   ### 1. <step>
   - <bullets; file paths and function names welcome>

   ### 2. <big step: about 400+ changed lines of code, or unrelated parts of the code>
   - **2a.** <sub-step: one commit>
   - **2b.** <sub-step: one commit>
   - **Stop:** review the branch and open the PR into main

   ## Open questions
   1. <point left unsettled>. Plan assumes <current assumption, or "nothing yet">.
   ```

   For an experiment, replace `## Goal` with `## Overall objective` (one line) and `## Specific objectives` (numbered; each says how it will be answered: which output, which `run.sh` stage, or "to decide").

   Thin is fine: a one-line Goal and a list of open questions is a valid start. From a user's draft, keep all its content and map it into these sections; ask before dropping anything. No status in `PLAN.md` (it lives in `PROGRESS.md`). Stop lines are optional while drafting: `/finalize-plan` proposes a `- **Stop:** <why>` line for each step the user must look at, and always the one on the last step (the stop rule is in `plans/README.md`, Build). Iterate on the file until the user approves it.

4. **Write it** (after approval). Create the branch if it doesn't exist, from the up-to-date default branch unless the user says otherwise (`git switch <main> && git pull`, then `git switch -c <branch>`; if there are uncommitted changes, ask first). Move the draft to `plans/<task>/PLAN.md` and delete the `tmp/new-plan/<task>/` copy. For an experiment, also scaffold, filling the title, issue and task name:
   - `experiment/run.sh` from [experiment-template/run.sh](experiment-template/run.sh), executable;
   - `results/` with an empty `.gitkeep`;
   - `RESULTS.md` from the template in `plans/EXPERIMENTS.md` (placeholders stay until the experiment closes);
   - `analysis.qmd` from [analysis-r.qmd](experiment-template/analysis-r.qmd) by default; from [analysis-py.qmd](experiment-template/analysis-py.qmd) only if the user asks for Python (for another language, keep the same three parts). The experiment itself can use any language or tool: only `analysis.qmd` has a default.

   Then run `/progress` for a **new task** with status `drafting` (and `**Kind:** experiment` for an experiment). Decisions already made in this conversation or in the user's draft go in as DECISION lines (for decisions from an earlier draft, use that draft's date if known and say "from draft").

5. **Commit and link.** One commit, `plan: start <task>`. Push the branch (no question needed: it is the task branch, unless the project's `CLAUDE.md` says otherwise). Then set the issue title to the plan's title if it differs, and put the plan link in the issue body, below the problem text, not in a comment: `gh issue edit <N> --body-file ...` with `Plan: <blob URL of PLAN.md on the branch>`. If the push failed, say the link is pending.

6. **Next.** Tell the user: the plan can change at any time (just say what to change; `/grill-plan` asks the hard questions); run `/finalize-plan` when they think it is ready to build.
