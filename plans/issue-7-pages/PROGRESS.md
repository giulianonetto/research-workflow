# Progress: Publish a project site with GitHub Pages (#7)
**Status:** planned · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#7](https://github.com/giulianonetto/research-workflow/issues/7)

## Current state (updated 2026-11-20)
- `planned`: check the repo before it goes public, one page with everything (`docs/index.html`, examples folded in), README links, turn on Pages from `main` `/docs`.
- The user makes the repo public after the step 1 check.
- Open questions accepted as assumptions (old commits, a shorter README, served files, order).

## 2026-11-20: plan started
Started from the user's question on how to show `docs/examples.html` on GitHub.
### Next
- In a fresh session: `/implement-next`, starting with `PLAN.md` step 1 (check the repo before it goes public).
### 13:36: finalized
- `/finalize-plan`: two small gaps fixed with the user's yes (step 2 says when it is done; step 4's Stop line has the exact wording, the post-merge check is a bullet above it). The four open questions accepted as they stand. No big steps. Status `drafting` → `planned`. Checklist (4 boxes) added to issue #7; no sub-issues.
### 12:27: one page with everything
- `PLAN.md`: new step 2 builds `docs/index.html` with the README's content and the examples, and deletes `docs/examples.html`; old steps 2-3 become 3-4; title, Goal and open questions follow (the site-root 404 question is gone).
- **DECISION 2026-11-20 12:27:** the site is one landing page, `docs/index.html`, with everything (README content, figures, commands, the examples folded in), and `docs/examples.html` is deleted, instead of publishing the examples page alone, because people should land in one place; the cost is a page to keep in step with the README, covered by the `CLAUDE.md` line and the stale-name check (user)
### 11:25: plan started
- Issue [#7](https://github.com/giulianonetto/research-workflow/issues/7) and `PLAN.md`, status `drafting`.
- **DECISION 2026-11-20 11:25:** publish `docs/examples.html` with GitHub Pages from `main` `/docs`, with the repo made public by the user, instead of a Markdown copy, because GitHub strips `<style>`, classes and inline SVG from Markdown, so the page would lose its look, and a second copy would need keeping in step (user)