#!/usr/bin/env bash
# Functional checks: the experiment run.sh template and the project-refresher script,
# run against a small fake project (one normal task, one experiment).
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
RUNSH=$ROOT/skills/new-plan/experiment-template/run.sh
WORK=$(mktemp -d); trap 'rm -rf "$WORK"' EXIT
fail() { echo "FAILED: $*" >&2; exit 1; }
has()  { grep -qF -- "$2" <<<"$1" || fail "$3 (expected to see: $2)"; }

# the refresher's collection script, taken from its SKILL.md
sed -n '/^```bash$/,/^```$/p' "$ROOT/skills/project-refresher/SKILL.md" | sed '1d;$d' > "$WORK/refresh.sh"
bash -n "$WORK/refresh.sh" || fail "refresher script does not parse"
bash -n "$RUNSH" || fail "run.sh template does not parse"

# fake project
P=$WORK/proj; mkdir -p "$P/plans/issue-1-old" "$P/plans/issue-3-bench" "$P/plans/issue-5-exp/experiment"
cd "$P"; git init -q -b main; git config user.email t@t; git config user.name t
cat > PROGRESS.md <<'EOF'
# Progress log

## Current state (updated 2026-10-30)
- **Now:** [issue-3-bench](plans/issue-3-bench/PROGRESS.md) in-progress; [issue-5-exp](plans/issue-5-exp/PROGRESS.md) in-progress

## 2026-10-30: work
### 10:00: x
- did a thing
EOF
printf '# Progress: old (#1)\n**Status:** done · **Kind:** task · **Plan:** [PLAN.md](PLAN.md)\n' > plans/issue-1-old/PROGRESS.md
cat > plans/issue-3-bench/PROGRESS.md <<'EOF'
# Progress: bench (#3)
**Status:** in-progress · **Kind:** task · **Plan:** [PLAN.md](PLAN.md)

## Current state (updated 2026-10-30)
- step 2 of 4

## 2026-10-30: build
### Next
- open R/sim.R and run step 3
### 10:00: step 2
- **DECISION 2026-10-30 10:00:** ruled out DSS, because too slow (sandbox 03)
EOF
cat > plans/issue-5-exp/PROGRESS.md <<'EOF'
# Progress: exp (#5)
**Status:** in-progress · **Kind:** experiment · **Plan:** [PLAN.md](PLAN.md)

## Current state (updated 2026-10-30)
- fitting

## 2026-10-30: runs
### Next
- write up
EOF
printf '# Results\n\n## Answers\n<!-- unreviewed -->\n**Overall objective:** <one line>\n' > plans/issue-5-exp/RESULTS.md
cp "$RUNSH" plans/issue-5-exp/experiment/run.sh; chmod +x plans/issue-5-exp/experiment/run.sh
git add -A; git commit -qm init

# run.sh: lists stages, rejects unknown ones, records runs locally and next to OUT
X=plans/issue-5-exp/experiment/run.sh
out=$(cd / && "$P/$X"); has "$out" "example" "run.sh with no stage should list stages"
(cd / && "$P/$X" nope 2>/dev/null) && fail "run.sh accepted an unknown stage"
(cd / && OUT=$WORK/scratch "$P/$X" all >/dev/null)
[ -f "$WORK/scratch/run-info.log" ] || fail "run.sh did not write \$OUT/run-info.log"
[ -f "$P/tmp/experiments/issue-5-exp/last-run.txt" ] || fail "run.sh did not write tmp/experiments/<task>/last-run.txt"
has "$(cat "$WORK/scratch/run-info.log")" "commit: $(git rev-parse HEAD)" "run-info.log should record the commit"
[ -d "$P/plans/issue-5-exp/results" ] || fail "run.sh did not create results/"

# refresher: short and detailed, from the repo root and from a subfolder
short=$(bash "$WORK/refresh.sh")
has "$short" "**Status:** in-progress · **Kind:** task" "refresher should show the task header"
has "$short" "open R/sim.R and run step 3" "refresher should show the task's Next"
has "$short" "-- last run:" "refresher should show the experiment's last run"
has "$short" "-- stages: example all" "refresher should list the experiment's stages"
has "$short" "1 unreviewed sections" "refresher should count unreviewed sections"
detailed=$(sed 's/^MODE=short/MODE=detailed/' "$WORK/refresh.sh" | bash)
has "$detailed" "-- recent decisions:" "detailed refresher should list recent decisions"
tasks=$(sed 's/^MODE=short/MODE=tasks/' "$WORK/refresh.sh" | bash)
has "$tasks" "in-progress · issue-3-bench · bench (#3)" "tasks mode should list each task with its status"
has "$tasks" "in-progress · issue-5-exp · exp (#5)" "tasks mode should list the experiment too"
grep -q "open R/sim.R" <<<"$tasks" && fail "tasks mode should print only the task lines"
[ "$(grep -c ' · issue-' <<<"$tasks")" = 3 ] && [ "$(grep ' · issue-' <<<"$tasks" | tail -n 1)" = "done · issue-1-old · old (#1)" ] || fail "tasks mode should list open tasks first, done ones last"
mkdir -p sub; sub=$(cd sub && bash "$WORK/refresh.sh")
has "$sub" "PROGRESS.md (current state)" "refresher should find the repo root from a subfolder"

echo "ok: run.sh template and refresher script"
