# research-workflow

Claude skills for research repos (see README.md). The skills are in `skills/`; each folder is one skill.

## Working on this repo

- This repo uses its own workflow, with all its rules in `plans/README.md`: read the Current state of `PROGRESS.md` first; tasks live in `plans/`; `/implement-next` builds one step per commit; the log update goes in the same commit as the work; every design decision is a DECISION line.
- The skills are written for a non-native English speaker: short sentences, plain words.
- After changing a skill, run `python3 tests/check_skills.py` and `bash tests/check_scripts.sh`. When you rename or remove a command, add its old name to `STALE` in `tests/check_skills.py`.
- The templates in `skills/setup-workflow/` are copied into projects. A change to them is a new version: bump `.claude-plugin/plugin.json` and the `Workflow version:` line together, and add a CHANGELOG section.
- Keep `docs/examples.html` in step with the skills.
