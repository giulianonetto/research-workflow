# Plan: Publish the examples page with GitHub Pages (#7)

**Started:** 2026-11-20 · **Status and progress:** [PROGRESS.md](PROGRESS.md) · **Folder log:** [../../PROGRESS.md](../../PROGRESS.md) · **Issue:** [#7](https://github.com/giulianonetto/research-workflow/issues/7) · **Branch:** `issue-7-pages`

## Goal
The examples page opens in the browser from one click in the README, with no download: GitHub Pages serves `docs/` from `main` at `https://giulianonetto.github.io/research-workflow/examples.html`. The page itself does not change.

Out of scope: a Markdown copy of the page; a custom domain; a Pages workflow in `.github/workflows/` (deploy from a branch is enough); making the repo public (the user does it).

## Where things are now
- The repo is private. Pages is not set up (`gh api repos/{owner}/{repo}/pages` gives 404). Pages on the free plan needs a public repo.
- `docs/` holds `examples.html` (291 lines, one `<style>` block, no JavaScript, 9 `<details>`), `figures.py` (makes the README figures) and `img/` (six SVGs used by the README).
- `docs/examples.html` has two links: `#github` (on the page) and `https://github.com/giulianonetto/research-workflow#commands` (works once the repo is public).
- `README.md:69`: "More: [examples](docs/examples.html): ... Download it and open it in a browser."
- `tests/check_skills.py` checks local links only in `SKILL.md` files; it scans `docs/examples.html` and `README.md` for stale names (`:91`). An `https://` link in the README is not checked.
- `CLAUDE.md:11`: "Keep `docs/examples.html` in step with the skills."
- 48 commits in history, all of which become public.

## Steps
### 1. Check the repo before it goes public
- The usual check before a repo goes public: secrets and personal details, in the files, all commits, issues and PRs.
- Report to the user. Nothing is changed without the user.
- **Stop:** the user reads the report and makes the repo public (Settings → General → Change visibility), before step 3 turns on Pages.

### 2. README and repo notes
- `docs/.nojekyll` (empty), so Pages serves the files as they are, without Jekyll.
- `README.md:69`: the link points to the Pages URL; drop "Download it and open it in a browser."
- `CLAUDE.md:11`: add that the page goes live when `main` changes.

### 3. Turn on Pages
- `gh api -X POST repos/giulianonetto/research-workflow/pages -f 'source[branch]=main' -f 'source[path]=/docs'` (outward-facing: Claude asks first; or the user does it in Settings → Pages).
- The site is built from `main`, so the page goes live when it is merged (step 2's README link works only after the merge).
- **Stop:** review the branch and open the PR into main; after the merge, open the URL in light and dark mode and check the README link.

## Open questions
1. If something must go from old commits: rewrite history (`git filter-repo`, then force-push `main` and the tags; the `v0.2.0`/`v0.3.0` tags and old PR links change), or start the public repo from a fresh history. Plan assumes nothing yet: decided after the step 1 report, and it may add a step.
2. The site root (`.../research-workflow/`) has no `index.html`, so it gives 404. Plan assumes that is fine (only `examples.html` is linked). Other choices: a small `docs/index.html` that redirects to `examples.html`.
3. `figures.py` and `img/` are served too. Plan assumes that is fine (they are public in the repo anyway).
4. Order: Pages can only be turned on after the repo is public, but the branch must be merged for the page to show. Plan assumes: public (after step 1) → turn on Pages (step 3) → merge. Turning on Pages before the merge serves the current `main`, which already has the page, so nothing breaks.
