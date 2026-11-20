# Progress: Publish a project site with GitHub Pages (#7)
**Status:** in-progress · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#7](https://github.com/giulianonetto/research-workflow/issues/7)

## Current state (updated 2026-11-20)
- `in-progress`: step 1 (check before going public) done; it found personal details in old commits and tags.
- Plan change: new step 2 rewrites the history and moves to a new repo with the same name; old steps 2-4 are now 3-5.
- Next stop: after step 2, the user checks the new repo and makes it public.

## 2026-11-20: plan started
Started from the user's question on how to show `docs/examples.html` on GitHub.
### Next
- `PLAN.md` step 2: clean the history and move to a new repo (`/implement-next`).
### 15:03: plan change: clean the history, move to a new repo
- `PLAN.md`: new step 2 (rewrite all branches and tags, move to a new repo with the same name); old steps 2-4 become 3-5; open question 1 settled and removed.
- **DECISION 2026-11-20 15:03 (plan change):** rewrite the history with `git filter-repo` and push it to a new repo with the same name, with the old repo renamed `research-workflow-old`, kept private and archived, because personal details sit in old commits and tags, and GitHub keeps merged PRs' commits in `refs/pull/*`, which a force-push cannot remove; the plan missed: what the history holds (step 1 check)
- **DECISION 2026-11-20 15:03:** every commit gets one author name and GitHub's noreply email, and new commits use it too, because the personal email would be public in every commit (user)
- **DECISION 2026-11-20 15:03:** the time zone city comes out of the logs and their history ("Times are local."), because it is a location hint (user)
- **DECISION 2026-11-20 15:03:** moved issues keep their numbers, with closed one-line placeholders at #1, #4 and #6 for the old PRs, because branch names, task folders and logs use the numbers (user)
### 14:50: step 1: check before going public
- Files, all commits on every branch and tag, issues, PRs and releases checked; the report went to the user, not into the repo. No secrets; personal details in old commits and tags. Status `planned` → `in-progress`.
### 13:36: finalized
- `/finalize-plan`: two small gaps fixed with the user's yes (step 2 says when it is done; step 4's Stop line has the exact wording, the post-merge check is a bullet above it). The four open questions accepted as they stand. No big steps. Status `drafting` → `planned`. Checklist (4 boxes) added to issue #7; no sub-issues.
### 12:27: one page with everything
- `PLAN.md`: new step 2 builds `docs/index.html` with the README's content and the examples, and deletes `docs/examples.html`; old steps 2-3 become 3-4; title, Goal and open questions follow (the site-root 404 question is gone).
- **DECISION 2026-11-20 12:27:** the site is one landing page, `docs/index.html`, with everything (README content, figures, commands, the examples folded in), and `docs/examples.html` is deleted, instead of publishing the examples page alone, because people should land in one place; the cost is a page to keep in step with the README, covered by the `CLAUDE.md` line and the stale-name check (user)
### 11:25: plan started
- Issue [#7](https://github.com/giulianonetto/research-workflow/issues/7) and `PLAN.md`, status `drafting`.
- **DECISION 2026-11-20 11:25:** publish `docs/examples.html` with GitHub Pages from `main` `/docs`, with the repo made public by the user, instead of a Markdown copy, because GitHub strips `<style>`, classes and inline SVG from Markdown, so the page would lose its look, and a second copy would need keeping in step (user)