#!/usr/bin/env python3
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent
src_dir = project_root / "src"
if src_dir.exists():
    sys.path.insert(0, str(src_dir))

from yt_comment_scraper.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
