# research-workflow

Claude skills for research repos (see README.md). The skills are in `skills/`; each folder is one skill.

## Working on this repo

- This repo uses its own workflow: read the Current state of `PROGRESS.md` first; tasks live in `plans/`; log with the `progress` skill; every design decision is a DECISION line (format in `plans/README.md`).
- The skills are written for a non-native English speaker: short sentences, plain words.
- After changing a skill, run `python3 tests/check_skills.py` and `bash tests/check_scripts.sh`. When you rename or remove a command, add its old name to `STALE` in `tests/check_skills.py`.
- The templates in `skills/setup-workflow/` are copied into projects. A change to them is a new version: bump `.claude-plugin/plugin.json` and the `Workflow version:` line together, and add a CHANGELOG section.
- Keep `docs/examples.html` in step with the skills.
