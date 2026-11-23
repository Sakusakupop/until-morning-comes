#!/usr/bin/env python3
"""Check tracked Unity assets for matching .meta files."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ASSETS_PATH = "until-morning-comes/Assets"


def tracked_asset_paths() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", f"{ASSETS_PATH}/"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return {os.fsdecode(path) for path in result.stdout.split(b"\0") if path}


def is_empty_folder_meta(path: str) -> bool:
    meta_path = Path(path)
    try:
        contents = meta_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    return any(line.strip() == "folderAsset: yes" for line in contents.splitlines())


def main() -> int:
    paths = tracked_asset_paths()
    assets = {path for path in paths if not path.endswith(".meta")}
    metas = paths - assets
    missing_metas = sorted(path for path in assets if f"{path}.meta" not in metas)

    orphaned_metas = []
    for meta_path in metas:
        asset_path = meta_path[:-5]
        if asset_path in assets:
            continue
        if any(path.startswith(f"{asset_path}/") for path in assets):
            continue
        if is_empty_folder_meta(meta_path):
            continue
        orphaned_metas.append(meta_path)

    if not missing_metas and not orphaned_metas:
        print(f"Unity asset .meta check passed for {ASSETS_PATH}/.")
        return 0

    print("Unity asset .meta check failed.", file=sys.stderr)
    for path in missing_metas:
        print(f"Missing .meta file for tracked asset: {path}", file=sys.stderr)
    for path in sorted(orphaned_metas):
        print(f"Tracked .meta file has no matching asset or folder: {path}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
