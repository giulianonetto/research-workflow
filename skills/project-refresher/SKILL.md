---
name: "project-refresher"
description: "Give a short 'where was I?' brief for a project folder after days or weeks away. Reads the folder's PROGRESS.md, plans/ and recent DECISION lines first; falls back to git state, recent files and R/shell history only when there is no log."
---

# Project refresher

Tell the user what they were doing in this folder, what is unfinished, and the next step.

## Arguments
Words after the command, any order, all optional:
- no mode word → **short mode (default)**; `detailed` → detailed mode.
- a number (e.g. `14`) → `DAYS=14` (fallback scan only).
- a path → `cd` there first.
- other words → a topic to focus on.

## Rules
- **Read-only.** Never commit, stash, checkout, delete or edit anything.
- **Exactly ONE tool call** (the script below) in short mode, then write the brief. Detailed mode: the same script with `MODE=detailed`, plus at most 1 extra call if it changes the brief (e.g. `git diff --stat`).
- **The logs are the source of truth.** If the folder has a `PROGRESS.md`, the script reads it and its active task folders and skips the scan. The task's **Next** was written for exactly this moment: use it as the next step, don't re-derive it.
- Never walk the whole folder (`find .`, `du`, `ls -R`): data folders can be huge. Never `cat`/Read history, logs or `.jsonl` files yourself.

## Collect
```bash
MODE=short; DAYS=30   # set MODE=detailed / DAYS=<n> from the arguments
W=160; [ "$MODE" = detailed ] && W=200
cap(){ cut -c1-$W | head -n "$1"; }
sec(){ printf '\n== %s ==\n' "$1"; }
n(){ [ "$MODE" = detailed ] && echo "$2" || echo "$1"; }   # n <short> <detailed>
block(){ awk -v h="$2" 'index($0,h)==1{on=1; print; next} on && /^## /{exit} on' "$1"; }  # one "## ..." section
R=$(git rev-parse --show-toplevel 2>/dev/null)   # works in subfolders and worktrees
[ -f PROGRESS.md ] || { [ -n "$R" ] && [ -f "$R/PROGRESS.md" ] && cd "$R"; }
if [ -n "$R" ]; then
  sec GIT
  git log -1 --format='last commit: %cr (%ci)' 2>/dev/null
  git status --short --branch 2>/dev/null | cap $(n 8 20)
  git stash list 2>/dev/null | cap 3
  git log -$(n 4 10) --date=short --format='%h %ad %s' 2>/dev/null | cap 10
fi
if [ -f PROGRESS.md ]; then
  sec "PROGRESS.md (current state)"
  block PROGRESS.md '## Current state' | grep -E '^(## |- |  )' | cap 15
  [ "$MODE" = detailed ] && { sec "PROGRESS.md (latest entry)"; awk '/^## [0-9]{4}-/{c++} c==1' PROGRESS.md | cap 30; }
  for t in $(block PROGRESS.md '## Current state' | grep -oE 'plans/[A-Za-z0-9_.-]+/' | sort -u); do
    [ -f "$t/PROGRESS.md" ] || continue
    sec "$t"
    grep -m1 '^\*\*Status' "$t/PROGRESS.md" | cap 1
    block "$t/PROGRESS.md" '## Current state' | grep -E '^(- |  )' | cap 8
    awk '/^### Next/{on=1; next} on && /^#/{exit} on' "$t/PROGRESS.md" | cap $(n 5 10)
    [ "$MODE" = detailed ] && [ -f "$t/PLAN.md" ] && block "$t/PLAN.md" '## Open questions' | cap 15
    D=$(grep -h '^- \*\*DECISION' "$t/PROGRESS.md" | head -n 5 | cut -c1-$W)
    [ "$MODE" = detailed ] && [ -n "$D" ] && printf -- '-- recent decisions:\n%s\n' "$D"
    if grep -qm1 '^\*\*Status.*Kind:\*\* experiment' "$t/PROGRESS.md"; then   # experiment extras
      tk=$(basename "$t"); lr="tmp/experiments/$tk/last-run.txt"
      if [ -f "$lr" ]; then echo "-- last run: $(head -n 1 "$lr" | cut -c4-) · $(grep -c 'uncommitted:' "$lr") uncommitted files"
      else echo "-- last run: none recorded on this computer"; fi
      [ -f "$t/experiment/run.sh" ] && echo "-- stages: $(grep -oE '^[a-z][a-z0-9_]*\(\)' "$t/experiment/run.sh" | tr -d '()' | tr '\n' ' ')"
      [ -f "$t/RESULTS.md" ] && echo "-- RESULTS.md: $(grep -c '<!-- unreviewed -->' "$t/RESULTS.md") unreviewed sections, $(grep -cE '<[a-z][^>]*>' "$t/RESULTS.md") placeholder lines"
    fi
  done
  [ -f plans/README.md ] && { sec "plans table"; grep -E '^\| \[' plans/README.md | cap 10; }
else
  sec RECENT_FILES
  if [ -n "$R" ]; then   # git knows what changed: no folder walk
    git log --since="$DAYS days ago" --name-only --format= 2>/dev/null | grep . | awk '!s[$0]++' | cap $(n 8 15)
  else                   # shallow and time-boxed
    timeout 10 find . -maxdepth 3 \( -name .git -o -name renv -o -name work -o -name node_modules -o -name .nextflow \) -prune \
      -o -type f -mtime -$DAYS -print 2>/dev/null | head -n 200 | xargs -r ls -t 2>/dev/null | cap $(n 8 15)
  fi
  for f in TODO* NOTES* NEXT* README.md; do [ -f "$f" ] && { sec "$f"; head -n $(n 8 20) "$f" | cut -c1-$W; break; }; done
  if [ -f .radian_history ]; then
    sec RADIAN
    tail -n 1500 .radian_history | awk '
      /^# time:/{t=$3" "$4; next} /^# mode:/{m=$3; next}
      /^\+/{l=substr($0,2); if(l ~ /^(ls\(\)|head\(|str\(|names\(|dim\(|q\(\)|[A-Za-z_.][A-Za-z0-9_.$]*)$/) next;
            if(t!=lt){print "[" t " " m "]"; lt=t} print l}' | cut -c1-120 | tail -n $(n 20 40)
  fi
  for h in .Rhistory .python_history; do [ -f "$h" ] && { sec "$h"; tail -n $(n 15 30) "$h" | cut -c1-$W; }; done
  J=$(ls -t "$HOME/.claude/projects/$(pwd | sed 's/[^a-zA-Z0-9]/-/g')"/*.jsonl 2>/dev/null | head -n 1)
  [ -n "$J" ] && { sec CLAUDE_SESSION; echo "last session: $(ls -l "$J" | awk '{print $6,$7,$8}')"
    tail -c 300000 "$J" | grep -E '"type": ?"user"' | grep -v '"tool_result"' \
      | grep -oE '"content": ?"([^"\\]|\\.){3,300}' | cut -c1-160 | tail -n $(n 3 8); }
fi
[ -f .nextflow.log ] && ! [ PROGRESS.md -nt .nextflow.log ] && { sec NEXTFLOW; tail -c 200000 .nextflow.log | grep -E 'ERROR|Execution (complete|cancelled|aborted)|Workflow completed|Error executing process' | tail -n $(n 3 8) | cut -c1-$W; }
L=$(ls -t slurm-*.out 2>/dev/null | head -n 1); [ -n "$L" ] && { sec "SLURM $L"; tail -n $(n 4 12) "$L" | cut -c1-$W; }
true
```

