# Plan: Publish a project site with GitHub Pages (#7)

**Started:** 2026-11-20 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#7](https://github.com/giulianonetto/research-workflow/issues/7) · **Branch:** `issue-7-pages`

## Goal
People land on one page that explains everything: what the workflow is, how to install it, how a task and a build run, the commands, and the examples. GitHub Pages serves `docs/` from `main`, with that page as `docs/index.html` at `https://giulianonetto.github.io/research-workflow/`. The README links to it.

Out of scope: a Markdown copy of the page; a custom domain; a Pages workflow in `.github/workflows/` (deploy from a branch is enough); making the repo public (the user does it); JavaScript on the page.

## Where things are now
- The repo is private. Pages is not set up (`gh api repos/{owner}/{repo}/pages` gives 404). Pages on the free plan needs a public repo.
- `docs/` holds `examples.html` (375 lines, one `<style>` block, no JavaScript, 9 `<details>`, light and dark mode), `figures.py` (makes the README figures) and `img/` (six SVGs: `flow`, `runs`, `start`, each light and dark).
- `docs/examples.html`: a five-day story from idea to merged PR, "How the work lands on GitHub" (an inline SVG branch diagram, anchor `#github`), four short cases. It links to `https://github.com/giulianonetto/research-workflow#commands` for the command table.
- `README.md` (107 lines): intro, flow figure, Why use it, How a build runs (runs figure), Get started (start figure, install, Claude Code install in `<details>`), Commands table, experiments line, "More: [examples](docs/examples.html) ... Download it and open it in a browser." (`:69`), What it writes in a project (`<details>`), Credits, Development.
- `tests/check_skills.py:91` scans `docs/examples.html`, `README.md` and `CLAUDE.md` for stale names; it checks local links only in `SKILL.md` files.
- `CLAUDE.md:11`: "Keep `docs/examples.html` in step with the skills."
- 48 commits in history, all of which become public.

## Steps
### 1. Check the repo before it goes public
- The usual check before a repo goes public: secrets and personal details, in the files, all commits, issues and PRs.
- Report to the user. Nothing is changed without the user.
- **Stop:** the user reads the report and makes the repo public (Settings → General → Change visibility), before step 4 turns on Pages.

### 2. One page with everything (`docs/index.html`)
- Top: what it is in one line, then the install box.
- The README's content: Why use it, the three figures (the SVGs in `docs/img/`, light and dark via `<picture>`), How a build runs, Get started (both install ways), Commands, What it writes in a project.
- The examples folded in as a section: the five-day story, How the work lands on GitHub, the four cases. The `#commands` link points to the page's own Commands section.
- A short nav at the top that jumps to the sections. The look, palette and dark mode of `examples.html`; no JavaScript.
- Delete `docs/examples.html` (never public, so no link to keep).
- Done when every README section and every examples section is on the page, the nav links work, and it reads well in light and dark mode and at phone width.
- **Stop:** the user opens the page locally and judges it, before step 3 links to it.

### 3. README, notes, checks
- `README.md`: a site link near the top; `:69` "More: examples ... download it" becomes a link to the site.
- `docs/.nojekyll` (empty), so Pages serves the files as they are, without Jekyll.
- `CLAUDE.md:11`: "Keep `docs/index.html` in step with the skills and the README; it goes live when `main` changes."
- `tests/check_skills.py:91`: scan `docs/index.html` instead of `docs/examples.html`.

### 4. Turn on Pages
- `gh api -X POST repos/giulianonetto/research-workflow/pages -f 'source[branch]=main' -f 'source[path]=/docs'` (outward-facing: Claude asks first; or the user does it in Settings → Pages).
- The site is built from `main`, so the page goes live when the branch is merged.
- After the merge: open the site in light and dark mode and at phone width, and check the README links.
- **Stop:** review the branch and open the PR into main

## Open questions
1. If something must go from old commits: rewrite history (`git filter-repo`, then force-push `main` and the tags; the `v0.2.0`/`v0.3.0` tags and old PR links change), or start the public repo from a fresh history. Plan assumes nothing yet: decided after the step 1 report, and it may add a step.
2. Should the README get shorter now that the site has the details? Plan assumes no: GitHub visitors read the README first.
3. `figures.py` and `img/` are served too. Plan assumes that is fine (they are public in the repo anyway).
4. Order: Pages can only be turned on after the repo is public, but the branch must be merged for the page to show. Plan assumes: public (after step 1) → turn on Pages (step 4) → merge. Before the merge, the site root gives 404 (no `index.html` on `main` yet); nothing links there yet, so nothing breaks.
