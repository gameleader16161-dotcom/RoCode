#!/usr/bin/env python3
"""RoCode design brief CLI. Copyright (c) 2026 QFR Studios. MIT License."""
import argparse
import datetime as dt
import json
from pathlib import Path
import sys

VERSION = 1
QUESTIONS = [
    ("style", "كيف بدك ستايل التصميم؟ كلاسيكي، مستقبلي، كرتوني، واقعي، فانتازي، أو خليط؟"),
    ("treatment", "بدك التزام قوي بالستايل أو الحقبة، ولا نسخة مطوّرة بلمسة أحدث؟"),
    ("gameplay", "شو نوع اللعب أو وظيفة الواجهة الأساسية؟"),
    ("setting", "وين بدك العالم؟ جزيرة، مدينة، غابة، فضاء، أو مكان ثاني؟"),
    ("scope", "شو حجم المطلوب؟ لوبي، مرحلة، عالم بمناطق، أو واجهات محددة؟"),
    ("devices", "على أي أجهزة لازم تشتغل التجربة؟"),
    ("audience", "لمين التجربة، وبأي لغة؟"),
    ("journey", "شو أول شي اللاعب يشوفه ويعمله؟"),
    ("zones", "شو المناطق الأساسية وكيف بدك ترتبط؟"),
    ("landmark", "شو العنصر المميز اللي بدك اللاعب يتذكره؟"),
    ("mood", "شو الجو والإضاءة اللي بدك إياهم؟"),
    ("palette", "شو الألوان اللي بتحبها أو بدك نتجنبها؟"),
    ("surfaces", "كيف بدك نوزع الخامات ونقشات الأسطح؟"),
    ("assets", "عندك باك أصول؟ ونبحث عن أصول مجانية مناسبة في الـToolbox؟"),
    ("motion", "شو العناصر اللي بدك فيها حركة؟"),
    ("gui", "شو الواجهات المطلوبة، أو ما بدك GUI؟"),
    ("gui_style", "شو ستايل الواجهة والأيقونات اللي بتحبه؟"),
    ("references", "عندك مراجع بتحبها؟ شو بالتحديد بتحب فيها؟"),
    ("constraints", "شو لازم نحافظ عليه، وشو ما بدك نعمله؟"),
]
FIELDS = {key for key, _ in QUESTIONS}
SOURCES = {"user", "delegated", "proposed"}
CRITICAL = {"style", "gameplay", "scope", "devices"}
MAP_ONLY = {"setting", "zones", "landmark", "surfaces"}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def new_brief(kind):
    return {"schema_version": VERSION, "skill": "rocode", "author": "QFR Studios",
            "kind": kind, "phase": "interview", "decisions": {}, "history": [],
            "checkpoint": None, "assets": [], "verification": []}


def validate(data):
    if not isinstance(data, dict) or data.get("schema_version") != VERSION:
        raise ValueError("Unsupported brief schema; expected version 1")
    if data.get("kind") not in {"map", "gui"}:
        raise ValueError("kind must be map or gui")
    if data.get("phase") not in {"interview", "ready", "building", "review", "delivered"}:
        raise ValueError("Invalid phase")
    if not isinstance(data.get("decisions"), dict) or not isinstance(data.get("history"), list):
        raise ValueError("decisions must be an object and history an array")
    for field, entry in data["decisions"].items():
        if field not in FIELDS or not isinstance(entry, dict):
            raise ValueError(f"Invalid decision field: {field}")
        if entry.get("source") not in SOURCES:
            raise ValueError(f"Invalid decision source: {field}")
        if not isinstance(entry.get("value"), str) or not entry["value"].strip():
            raise ValueError(f"Decision needs a nonempty string: {field}")
    checkpoint = data.get("checkpoint")
    if data["phase"] != "interview":
        if not isinstance(checkpoint, dict) or checkpoint.get("mode") not in {"agreed", "delegated", "start-now"}:
            raise ValueError("A build phase needs a valid user-start checkpoint")
        if not isinstance(checkpoint.get("user_quote"), str) or not checkpoint["user_quote"].strip():
            raise ValueError("A checkpoint needs the actual user instruction")
        if not isinstance(checkpoint.get("unresolved"), list):
            raise ValueError("A checkpoint needs an unresolved topics list")
    return data


def load(path):
    return validate(json.loads(path.read_text(encoding="utf-8-sig")))


def save(path, data):
    validate(data)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    # Exclusive creation refuses a concurrent writer instead of overwriting its file.
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    temporary.replace(path)


def pending(data):
    skipped = MAP_ONLY if data["kind"] == "gui" else set()
    gui = data["decisions"].get("gui", {})
    no_gui = gui.get("value", "").strip().casefold() if gui.get("source") in {"user", "delegated"} else ""
    if no_gui in {"none", "no", "لا", "بدون", "بدون واجهة", "بدون gui"}:
        skipped = skipped | {"gui_style"}
    if data["kind"] == "gui":
        skipped = skipped | {"gui"}
    return [(field, question) for field, question in QUESTIONS
            if field not in skipped and
            data["decisions"].get(field, {}).get("source") not in {"user", "delegated"}]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=Path("work/rocode/brief.json"))
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--kind", choices=["map", "gui"], default="map")
    update = commands.add_parser("set")
    update.add_argument("field", choices=sorted(FIELDS))
    update.add_argument("value")
    update.add_argument("--source", choices=sorted(SOURCES), default="user")
    commands.add_parser("next")
    commands.add_parser("validate")
    ready = commands.add_parser("ready")
    ready.add_argument("--mode", choices=["agreed", "delegated", "start-now"], required=True)
    ready.add_argument("--user-quote", required=True,
                       help="Actual user instruction to start; not inferred permission")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            if args.file.exists():
                raise ValueError("Brief already exists; read it instead of reinitializing")
            save(args.file, new_brief(args.kind))
            result = {"created": str(args.file), "phase": "interview"}
        else:
            data = load(args.file)
            if args.command == "set":
                if not args.value.strip():
                    raise ValueError("An empty answer cannot complete a design topic")
                old = data["decisions"].get(args.field)
                data["decisions"][args.field] = {"value": args.value, "source": args.source}
                data["history"].append({"at": now(), "field": args.field, "previous": old,
                                        "value": args.value, "source": args.source})
                # A changed design decision invalidates the old readiness checkpoint.
                data["phase"], data["checkpoint"] = "interview", None
                save(args.file, data)
                result = {"saved": args.field, "source": args.source}
            elif args.command == "next":
                remaining = pending(data)
                result = {"phase": data["phase"], "remaining": len(remaining),
                          "next": ({"field": remaining[0][0], "question": remaining[0][1]}
                                   if remaining and data["phase"] == "interview" else None),
                          "can_offer_build": not (CRITICAL & {k for k, _ in remaining})}
            elif args.command == "ready":
                if not args.user_quote.strip():
                    raise ValueError("Use the user's actual start/delegation instruction")
                unresolved = [key for key, _ in pending(data)]
                if args.mode == "agreed" and (CRITICAL & set(unresolved)):
                    raise ValueError("Core choices unresolved; ask or record explicit delegation/start-now")
                data["checkpoint"] = {"at": now(), "mode": args.mode,
                                      "user_quote": args.user_quote, "unresolved": unresolved}
                data["phase"] = "ready"
                save(args.file, data)
                result = {"phase": "ready", "mode": args.mode, "unresolved": unresolved}
            else:
                result = {"valid": True, "phase": data["phase"]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"RoCode: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
