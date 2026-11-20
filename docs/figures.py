#!/usr/bin/env python3
"""Draw the README figures, in a light and a dark version: python3 docs/figures.py

Writes docs/img/flow-{light,dark}.svg (the life of a task), docs/img/runs-{light,dark}.svg
(a build in runs, with its stops) and docs/img/start-{light,dark}.svg (get started).
The figures have their own look: solid status colors, dark command chips, a line icon per stage.
Text does not wrap in SVG, so every line is written by hand: keep card and lane lines
under about 20 characters.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "img"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
PAD = 24  # empty space under each figure: GitHub puts no margin under an image

# <status> is the solid color, <status>_ink the text on it
THEMES = {
    "light": dict(fg="#1c2233", muted="#596173", line="#d3d8e0", card="#ffffff", soft="#f0f2f5", arrow="#1c2233",
                  cmd_bg="#1c2233", cmd_fg="#ffffff", you="#cf4527", you_ink="#ffffff", you_bg="#fdece7",
                  drafting="#e3a400", drafting_ink="#1c2233", planned="#2b59c3", planned_ink="#ffffff",
                  inprog="#0d8a69", inprog_ink="#ffffff", done="#596173", done_ink="#ffffff"),
    "dark": dict(fg="#eceff4", muted="#a2a9b7", line="#363c48", card="#151a21", soft="#1c2129", arrow="#eceff4",
                 cmd_bg="#2c3547", cmd_fg="#f2f4f8", you="#ff7d5e", you_ink="#0d1117", you_bg="#36201b",
                 drafting="#f2b632", drafting_ink="#0d1117", planned="#7aa2ff", planned_ink="#0d1117",
                 inprog="#36c79b", inprog_ink="#0d1117", done="#a2a9b7", done_ink="#0d1117"),
}

# line icons on a 24-unit grid
ICONS = {
    "bulb": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.6 10.8c.7.5 1.1 1.3 1.1 2.1v.1h5v-.1c0-.8.4-1.6 1.1-2.1A6 6 0 0 0 12 3z"/>',
    "chat": '<path d="M4 5h16v11H10l-5 4v-4H4z"/><path d="M10 9.2a2 2 0 1 1 2.9 1.8c-.6.3-.9.8-.9 1.4"/><circle cx="12" cy="14.3" r=".4"/>',
    "list": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 9.5l1.5 1.5 2.5-2.5M14.5 10h2M8 15.5l1.5 1.5 2.5-2.5M14.5 16h2"/>',
    "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4.5l-3 15"/>',
    "merge": '<circle cx="6" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="13" r="2"/><path d="M6 7v10M6 7c0 4.5 5 6 10 6"/>',
    "download": '<path d="M12 4v11M7.5 10.5L12 15l4.5-4.5M5 19.5h14"/>',
    "folder": '<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5H9l2 2.5h8.5A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>',
    "person": '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c0-3.9 3.1-6 7-6s7 2.1 7 6"/>',
    "branch": '<circle cx="6" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="6" r="2"/><path d="M6 7v10M18 8c0 5-12 3-12 9"/>',
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, fill="fg", weight=400, family=SANS, anchor="start", spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{{{fill}}}" text-anchor="{anchor}"{sp}>{esc(s)}</text>')


def icon(name, x, y, color, size=24):
    """A line icon; (x, y) is the top-left corner."""
    return (f'<g transform="translate({x} {y}) scale({size / 24:.3f})" fill="none" stroke="{{{color}}}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def chip_width(label, kind):
    return len(label) * 7.8 + 20 if kind == "cmd" else len(label) * 7.4 + 18


def chip(x, y, label, kind="cmd"):
    """A command chip (dark, mono, like a key) or a 'you' chip (solid red). (x, y) is the top-left corner."""
    w = chip_width(label, kind)
    if kind == "cmd":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="4" fill="{{cmd_bg}}"/>'
                + text(x + w / 2, y + 16.5, label, 13, "cmd_fg", 500, MONO, "middle")), w
    return (f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="4" fill="{{you}}"/>'
            + text(x + w / 2, y + 16.5, label, 12.5, "you_ink", 700, SANS, "middle")), w


def box(x, y, w, h, fill="card"):
    """An outlined box; the stroke sits inside (x, y, w, h)."""
    return f'<rect x="{x + .75}" y="{y + .75}" width="{w - 1.5}" height="{h - 1.5}" rx="4" fill="{{{fill}}}" stroke="{{line}}" stroke-width="1.5"/>'


def card(x, y, w, h, color):
    """A card with a thin colored top edge."""
    return (box(x, y, w, h)
            + f'<path d="M{x} {y + 4} a4 4 0 0 1 4 -4 h{w - 8} a4 4 0 0 1 4 4 v2 h-{w} z" fill="{{{color}}}"/>')


def chevron(x, y, color="arrow"):
    """A '>' arrow; (x, y) is its tip."""
    return (f'<path d="M{x - 7} {y - 7} l7 7 l-7 7" fill="none" stroke="{{{color}}}" stroke-width="2.4" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def heading(cx, y, label):
    return text(cx, y, label, 14, "fg", 700, SANS, "middle")


LOOP = ('<path d="M{x1} {y1} a5 5 0 1 1 -1.5 -3.6" fill="none" stroke="{{{c}}}" stroke-width="1.6" stroke-linecap="round"/>'
        '<path d="M{x2} {y2} v3.2 h-3.2" fill="none" stroke="{{{c}}}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')


def flow():
    W, CW, TOP, CH = 1000, 172, 52, 196
    # the gap after Finalize is wider: it is the gate where the task becomes `planned`
    gaps = [20, 20, 80, 20]
    xs = [0]
    for g in gaps:
        xs.append(xs[-1] + CW + g)
    cards = [
        ("drafting", "Start a plan", "/new-plan", "bulb", ["Brainstorm and draft.", ("tmp/ → plans/<task>/", "mono"), "+ a PROGRESS.md log"], None),
        ("drafting", "Shape it", "/grill-plan", "chat", ["Refine the plan", "with feedback."], "over many sessions"),
        ("drafting", "Finalize", "/finalize-plan", "list", ["Checks plan is ready", "to build: one commit", "per step/sub-step."], None),
        ("inprog", "Build", "/implement-next", "code", ["Claude builds and", "reviews each step,", "up to the next stop."], "one run per stop"),
        ("done", "Close", "/progress", "merge", ["Claude reviews the", "branch, opens the PR,", "then marks it done."], None),
    ]
    you = [["Approve the draft."], ["Answer questions,", "improve the plan."], ["Approve the plan", "and stopping points."],
           ["Look at each stop,", "check with /sandbox."], ["Review + merge PR."]]
    # a cell is its lines, or (number of columns, lines) when it spans several stages
    github = [(2, ["Issue opened → task branch pushed → plan link.", "Plan updates committed to the task branch."]),
              ["Checklist: one box", "per step."], ["Reviewed commit +", "box ticked per step."], ["PR into main", "closes the issue."]]
    out = []
    # status band: one solid bar, cut into the four statuses; `planned` is the gate after Finalize
    segs = [("drafting", "drafting", xs[0], xs[2] + CW), ("planned", "planned", xs[2] + CW, xs[3]),
            ("inprog", "in progress", xs[3], xs[4]), ("done", "done", xs[4], xs[4] + CW)]
    for k, (status, label, x1, x2) in enumerate(segs):
        if k in (0, 3):  # round only the outer ends
            sx = x2 - 6 if k == 0 else x1
            out.append(f'<rect x="{x1}" y="8" width="{x2 - x1}" height="26" rx="4" fill="{{{status}}}"/>'
                       f'<rect x="{sx}" y="8" width="6" height="26" fill="{{{status}}}"/>')
        else:
            out.append(f'<rect x="{x1}" y="8" width="{x2 - x1}" height="26" fill="{{{status}}}"/>')
        out.append(text((x1 + x2) / 2, 26, label, 13, f"{status}_ink", 700, SANS, "middle"))
    for i, (status, title, cmd, ic, lines, loop) in enumerate(cards):
        x = xs[i]
        out.append(card(x, TOP, CW, CH, status))
        out.append(text(x + 15, TOP + 44, str(i + 1), 30, status, 800))
        out.append(text(x + 38, TOP + 40, title, 16, "fg", 700))
        out.append(icon(ic, x + CW - 38, TOP + 19, status))
        svg, _ = chip(x + 16, TOP + 60, cmd)
        out.append(svg)
        for j, line in enumerate(lines):
            if isinstance(line, tuple):  # a path: mono, a bit smaller
                out.append(text(x + 16, TOP + 110 + j * 19, line[0], 11.5, "muted", 500, MONO))
            else:
                out.append(text(x + 16, TOP + 110 + j * 19, line, 13, "muted"))
        if loop:
            out.append(f'<line x1="{x + 16}" y1="{TOP + CH - 30}" x2="{x + CW - 16}" y2="{TOP + CH - 30}" stroke="{{line}}" stroke-dasharray="3 3"/>')
            lx, ly = x + 22, TOP + CH - 12
            out.append(LOOP.format(x1=lx + 5, y1=ly - 4, x2=lx + 5.5, y2=ly - 11, c=status))
            out.append(text(x + 34, TOP + CH - 10, loop, 12.5, status, 600))
        if i:
            out.append(chevron(x - gaps[i - 1] / 2 + 3.5, TOP + 36))
    # two lanes under the cards: what you do, and what you can follow on GitHub
    y = TOP + CH + 36
    for key, ic, rows, fill, color, weight in [("You", "person", you, "you_bg", "you", 500),
                                               ("On GitHub", "branch", github, "soft", "muted", 400)]:
        out.append(icon(ic, 0, y - 15, color, 18))
        out.append(text(24, y, key, 14, color, 700))
        top = y + 10
        cells, col = [], 0
        for cell in rows:
            span, lines = cell if isinstance(cell, tuple) else (1, cell)
            cells.append((xs[col], xs[col + span - 1] + CW - xs[col], lines))
            col += span
        h = 25 + (max(len(lines) for _, _, lines in cells) - 1) * 19 + 15
        for x, w, lines in cells:
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="4" fill="{{{fill}}}"/>')
            if key == "You":  # a red bar down the left edge
                out.append(f'<rect x="{x}" y="{top}" width="4" height="{h}" fill="{{you}}"/>')
            for j, line in enumerate(lines):
                out.append(text(x + 16, top + 25 + j * 19, line, 13, "fg", weight))
        y = top + h + 34
    # the gate: a dashed line down the gap after Finalize, broken at the arrow
    gx = xs[2] + CW + gaps[2] / 2
    for y1, y2 in [(34, TOP + 26), (TOP + 50, y - 38)]:
        out.append(f'<line x1="{gx}" y1="{y1}" x2="{gx}" y2="{y2}" stroke="{{planned}}" stroke-width="2" stroke-dasharray="4 5"/>')
    # every session
    by = y + 10
    out.append(heading(W / 2, by, "Every session"))
    ry = by + 16
    left, wl = chip(0, ry, "/project-refresher")
    right, wr = chip(0, ry, "/progress")
    mid_w = 150
    total = wl + 60 + mid_w + 60 + wr
    x0 = (W - total) / 2
    out.append(f'<g transform="translate({x0} 0)">{left}</g>')
    out.append(text(x0 + wl / 2, ry + 44, "where was I?", 12.5, "muted", 400, SANS, "middle"))
    mx = x0 + wl + 60
    for d in (x0 + wl + 10, mx + mid_w + 10):
        out.append(f'<line x1="{d}" y1="{ry + 12}" x2="{d + 40}" y2="{ry + 12}" stroke="{{muted}}" stroke-width="2" stroke-dasharray="4 5"/>')
    out.append(box(mx, ry - 2, mid_w, 28))
    out.append(text(mx + mid_w / 2, ry + 16.5, "plan or build", 13, "fg", 500, SANS, "middle"))
    rx = mx + mid_w + 60
    out.append(f'<g transform="translate({rx} 0)">{right}</g>')
    out.append(text(rx + wr / 2, ry + 44, "log it, same commit", 12.5, "muted", 400, SANS, "middle"))
    # record keeping: the two logs
    ky = ry + 90
    out.append(heading(W / 2, ky, "Record keeping"))
    logs = [("PROGRESS.md", "folder log (one per project): active tasks, status changes, PRs, releases"),
            ("plans/<task>/PROGRESS.md", "task log (one per task): work per step, DECISION lines, Next")]
    fw = max(len(f) for f, _ in logs) * 7.8 + 20
    total = fw + 12 + max(len(d) for _, d in logs) * 6.6
    x0 = (W - total) / 2
    for j, (f, d) in enumerate(logs):
        fy = ky + 16 + j * 34
        w = len(f) * 7.8 + 20
        out.append(f'<rect x="{x0 + fw - w}" y="{fy}" width="{w}" height="24" rx="4" fill="{{soft}}"/>')
        out.append(text(x0 + fw - 10, fy + 16.5, f, 13, "fg", 500, MONO, "end"))  # names right-aligned to the descriptions
        out.append(text(x0 + fw + 12, fy + 16.5, d, 12.5, "muted"))
    # any time: check by hand, or change the plan
    ay = ky + 16 + 2 * 34 + 38
    out.append(heading(W / 2, ay, "Any time"))
    sy = ay + 16
    sb, ws = chip(0, sy, "/sandbox")
    note1, tag = "check by hand", "change the plan"
    wt = len(tag) * 7.4 + 28
    total = ws + 10 + len(note1) * 6.6 + 48 + wt
    x0 = (W - total) / 2
    out.append(f'<g transform="translate({x0} 0)">{sb}</g>')
    x1 = x0 + ws + 10
    out.append(text(x1, sy + 16.5, note1, 12.5, "muted"))
    x2 = x1 + len(note1) * 6.6 + 48
    out.append(box(x2, sy - 2, wt, 28))
    out.append(text(x2 + wt / 2, sy + 16.5, tag, 13, "fg", 500, SANS, "middle"))
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
            x += 30
            xs.append(x)
            x += 30 + 62
    shift = (W - (xs[-1] + 80)) / 2
    xs = [v + shift for v in xs]
    out = []
    # the line: solid while Claude builds, dashed while it waits for you
    for i in range(len(seq) - 1):
        a, b = xs[i], xs[i + 1]
        dash = ' stroke-dasharray="5 6"' if seq[i][0] == "stop" else ""
        color = "muted" if seq[i][0] == "stop" else "inprog"
        width = 2 if seq[i][0] == "stop" else 3.5
        out.append(f'<line x1="{a}" y1="{Y}" x2="{b}" y2="{Y}" stroke="{{{color}}}" stroke-width="{width}"{dash}/>')
    # run brackets
    for n, (a, b) in enumerate([(0, 2), (3, 7)], 1):
        x1, x2 = xs[a] - 28, xs[b] + 28
        out.append(f'<path d="M{x1} 58 v-8 h{x2 - x1} v8" fill="none" stroke="{{muted}}" stroke-width="1.6"/>')
        svg, w = chip(0, 38, f"/implement-next · run {n}")
        out.append(f'<g transform="translate({(x1 + x2) / 2 - w / 2} 0)">{svg}</g>')
        out.append(text((x1 + x2) / 2, 24, "asks once, then builds without asking", 12.5, "muted", 400, SANS, "middle"))
    for (kind, label), x in zip(seq, xs):
        if kind == "step":
            out.append(f'<circle cx="{x}" cy="{Y}" r="18" fill="{{inprog}}"/>')
            out.append(text(x, Y + 5.5, label, 15, "inprog_ink", 800, SANS, "middle"))
        else:
            out.append(f'<rect x="{x - 32}" y="{Y - 15}" width="64" height="30" rx="4" fill="{{you}}"/>')
            out.append(text(x, Y + 5, "Stop", 14, "you_ink", 800, SANS, "middle"))
            why, then = label
            out.append(text(x, Y + 42, why, 13, "you", 700, SANS, "middle"))
            out.append(text(x, Y + 60, then, 12.5, "muted", 400, SANS, "middle"))
    # legend
    ly = 206
    out.append(f'<circle cx="{W / 2 - 330}" cy="{ly - 4}" r="8" fill="{{inprog}}"/>')
    out.append(text(W / 2 - 314, ly, "one step: reviewed, one commit with its log, pushed, box ticked in the issue", 12.5, "muted"))
    return W, ly + 12, "A build in runs: Claude builds steps 1-2, stops for you, then builds steps 3-6 and stops for the PR into main.", out


def start():
    W, CW, GAP, CH = 1000, 290, 65, 156
    cards = [
        ("Install", "download", ("Claude Desktop", "you"), ["Customize → Plugins:", "add the plugin once."]),
        ("Set up a repo", "folder", ("/setup-workflow", "cmd"), ["Once per repo.", "Needs a GitHub remote."]),
        ("Start a task", "bulb", ("/new-plan", "cmd"), ["Say the idea.", "Claude drafts the plan."]),
    ]
    out = []
    for i, (title, ic, (label, kind), lines) in enumerate(cards):
        x = i * (CW + GAP)
        out.append(card(x, 0, CW, CH, "inprog"))
        out.append(text(x + 16, 44, str(i + 1), 30, "inprog", 800))
        out.append(text(x + 40, 40, title, 16, "fg", 700))
        out.append(icon(ic, x + CW - 40, 19, "inprog"))
        svg, _ = chip(x + 16, 62, label, kind)
        out.append(svg)
        for j, line in enumerate(lines):
            out.append(text(x + 16, 114 + j * 19, line, 13, "muted"))
        if i:
            out.append(chevron(x - GAP / 2 + 3.5, CH / 2))
    return W, CH, "Get started: install the plugin, run /setup-workflow once per repo, then /new-plan for each task.", out


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
