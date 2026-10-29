#!/usr/bin/env python3
"""Local package integrity checks. Copyright (c) 2026 QFR Studios."""
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "rocode"


def check(root=ROOT):
    root = Path(root).resolve()
    skill = root / "skills" / "rocode"
    errors = []
    required = ["SKILL.md", "agents/openai.yaml", "LICENSE", "NOTICE", "scripts/brief.py",
                "assets/brief.example.json", "assets/Geometry.luau", "assets/SceneAudit.luau"]
    for name in required:
        if not (skill / name).is_file():
            errors.append(f"Missing skill resource: {name}")
    if errors:
        return errors
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match or not re.search(r"^name: rocode$", match[1], re.M):
        errors.append("Missing or invalid skill frontmatter")
    if not match or not re.search(r"^description: .+", match[1], re.M):
        errors.append("Missing description")
    for item in root.rglob("*"):
        if (not item.is_file() or ".git" in item.parts or "__pycache__" in item.parts
                or item.relative_to(root).parts[0] in {"work", "dist", ".venv"}):
            continue
        if item.suffix in {".md", ".luau", ".py", ".yaml", ".json"} or item.name in {"LICENSE", "NOTICE"}:
            content = item.read_text(encoding="utf-8")
            if "QFR Studios" not in content:
                errors.append(f"Missing attribution: {item.relative_to(root)}")
            if item.suffix == ".md":
                for destination in re.findall(r"\]\(([^)]+)\)", content):
                    if "://" in destination or destination.startswith("#"):
                        continue
                    destination = unquote(destination.split("#")[0])
                    target = (item.parent / destination).resolve()
                    if not target.is_relative_to(root) or not target.exists():
                        errors.append(f"Broken/escaping reference in {item.relative_to(root)}: {destination}")
    for name in ["LICENSE", "NOTICE"]:
        if (root / name).read_bytes() != (skill / name).read_bytes():
            errors.append(f"Installed {name} differs from repository {name}")
    spec = importlib.util.spec_from_file_location("rocode_brief_check", skill / "scripts" / "brief.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.validate(json.loads((skill / "assets" / "brief.example.json").read_text(encoding="utf-8")))
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid example brief: {exc}")
    return errors


if __name__ == "__main__":
    failures = check()
    for failure in failures:
        print(f"FAIL: {failure}")
    print("RoCode package checks passed" if not failures else f"{len(failures)} package issues")
    raise SystemExit(bool(failures))
