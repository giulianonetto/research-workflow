#!/usr/bin/env python3
"""Static checks for the skills: frontmatter, plugin manifest, versions, local links, stale names."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ALLOWED_KEYS = {"name", "description", "disable-model-invocation", "license", "allowed-tools", "metadata", "argument-hint"}
STALE = [  # (pattern, files allowed to contain it, why it is stale)
    (r"/to-plan\b", {"skills/setup-workflow/SKILL.md"}, "to-plan was split into new-plan, update-plan and finalize-plan"),
    (r"`/pr`|/pr\b(?![a-z-])", set(), "/pr is not published in the mattpocock plugin"),
    (r"/retro\b", set(), "/retro is not published in the mattpocock plugin"),
    (r"NOTES\.md", set(), "NOTES.md was dropped: brainstorm goes in PROGRESS.md"),
    (r"/update-plan\b", {"skills/setup-workflow/SKILL.md"}, "update-plan was removed: plan changes follow the rules in plans/README.md"),
    (r"/to-tickets\b", {"skills/setup-workflow/SKILL.md"}, "mattpocock-skills is no longer used: /finalize-plan prepares the build"),
    (r"/implement(?![-\w])", {"skills/setup-workflow/SKILL.md"}, "mattpocock-skills is no longer used: /implement-next builds"),
    (r"/grilling\b|/grill-with-docs\b", {"skills/setup-workflow/SKILL.md"}, "mattpocock-skills is no longer used: /grill-plan"),
    (r"/domain-modeling\b", {"skills/setup-workflow/SKILL.md"}, "mattpocock-skills is no longer used: the glossary rules are in plans/README.md"),
    (r"\bpaused\b", {"skills/setup-workflow/SKILL.md"}, "the paused status was removed: a task on hold stays in-progress"),
    (r"## Changes", {"skills/setup-workflow/SKILL.md"}, "## Changes in PLAN.md was replaced by the (plan change) DECISION tag"),
    (r"docs/adr", {"skills/setup-workflow/SKILL.md"}, "ADRs were removed: DECISION lines do the job"),
]
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


# 1. every skill: frontmatter, name = folder, description length, allowed keys
names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
for n in names:
    f = SKILLS / n / "SKILL.md"
    if not f.exists():
        err(f"{n}: no SKILL.md")
        continue
    fm = frontmatter(f.read_text())
    if fm is None:
        err(f"{n}: SKILL.md has no frontmatter")
        continue
    if fm.get("name") != n:
        err(f"{n}: frontmatter name is {fm.get('name')!r}, folder is {n!r}")
    d = fm.get("description", "")
    if not d:
        err(f"{n}: empty description")
    if len(d) > 1024 or "<" in d or ">" in d:
        err(f"{n}: description over 1024 characters or contains angle brackets")
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        err(f"{n}: unexpected frontmatter keys {sorted(extra)}")

# 2. plugin manifest lists every skill, and its version matches the templates
plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
listed = sorted(Path(p).name for p in plugin["skills"])
if listed != names:
    err(f"plugin.json skills {listed} != skill folders {names}")
m = re.search(r"Workflow version: (\S+)", (SKILLS / "setup-workflow/PLANS-README.md").read_text())
if not m or m.group(1) != plugin["version"]:
    err(f"Workflow version in PLANS-README.md ({m and m.group(1)}) != plugin.json version ({plugin['version']})")
if f"## {plugin['version']}" not in (ROOT / "CHANGELOG.md").read_text():
    err(f"CHANGELOG.md has no '## {plugin['version']}' section")

# 3. local links in SKILL.md files (outside code blocks) point to files that exist.
#    Other .md files are templates: their links point into the target project.
for f in SKILLS.glob("*/SKILL.md"):
    body = re.sub(r"```.*?```", "", f.read_text(), flags=re.S)
    for target in re.findall(r"\]\(([^)#\s]+)\)", body):
        if re.match(r"[a-z]+:|\.\./|plans/|/", target) or "<" in target:
            continue  # URLs, and paths that exist only in the target project
        if not (f.parent / target).exists():
            err(f"{f.relative_to(ROOT)}: link to missing file {target}")

# 4. stale names
for f in list(SKILLS.rglob("*.md")) + [ROOT / "docs/examples.html", ROOT / "README.md"]:
    rel = str(f.relative_to(ROOT))
    text = f.read_text()
    for pat, allowed, why in STALE:
        if rel not in allowed and re.search(pat, text):
            err(f"{rel}: matches {pat!r} ({why})")

# 5. skill names are always written /name: flag `name`, <code>name</code> and chips without the slash
bare = re.compile(r"`(%s)`|<code>(%s)</code>|chip cmd\">(%s)<" % ((("|".join(map(re.escape, names))),) * 3))
for f in list(SKILLS.rglob("*.md")) + [ROOT / "docs/examples.html", ROOT / "README.md", ROOT / "CLAUDE.md"]:
    for i, line in enumerate(f.read_text().splitlines(), 1):
        for m in bare.finditer(line):
            err(f"{f.relative_to(ROOT)}:{i}: skill name without the slash: {m.group(0)}")

if errors:
    print("FAILED:")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)
print(f"ok: {len(names)} skills, version {plugin['version']}")
