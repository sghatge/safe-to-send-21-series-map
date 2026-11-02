"""Generate the series index (SERIES.md) and a dependency map from registry.json.

One source of truth for all 28 repos: titles, weeks and which episode builds on which.
Rerun after editing registry.json. Standard library only.
"""
import json

GH = "https://github.com/sghatge/"


def load(path="registry.json"):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def validate(reg):
    eps = {e["ep"] for e in reg["episodes"]}
    problems = []
    if eps != set(range(1, 29)):
        problems.append(f"episodes should be 1..28, missing {sorted(set(range(1, 29)) - eps)}")
    for e in reg["episodes"]:
        for d in e["builds_on"]:
            if d not in eps:
                problems.append(f"ep {e['ep']} builds on unknown ep {d}")
            elif d >= e["ep"]:
                problems.append(f"ep {e['ep']} builds on a later episode ({d})")
        if not e["repo"].startswith(f"safe-to-send-{e['ep']:02d}-"):
            problems.append(f"ep {e['ep']} repo name does not match its number")
    return problems


def mermaid(reg):
    lines = ["flowchart LR"]
    for w, name in reg["weeks"].items():
        lines.append(f'  subgraph W{w}["Week {w}: {name}"]')
        for e in reg["episodes"]:
            if str(e["week"]) == w:
                lines.append(f'    E{e["ep"]}["{e["ep"]:02d} {e["title"]}"]')
        lines.append("  end")
    for e in reg["episodes"]:
        for d in e["builds_on"]:
            lines.append(f"  E{d} --> E{e['ep']}")
    return "\n".join(lines)


def series_md(reg):
    out = [f"# {reg['series']}: all 28 repos", "", reg["tagline"] + ".", ""]
    for w, name in reg["weeks"].items():
        out += [f"## Week {w}: {name}", "", "| Ep | Repo | What it shows |", "|---|---|---|"]
        for e in reg["episodes"]:
            if str(e["week"]) == w:
                out.append(f"| {e['ep']:02d} | [{e['repo']}]({GH}{e['repo']}) | {e['title']} |")
        out.append("")
    out += ["## How the episodes connect", "", "```mermaid", mermaid(reg), "```", "",
            "## Foundations", ""] + [f"- [{f['repo']}]({GH}{f['repo']}): {f['title']}" for f in reg["foundations"]]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    reg = load()
    issues = validate(reg)
    if issues:
        raise SystemExit("\n".join(issues))
    with open("SERIES.md", "w", encoding="utf-8") as fh:
        fh.write(series_md(reg))
    built_on = sum(1 for e in reg["episodes"] if e["builds_on"])
    print(f"SERIES.md written: 28 episodes, {built_on} build on an earlier one")
