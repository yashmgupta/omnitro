#!/usr/bin/env python3
"""Check this repository's limited SKILL.md metadata format and directory layout."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELD = re.compile(r"([a-z][a-z-]*):(?: (.*))?\Z")


def check(path: Path) -> list[str]:
    errors = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return [f"{path}: missing YAML frontmatter delimiters"]
    end = lines.index("---", 1)
    fields: dict[str, str] = {}
    current = None
    for line in lines[1:end]:
        if line.startswith("  ") and current and fields[current] == ">":
            continue
        match = FIELD.fullmatch(line)
        if not match:
            errors.append(f"{path}: unsupported metadata line: {line!r}")
            continue
        current, value = match.groups()
        if current in fields:
            errors.append(f"{path}: duplicate metadata field {current}")
        fields[current] = value or ""

    # Collect folded descriptions separately; only the `>` form is used here.
    for index, line in enumerate(lines[1:end], start=1):
        if line == "description: >":
            parts = []
            for continuation in lines[index + 1:end]:
                if not continuation.startswith("  "):
                    break
                parts.append(continuation.strip())
            fields["description"] = " ".join(parts)
            break
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME.fullmatch(name) or len(name) > 64:
        errors.append(f"{path}: invalid skill name {name!r}")
    if name != path.parent.name:
        errors.append(f"{path}: name must match parent directory")
    if not description or len(description) > 1024:
        errors.append(f"{path}: description must be 1-1024 characters")
    if not "\n".join(lines[end + 1:]).strip():
        errors.append(f"{path}: skill instructions are empty")
    return errors


def main() -> int:
    errors = []
    paths = []
    for directory in ("skills", "specialized-skills"):
        root = ROOT / directory
        if not root.is_dir():
            errors.append(f"{root}: missing skill directory")
            continue
        for folder in sorted(root.iterdir()):
            if not folder.is_dir():
                errors.append(f"{folder}: expected a skill directory")
            elif not (folder / "SKILL.md").is_file():
                errors.append(f"{folder}: missing SKILL.md")
            else:
                paths.append(folder / "SKILL.md")
    names = set()
    for path in paths:
        errors.extend(check(path))
        if path.parent.name in names:
            errors.append(f"{path}: duplicate skill directory name")
        names.add(path.parent.name)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(paths)} skill files; no structural errors found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
