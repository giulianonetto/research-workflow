#!/usr/bin/env python3
"""Draw the README figures, in a light and a dark version: python3 docs/figures.py

Writes docs/img/flow-{light,dark}.svg (the life of a task), docs/img/runs-{light,dark}.svg
(a build in runs, with its stops) and docs/img/start-{light,dark}.svg (get started). Colors follow docs/workflow.html. Text does not wrap in SVG,
so every line is written by hand: keep card and lane lines under about 20 characters.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "img"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
PAD = 24  # empty space under each figure: GitHub puts no margin under an image

THEMES = {
    "light": dict(fg="#1b2420", muted="#66716b", line="#dfe4e1", card="#ffffff", soft="#f3f6f4", arrow="#b9c2bd",
                  accent="#2f6b4f", accent_bg="#e6f1ea", you="#5b4a8a", you_bg="#eeeaf6",
                  drafting="#a06a00", drafting_bg="#fcf2dc", planned="#1f5596", planned_bg="#e4edf9",
                  inprog="#2f6b4f", inprog_bg="#e6f1ea", done="#4c5752", done_bg="#eceeed"),
    "dark": dict(fg="#e6edf3", muted="#9aa59f", line="#30363d", card="#161b22", soft="#1c2229", arrow="#56605b",
                 accent="#6fcf97", accent_bg="#163324", you="#b9a6ef", you_bg="#2b2342",
                 drafting="#e3b341", drafting_bg="#3a2e10", planned="#79b8ff", planned_bg="#132a4a",
                 inprog="#6fcf97", inprog_bg="#163324", done="#aab4af", done_bg="#262b29"),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, fill="fg", weight=400, family=SANS, anchor="start", spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{{{fill}}}" text-anchor="{anchor}"{sp}>{esc(s)}</text>')


def chip_width(label, kind):
    return len(label) * 7.2 + 18 if kind == "cmd" else len(label) * 7.6 + 18


def chip(x, y, label, kind="cmd"):
    """A command chip (mono, green) or a 'you' chip (caps, purple). (x, y) is the top-left corner."""
    w = chip_width(label, kind)
    if kind == "cmd":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="6" fill="{{accent_bg}}"/>'
                + text(x + w / 2, y + 16.5, label, 12, "accent", 500, MONO, "middle")), w
    return (f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="6" fill="{{you_bg}}"/>'
            + text(x + w / 2, y + 16.5, label.upper(), 11, "you", 600, SANS, "middle", ".05em")), w


def pill(cx, cy, label, color):
    w = len(label) * 8.2 + 24
    return (f'<rect x="{cx - w / 2}" y="{cy - 11}" width="{w}" height="22" rx="11" fill="{{{color}_bg}}"/>'
            + text(cx, cy + 4, label.upper(), 11, color, 600, SANS, "middle", ".06em"))


LOOP = ('<path d="M{x1} {y1} a5 5 0 1 1 -1.5 -3.6" fill="none" stroke="{{{c}}}" stroke-width="1.6" stroke-linecap="round"/>'
        '<path d="M{x2} {y2} v3.2 h-3.2" fill="none" stroke="{{{c}}}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')


def flow():
    W, CW, TOP, CH = 1000, 172, 44, 190
    # the gap after Finalize is wider: it is the gate where the task becomes `planned`
    gaps = [20, 20, 80, 20]
    xs = [0]
    for g in gaps:
        xs.append(xs[-1] + CW + g)
    cards = [
        ("drafting", "Start a plan", "/new-plan", ["Brainstorm and draft.", ("tmp/ → plans/<task>/", "mono"), "+ a PROGRESS.md log"], None),
        ("drafting", "Shape it", "/grill-plan", ["Refine the plan", "with feedback."], "over many sessions"),
        ("drafting", "Finalize", "/finalize-plan", ["Checks plan is ready", "to build: one commit", "per step/sub-step."], None),
        ("inprog", "Build", "/implement-next", ["Claude builds and", "reviews each step,", "up to the next stop."], "one run per stop"),
        ("done", "Close", "/progress", ["Claude reviews the", "branch, opens the PR,", "then marks it done."], None),
    ]
    you = [["Approve the draft."], ["Answer questions."], ["Approve the plan", "and stopping points."],
           ["Look at each stop,", "check with /sandbox."], ["Review + merge PR."]]
    # a cell is its lines, or (number of columns, lines) when it spans several stages
    github = [(2, ["Issue opened → task branch pushed → plan link.", "Plan updates committed to the task branch."]),
              ["Checklist: one box", "per step."], ["Reviewed commit +", "box ticked per step."], ["PR into main", "closes the issue."]]
    out = []
    # status track: drafting over cards 1-3, `planned` is the gate after Finalize
    for status, label, x1, x2 in [("drafting", "drafting", xs[0], xs[2] + CW), ("planned", "planned", xs[2] + CW, xs[3]),
                                  ("inprog", "in-progress", xs[3], xs[3] + CW), ("done", "done", xs[4], xs[4] + CW)]:
        out.append(f'<rect x="{x1}" y="14" width="{x2 - x1}" height="4" rx="2" fill="{{{status}}}"/>')
    for status, label, x1, x2 in [("drafting", "drafting", xs[0], xs[2] + CW), ("planned", "planned", xs[2] + CW, xs[3]),
                                  ("inprog", "in-progress", xs[3], xs[3] + CW), ("done", "done", xs[4], xs[4] + CW)]:
        out.append(pill((x1 + x2) / 2, 16, label, status))
    for i, (status, title, cmd, lines, loop) in enumerate(cards):
        x = xs[i]
        out.append(f'<rect x="{x + .5}" y="{TOP + .5}" width="{CW - 1}" height="{CH}" rx="12" fill="{{card}}" stroke="{{line}}"/>')
        out.append(f'<circle cx="{x + 30}" cy="{TOP + 32}" r="14" fill="{{{status}_bg}}"/>')
        out.append(text(x + 30, TOP + 37, str(i + 1), 14, status, 600, SANS, "middle"))
        out.append(text(x + 52, TOP + 37.5, title, 16, "fg", 600))
        svg, _ = chip(x + 16, TOP + 58, cmd)
        out.append(svg)
        for j, line in enumerate(lines):
            if isinstance(line, tuple):  # a path: mono, a bit smaller
                out.append(text(x + 16, TOP + 108 + j * 19, line[0], 11.5, "muted", 500, MONO))
            else:
                out.append(text(x + 16, TOP + 108 + j * 19, line, 13, "muted"))
        if loop:
            out.append(f'<line x1="{x + 16}" y1="{TOP + CH - 30}" x2="{x + CW - 16}" y2="{TOP + CH - 30}" stroke="{{line}}" stroke-dasharray="3 3"/>')
            lx, ly = x + 22, TOP + CH - 12
            out.append(LOOP.format(x1=lx + 5, y1=ly - 4, x2=lx + 5.5, y2=ly - 11, c=status))
            out.append(text(x + 34, TOP + CH - 10, loop, 12.5, status, 500))
        if i:
            ax, ay = x - gaps[i - 1] / 2 + 3.5, TOP + 32
            out.append(f'<path d="M{ax - 4} {ay - 7} l7 7 l-7 7" fill="none" stroke="{{arrow}}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    # two lanes under the cards: what you do, and what you can follow on GitHub
    y = TOP + CH + 32
    for key, rows, fill, ink, weight in [("YOU", you, "you_bg", "you", 500), ("ON GITHUB", github, "soft", "fg", 400)]:
        color = "you" if key == "YOU" else "muted"
        out.append(text(0, y, key, 11.5, color, 600, SANS, "start", ".09em"))
        top = y + 10
        cells, col = [], 0
        for cell in rows:
            span, lines = cell if isinstance(cell, tuple) else (1, cell)
            cells.append((xs[col], xs[col + span - 1] + CW - xs[col], lines))
            col += span
        h = 25 + (max(len(lines) for _, _, lines in cells) - 1) * 19 + 15
        for x, w, lines in cells:
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="10" fill="{{{fill}}}"/>')
            for j, line in enumerate(lines):
                out.append(text(x + 14, top + 25 + j * 19, line, 13, ink, weight))
        y = top + h + 30
    # the gate: a faint line down the gap after Finalize, broken at the arrow
    gx = xs[2] + CW + gaps[2] / 2
    for y1, y2 in [(30, TOP + 18), (TOP + 48, y - 34)]:
        out.append(f'<line x1="{gx}" y1="{y1}" x2="{gx}" y2="{y2}" stroke="{{planned}}" stroke-width="1.5" stroke-dasharray="3 5" opacity=".55"/>')
    # every session
    by = y + 14
    out.append(text(W / 2, by, "EVERY SESSION", 11.5, "muted", 600, SANS, "middle", ".09em"))
    ry = by + 18
    left, wl = chip(0, ry, "/project-refresher")
    mid_w = 150
    right, wr = chip(0, ry, "/progress")
    total = wl + 60 + mid_w + 60 + wr
    x0 = (W - total) / 2
    out.append(f'<g transform="translate({x0} 0)">{left}</g>')
    out.append(text(x0 + wl / 2, ry + 44, "where was I?", 12.5, "muted", 400, SANS, "middle"))
    d1 = x0 + wl + 10
    out.append(f'<line x1="{d1}" y1="{ry + 12}" x2="{d1 + 40}" y2="{ry + 12}" stroke="{{arrow}}" stroke-width="2" stroke-dasharray="5 5"/>')
    mx = x0 + wl + 60
    out.append(f'<rect x="{mx}" y="{ry - 2}" width="{mid_w}" height="28" rx="14" fill="{{soft}}"/>')
    out.append(text(mx + mid_w / 2, ry + 16.5, "work on the plan", 13, "fg", 400, SANS, "middle"))
    d2 = mx + mid_w + 10
    out.append(f'<line x1="{d2}" y1="{ry + 12}" x2="{d2 + 40}" y2="{ry + 12}" stroke="{{arrow}}" stroke-width="2" stroke-dasharray="5 5"/>')
    rx = mx + mid_w + 60
    out.append(f'<g transform="translate({rx} 0)">{right}</g>')
    out.append(text(rx + wr / 2, ry + 44, "log it, same commit", 12.5, "muted", 400, SANS, "middle"))
    # record keeping: the two logs
    ky = ry + 92
    out.append(text(W / 2, ky, "RECORD KEEPING", 11.5, "muted", 600, SANS, "middle", ".09em"))
    logs = [("PROGRESS.md", "folder log (one per project): active tasks, status changes, PRs, releases"),
            ("plans/<task>/PROGRESS.md", "task log (one per task): work per step, DECISION lines, Next")]
    fw = max(len(f) for f, _ in logs) * 7.2 + 18
    total = fw + 12 + max(len(d) for _, d in logs) * 6.6
    x0 = (W - total) / 2
    for j, (f, d) in enumerate(logs):
        fy = ky + 18 + j * 34
        out.append(f'<rect x="{x0 + fw - (len(f) * 7.2 + 18)}" y="{fy}" width="{len(f) * 7.2 + 18}" height="24" rx="6" fill="{{soft}}"/>')
        out.append(text(x0 + fw - 9, fy + 16.5, f, 12, "fg", 500, MONO, "end"))  # names right-aligned to the descriptions
        out.append(text(x0 + fw + 12, fy + 16.5, d, 12.5, "muted"))
    # any time: check by hand, or change the plan
    ay = ky + 18 + 2 * 34 + 40
    out.append(text(W / 2, ay, "ANY TIME", 11.5, "muted", 600, SANS, "middle", ".09em"))
    sy = ay + 18
    sb, ws = chip(0, sy, "/sandbox")
    note1 = "check by hand"
    tag = "change the plan"
    wt = len(tag) * 7.4 + 28
    total = ws + 10 + len(note1) * 6.6 + 48 + wt
    x0 = (W - total) / 2
    out.append(f'<g transform="translate({x0} 0)">{sb}</g>')
    x1 = x0 + ws + 10
    out.append(text(x1, sy + 16.5, note1, 12.5, "muted"))
    x2 = x1 + len(note1) * 6.6 + 48
    out.append(f'<rect x="{x2}" y="{sy - 2}" width="{wt}" height="28" rx="14" fill="{{soft}}"/>')
    out.append(text(x2 + wt / 2, sy + 16.5, tag, 13, "fg", 400, SANS, "middle"))
    return W, sy + 26, ("The life of a task: start a plan, shape it, finalize it, build it in runs, close it; "
                        "what you do and what you follow on GitHub at each stage."), out


def runs():
    W = 1000
    Y = 104
    seq = [("step", "1"), ("step", "2"), ("stop", ("look at the plots", "you look, then run again")),
           ("step", "3"), ("step", "4"), ("step", "5"), ("step", "6"), ("stop", ("review, PR into main", "you merge it"))]
    xs, x = [], 40
    for kind, _ in seq:
        if kind == "step":
            x += 22
            xs.append(x)
            x += 22 + 62
        else:
            x += 28
            xs.append(x)
            x += 28 + 62
    shift = (W - (xs[-1] + 80)) / 2
    xs = [v + shift for v in xs]
    out = []
    # the line: solid while Claude builds, dashed while it waits for you
    for i in range(len(seq) - 1):
        a, b = xs[i], xs[i + 1]
        dash = ' stroke-dasharray="5 5"' if seq[i][0] == "stop" else ""
        color = "arrow" if seq[i][0] == "stop" else "inprog"
        out.append(f'<line x1="{a}" y1="{Y}" x2="{b}" y2="{Y}" stroke="{{{color}}}" stroke-width="2.5"{dash}/>')
    # run brackets
    for n, (a, b) in enumerate([(0, 2), (3, 7)], 1):
        x1, x2 = xs[a] - 26, xs[b] + 26
        out.append(f'<path d="M{x1} 58 v-8 h{x2 - x1} v8" fill="none" stroke="{{line}}" stroke-width="1.6"/>')
        label = f"/implement-next · run {n}"
        w = len(label) * 7.2 + 20
        out.append(f'<rect x="{(x1 + x2) / 2 - w / 2}" y="38" width="{w}" height="24" rx="6" fill="{{accent_bg}}"/>')
        out.append(text((x1 + x2) / 2, 54.5, label, 12, "accent", 500, MONO, "middle"))
        out.append(text((x1 + x2) / 2, 24, "asks once, then builds without asking", 12, "muted", 400, SANS, "middle"))
    for (kind, label), x in zip(seq, xs):
        if kind == "step":
            out.append(f'<circle cx="{x}" cy="{Y}" r="18" fill="{{inprog_bg}}" stroke="{{inprog}}" stroke-width="2"/>')
            out.append(text(x, Y + 5, label, 14, "inprog", 600, SANS, "middle"))
        else:
            out.append(f'<rect x="{x - 30}" y="{Y - 14}" width="60" height="28" rx="14" fill="{{you_bg}}" stroke="{{you}}" stroke-width="2"/>')
            out.append(text(x, Y + 4.5, "STOP", 11.5, "you", 700, SANS, "middle", ".08em"))
            why, then = label
            out.append(text(x, Y + 40, why, 12.5, "you", 500, SANS, "middle"))
            out.append(text(x, Y + 58, then, 12, "muted", 400, SANS, "middle"))
    # legend
    ly = 206
    out.append(f'<circle cx="{W / 2 - 330}" cy="{ly - 4}" r="8" fill="{{inprog_bg}}" stroke="{{inprog}}" stroke-width="1.6"/>')
    out.append(text(W / 2 - 314, ly, "one step: reviewed, one commit with its log, pushed, box ticked in the issue", 12.5, "muted"))
    return W, ly + 12, "A build in runs: Claude builds steps 1-2, stops for you, then builds steps 3-6 and stops for the PR into main.", out


def start():
    W, CW, GAP, CH = 1000, 290, 65, 150
    cards = [
        ("Install", ("Claude Desktop", "you"), ["Customize → Plugins:", "add the plugin once."]),
        ("Set up a repo", ("/setup-workflow", "cmd"), ["Once per repo.", "Needs a GitHub remote."]),
        ("Start a task", ("/new-plan", "cmd"), ["Say the idea.", "Claude drafts the plan."]),
    ]
    out = []
    for i, (title, (label, kind), lines) in enumerate(cards):
        x = i * (CW + GAP)
        out.append(f'<rect x="{x + .5}" y=".5" width="{CW - 1}" height="{CH}" rx="12" fill="{{card}}" stroke="{{line}}"/>')
        out.append(f'<circle cx="{x + 30}" cy="32" r="14" fill="{{accent_bg}}"/>')
        out.append(text(x + 30, 37, str(i + 1), 14, "accent", 600, SANS, "middle"))
        out.append(text(x + 52, 37.5, title, 16, "fg", 600))
        svg, _ = chip(x + 16, 58, label, kind)
        out.append(svg)
        for j, line in enumerate(lines):
            out.append(text(x + 16, 112 + j * 19, line, 13, "muted"))
        if i:
            ax, ay = x - GAP / 2 + 3, CH / 2
            out.append(f'<path d="M{ax - 4} {ay - 8} l8 8 l-8 8" fill="none" stroke="{{arrow}}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    return W, CH + 1, "Get started: install the plugin, run /setup-workflow once per repo, then /new-plan for each task.", out


def write(name, fig):
    W, H, title, parts = fig()
    for theme, colors in THEMES.items():
        body = "\n".join(parts)
        for k, v in colors.items():
            body = body.replace("{" + k + "}", v)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 {W + 4} {H + 4 + PAD}" width="{W + 4}" height="{H + 4 + PAD}" '
               f'role="img" aria-label="{esc(title)}">\n<title>{esc(title)}</title>\n{body}\n</svg>\n')
        (OUT / f"{name}-{theme}.svg").write_text(svg)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    write("flow", flow)
    write("runs", runs)
    write("start", start)
    print(f"wrote {sorted(p.name for p in OUT.glob('*.svg'))}")
