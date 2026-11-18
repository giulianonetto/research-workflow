---
name: grill-plan
description: Ask the hard questions about a task's plan in rounds - numbered questions, each with a recommended answer - until nothing is left silently assumed, and record each answer in PLAN.md and DECISION lines. Use while a plan is drafting, when the user says "grill the plan", or when /finalize-plan offers it.
---

Adapted from Matt Pocock's grilling skill (mattpocock-skills, MIT License, Copyright (c) 2026 Matt Pocock; full notice in the plugin's `NOTICE` file).

Use it any time while a plan is drafting, as often as the user likes; `/finalize-plan` offers it when weak spots remain. If the folder has no `plans/README.md`, tell the user to run `/setup-workflow` first and stop. Find the task from the branch name or the folder's Current state; if that is not clear, ask.

## Steps

1. **Read first.** `plans/README.md` (the rules, the glossary tests), the task's `PLAN.md`, its `PROGRESS.md` (Current state, recent entries, DECISION lines), `GLOSSARY.md` if it exists, and the code and data the plan names. Start from the **Open questions** and the weak spots: a thin step, a fact not checked, an assumption nobody stated, plan text that contradicts a DECISION line.

2. **Map the design tree.** Every decision branches into the decisions that depend on it. The **frontier** is every decision whose prerequisites are settled: the questions you can ask now without guessing at answers you have not heard yet.

3. **Ask in rounds.** Ask the whole frontier in one round, then wait for the answers. Number each question and give your recommended answer, worded so that "yes" accepts it:

   ```
   **Q1. <title>:** <the question, with the options if there are several>
   Recommended: <your answer, with the reason in one line>
   ```

   A question that depends on another question still open in this round waits for a later round. After each round, recompute the frontier: settled decisions open new questions.

4. **Facts are yours, decisions are the user's.** Look up every fact yourself (files, data, code, git, docs); never ask the user for something you can find. A running lookup only holds back the questions that depend on it. Put every decision to the user and wait.

5. **Record the answers** under the plan-change rules in `plans/README.md`: every decision is a DECISION line in the task log; show each `PLAN.md` edit before writing it; a settled question leaves **Open questions**. Propose a glossary term only when it passes the three tests in `plans/README.md`, and add it only if the user agrees. Log with `/progress` and commit `PLAN.md` and the log together: `plan: <short summary>`.

Done when the frontier is empty: every branch visited, nothing left silently assumed. Act on nothing (no `PLAN.md` edit, no code) before the user agrees.
