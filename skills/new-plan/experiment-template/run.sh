#!/usr/bin/env bash
# Experiment: <title> (#<N>)
# The one entry point for this experiment's results. Rules: plans/EXPERIMENTS.md
#
# How to use it (from any folder):
#   ./run.sh                    show the list of stages
#   ./run.sh simulate fit       run these stages, in this order
#   ./run.sh all                run every stage
#   OUT=/scratch/$USER/x ./run.sh fit    same, but big outputs go to /scratch/$USER/x
#
# You only edit PART 2. Leave PART 1 and PART 3 as they are.

# ===== PART 1: setup (leave as is) =====
set -euo pipefail            # stop at the first error, instead of carrying on with broken results
cd "$(dirname "$0")"         # work from this folder (experiment/), wherever you call it from
TASK=$(basename "$(dirname "$PWD")")                                  # the task folder name, e.g. issue-52-hurdle-vs-zinb
ROOT=$(git rev-parse --show-toplevel 2>/dev/null || (cd ../../.. && pwd))   # the repo's top folder
OUT=${OUT:-$ROOT/tmp/experiments/$TASK}   # BIG outputs: not in git (tmp/ is gitignored). Set OUT=... to put them elsewhere.
RES=../results                            # SMALL outputs for RESULTS.md (tables, figures): committed to git
export OUT RES                            # so your R/Python scripts can read them: Sys.getenv("OUT"), os.environ["OUT"]

# ===== PART 2: stages (edit here) =====
# A stage is a name followed by () and a block in { }. Inside the block, write the commands
# you would type in the terminal. "$OUT" and "$RES" are the two output folders above.
# A name starting with _ is a helper, not a stage (it is not listed).

example() {
  echo "replace me with real commands, for example:"
  echo "  Rscript simulate.R \"\$OUT/sim\"                  # an R script"
  echo "  python fit.py --in \"\$OUT/sim\" --out \"\$OUT/fit\"  # a Python script"
  echo "  nextflow run main.nf -profile slurm --outdir \"\$OUT/nf\""
  echo "  Rscript -e 'targets::tar_make()'"
  echo "  sbatch --wait job.slurm \"\$OUT\"                  # a cluster job; waits until it ends"
  echo "  Rscript summarize.R \"\$OUT\" \"\$RES\"               # writes the small tables/figures"
}

all() {                      # runs the stages one after the other
  example
}

# ===== PART 3: runner (leave as is) =====
_stages() { grep -oE '^[a-z][a-z0-9_]*\(\)' "$0" | tr -d '()'; }        # finds the stage names in this file
if [ $# -eq 0 ]; then echo "stages:"; _stages | sed 's/^/  /'; exit 0; fi   # no stage given: list them
for s in "$@"; do _stages | grep -qx "$s" || { echo "unknown stage: $s (run ./run.sh to list)" >&2; exit 1; }; done
LOCAL=$ROOT/tmp/experiments/$TASK                                      # always local and gitignored, even when OUT is elsewhere
mkdir -p "$OUT" "$RES" "$LOCAL"
{ echo "== $(date '+%Y-%m-%d %H:%M:%S %z') $(hostname) stages: $*"   # provenance: when, where, what
  echo "commit: $(git rev-parse HEAD 2>/dev/null || echo none)"         # which version of the code
  echo "out: $OUT"
  git status --porcelain 2>/dev/null | head -n 20 | sed 's/^/  uncommitted: /'; } > "$LOCAL/last-run.txt"
cat "$LOCAL/last-run.txt" >> "$OUT/run-info.log"                        # full history next to the outputs
for s in "$@"; do echo ">> $s"; "$s"; done                               # run each stage you asked for
