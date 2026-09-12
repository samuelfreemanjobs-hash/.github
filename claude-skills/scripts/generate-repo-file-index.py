#!/usr/bin/env python3
"""Walk claude-skills/ and -build-ai-agents-with-claude/; write docs/REPO-FILE-INDEX.md."""
from __future__ import annotations

import os
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROOTS = [ROOT / "claude-skills", ROOT / "-build-ai-agents-with-claude"]
OUT = ROOT / "claude-skills/docs/REPO-FILE-INDEX.md"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv", "dist", "build"}


def should_skip(p: Path) -> bool:
    return any(part in SKIP_DIRS for part in p.parts)


def collect_files() -> list[tuple[str, int, str]]:
    files: list[tuple[str, int, str]] = []
    for base in ROOTS:
        if not base.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            dp = Path(dirpath)
            if should_skip(dp):
                continue
            for fn in filenames:
                fp = dp / fn
                if should_skip(fp):
                    continue
                files.append((fp.relative_to(ROOT).as_posix(), fp.stat().st_size, base.name))
    files.sort(key=lambda x: x[0].lower())
    return files


def tag(path: str) -> list[str]:
    p = path.lower()
    tags: list[str] = []
    if p.endswith("/skill.md") or p.endswith("skill.md"):
        tags.append("skill")
    if "prompt" in p or "/prompts/" in p or p.endswith("prompts.py"):
        tags.append("prompt")
    if "template" in p:
        tags.append("template")
    if p.endswith((".html", ".jsx", ".tsx")):
        tags.append("web-ui")
    if "deliverable" in p:
        tags.append("deliverable")
    if "/hub/" in p:
        tags.append("hub")
    if "system-prompt" in p or p.endswith("soul.md") or p.endswith("duties.md"):
        tags.append("agent-persona")
    if p.endswith(".csv"):
        tags.append("data-import")
    if "schema" in p or p.endswith(".json"):
        tags.append("schema-config")
    return tags


def main() -> None:
    files = collect_files()
    by_root: dict[str, int] = defaultdict(int)
    by_ext: dict[str, int] = defaultdict(int)
    by_tag: dict[str, list[str]] = defaultdict(list)
    tagged_paths: set[str] = set()

    for path, _size, root in files:
        by_root[root] += 1
        ext = Path(path).suffix.lower() or "(no ext)"
        by_ext[ext] += 1
        tags = tag(path)
        if not tags:
            by_tag["other"].append(path)
        for t in tags:
            by_tag[t].append(path)
            tagged_paths.add(path)

    for k in by_tag:
        by_tag[k] = sorted(set(by_tag[k]), key=str.lower)

    out: list[str] = []
    out.append("# Repository file index (automated)")
    out.append("")
    out.append("> **Scope:** `claude-skills/` + `-build-ai-agents-with-claude/` in this repo.")
    out.append("> **Regenerate:** `python3 claude-skills/scripts/generate-repo-file-index.py`")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append("| Metric | Value |")
    out.append("|--------|-------|")
    out.append(f"| **Total files** | {len(files)} |")
    for root in sorted(by_root.keys()):
        out.append(f"| `{root}/` | {by_root[root]} files |")
    out.append("")
    out.append("### By extension")
    out.append("")
    out.append("| Extension | Count |")
    out.append("|-----------|-------|")
    for ext, n in sorted(by_ext.items(), key=lambda x: (-x[1], x[0])):
        out.append(f"| `{ext}` | {n} |")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Curated buckets (prompt / skill / IP-oriented)")
    out.append("")
    order = [
        "skill",
        "prompt",
        "agent-persona",
        "template",
        "deliverable",
        "hub",
        "web-ui",
        "data-import",
        "schema-config",
        "other",
    ]
    for t in order:
        items = by_tag.get(t, [])
        out.append(f"### `{t}` ({len(items)})")
        out.append("")
        if t == "other":
            out.append("_See full listing below._")
        else:
            for p in items:
                out.append(f"- `{p}`")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Full path listing (every file)")
    out.append("")

    current_top: str | None = None
    current_dir: str | None = None
    rows: list[tuple[str, int]] = []

    def flush_table() -> None:
        nonlocal rows
        if not rows:
            return
        out.append("| File | Bytes |")
        out.append("|------|-------|")
        for name, size in rows:
            out.append(f"| `{name}` | {size} |")
        out.append("")
        rows = []

    for path, size, _root in files:
        parts = path.split("/")
        top = parts[0]
        dir_part = "/".join(parts[:-1])
        name = parts[-1]
        if top != current_top:
            flush_table()
            current_top = top
            current_dir = None
            out.append(f"### `{top}/`")
            out.append("")
        if dir_part != current_dir:
            flush_table()
            current_dir = dir_part
            out.append(f"#### `{dir_part}/`")
            out.append("")
        rows.append((name, size))
    flush_table()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(files)} files)")


if __name__ == "__main__":
    main()
