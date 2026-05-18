from __future__ import annotations

import re
from pathlib import Path

SKIP_DIRS = {"__pycache__", ".git", "node_modules", ".omc", "dist"}
NOTE_SUFFIXES = {".pdf", ".md"}
ROOT_LEVEL_MARKDOWN_EXCLUDES = {"README.md", "README.restored.md"}


def natural_key(path: Path | str):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r"(\d+)", str(path))]


def _should_skip(rel_path: Path) -> bool:
    return any(part.startswith(".") or part in SKIP_DIRS for part in rel_path.parts)


def _is_note_candidate(rel_path: Path) -> bool:
    suffix = rel_path.suffix.lower()
    if suffix not in NOTE_SUFFIXES or _should_skip(rel_path):
        return False
    if len(rel_path.parts) == 1 and suffix == ".md" and rel_path.name in ROOT_LEVEL_MARKDOWN_EXCLUDES:
        return False
    return True


def build_file_groups(root: Path) -> list[dict]:
    entries: dict[str, dict] = {}

    for file_path in sorted(root.glob("**/*"), key=natural_key):
        if not file_path.is_file():
            continue

        rel_path = file_path.relative_to(root)
        if not _is_note_candidate(rel_path):
            continue

        rel_key = rel_path.with_suffix("")
        key = rel_key.as_posix()
        entry = entries.setdefault(
            key,
            {
                "stem": rel_key.name,
                "pdf": None,
                "md": None,
                "has_pdf": False,
                "has_notes": False,
                "course": rel_path.parts[0] if len(rel_path.parts) > 1 else ".",
            },
        )

        rel_posix = rel_path.as_posix()
        if rel_path.suffix.lower() == ".pdf":
            entry["pdf"] = rel_posix
            entry["has_pdf"] = True
        elif rel_path.suffix.lower() == ".md":
            entry["md"] = rel_posix
            entry["has_notes"] = True

    grouped: dict[str, list] = {}
    for key in sorted(entries, key=natural_key):
        entry = entries[key]
        course = entry.pop("course")
        grouped.setdefault(course, []).append(entry)

    return [{"course": course, "files": files} for course, files in grouped.items()]
