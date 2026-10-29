#!/usr/bin/env python3
"""Install RoCode without overwriting a skill. Copyright (c) 2026 QFR Studios."""
import argparse
import os
from pathlib import Path
import shutil
import sys


def install(source, skills_dir):
    source = Path(source).resolve()
    skills_dir = Path(skills_dir).expanduser().resolve()
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source is missing SKILL.md")
    target = skills_dir / "rocode"
    # lexists also detects broken symlinks; no implicit replacement.
    if os.path.lexists(target):
        raise FileExistsError(f"An installation already exists: {target}")
    if target == source or source in target.parents:
        raise ValueError("Destination cannot be inside the source skill")
    if any(item.is_symlink() for item in source.rglob("*")):
        raise ValueError("Refusing a source bundle containing symlinks")
    skills_dir.mkdir(parents=True, exist_ok=True)
    # mkdir is exclusive, so a concurrent installation cannot be overwritten.
    target.mkdir()
    shutil.copytree(source, target, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.tmp"))
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Parent skill directory; defaults to ~/.agents/skills")
    args = parser.parse_args()
    try:
        target = install(Path(__file__).resolve().parents[1] / "skills" / "rocode", args.skills_dir)
    except (ValueError, OSError) as exc:
        print(f"RoCode installation stopped: {exc}", file=sys.stderr)
        return 2
    print(f"Installed RoCode by QFR Studios to {target}")
    print("Invoke $rocode in Codex. Restart Codex if the skill does not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
