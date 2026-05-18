#!/usr/bin/env python3
from __future__ import annotations

import os
import plistlib
import shlex
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).parent.resolve()
DIST_DIR = REPO_ROOT / "dist"
APP_NAME = "AltToNotes Viewer"
APP_PATH = DIST_DIR / f"{APP_NAME}.app"
CONTENTS_DIR = APP_PATH / "Contents"
MACOS_DIR = CONTENTS_DIR / "MacOS"
LAUNCHER_PATH = MACOS_DIR / APP_NAME
INFO_PLIST_PATH = CONTENTS_DIR / "Info.plist"
LOG_PATH = "/tmp/alttonotes-viewer.log"


def build_launcher_script() -> str:
    repo_root = str(REPO_ROOT)
    viewer_path = str(REPO_ROOT / "viewer.py")
    return f"""#!/bin/zsh
set -euo pipefail
cd {shlex.quote(repo_root)}
/usr/bin/python3 {shlex.quote(viewer_path)} --root {shlex.quote(repo_root)} >{shlex.quote(LOG_PATH)} 2>&1 &
"""


def build_info_plist() -> dict:
    return {
        "CFBundleDisplayName": APP_NAME,
        "CFBundleExecutable": APP_NAME,
        "CFBundleIdentifier": "io.altalt.alttonotes.viewer",
        "CFBundleName": APP_NAME,
        "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": "1.0",
        "CFBundleVersion": "1",
        "LSMinimumSystemVersion": "11.0",
    }


def main():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    if APP_PATH.exists():
        shutil.rmtree(APP_PATH)

    MACOS_DIR.mkdir(parents=True, exist_ok=True)

    LAUNCHER_PATH.write_text(build_launcher_script(), encoding="utf-8")
    os.chmod(LAUNCHER_PATH, 0o755)

    with INFO_PLIST_PATH.open("wb") as handle:
        plistlib.dump(build_info_plist(), handle)

    print(f"Built: {APP_PATH}")
    print(f"Launch log: {LOG_PATH}")


if __name__ == "__main__":
    main()
