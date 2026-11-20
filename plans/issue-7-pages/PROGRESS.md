# Progress: Publish the examples page with GitHub Pages (#7)
**Status:** drafting · **Kind:** task · **Plan:** [PLAN.md](PLAN.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#7](https://github.com/giulianonetto/research-workflow/issues/7)

## Current state (updated 2026-11-20)
- Plan drafted: check the repo before it goes public, README link to the Pages URL, turn on Pages from `main` `/docs`.
- The user makes the repo public after the step 1 check.
- Open: the history question if something must go from old commits; a 404 at the site root.

## 2026-11-20: plan started
Started from the user's question on how to show `docs/examples.html` on GitHub.
### Next
- `/finalize-plan`, or settle open question 2 (site root 404) in `PLAN.md` first.
### 11:25: plan started
- Issue [#7](https://github.com/giulianonetto/research-workflow/issues/7) and `PLAN.md`, status `drafting`.
- **DECISION 2026-11-20 11:25:** publish `docs/examples.html` with GitHub Pages from `main` `/docs`, with the repo made public by the user, instead of a Markdown copy, because GitHub strips `<style>`, classes and inline SVG from Markdown, so the page would lose its look, and a second copy would need keeping in step (user)