## Reading the output
- **Experiments** (header says `Kind: experiment`): also say when it last ran and which stages, and how far the write-up is: "RESULTS.md: N unreviewed sections, M placeholder lines" means not written yet (placeholders) or written but not reviewed. Suggest `/write-results` when results exist but the write-up lags, and "mark done" when nothing is unreviewed. "none recorded on this computer" may just mean it ran on another machine (the cluster).
- **With PROGRESS.md:** the Current state blocks say what is active; the task's **Next** is the next step. Use git only to add what the log can't know: uncommitted files, commits newer than the log's date (work that was never logged: say so).
- **Without it:** RADIAN lines are `[UTC time mode]` + code; **convert UTC to local time**. `browse` mode = debugging inside a function. Look for files read/written, models fit, lines retried many times (an error being fixed). CLAUDE_SESSION = the user's last requests to Claude here.
- Skip empty sections silently.

## Write the brief
Simple words (the user is not a native English speaker). Mark guesses with "probably". Use real Markdown headings exactly as below.

### Short mode (default) — strict limits
```
# At a glance
<max 2 sentences, max 35 words total: what you were doing and where you stopped>

## Last active
<date (N days ago) · branch `x` · one status word, e.g. "all committed" / "3 files uncommitted">

## Unfinished
<max 15 words, or "Nothing open.">

## Next step
<one action, max 15 words; with a PROGRESS.md, the task's Next>

_Run `/project-refresher detailed` for more._
```
No explanations of how you know, no counts or IDs unless they are the main point, no extra sections. If there is no PROGRESS.md, add one last line: _No PROGRESS.md here: this brief is a guess from git and history._

### Detailed mode
```
# At a glance
<same as short mode>

## Last active
## What you were doing      <2–4 sentences; name the active task or script>
## Unfinished work          <bullets: task status and open questions, uncommitted files, stashes, failed runs>
## Recent decisions        <up to 5 DECISION lines of the active task, as one short bullet each with date; skip if none>
## Recent timeline          <up to 8 bullets, newest first, from the latest log entry and commits>
## Next steps               <1–3 bullets; the task's Next first>
```
End with one line offering a follow-up: open the task's PLAN.md, show the full diff, or show more history.
