"""Move the newest eRank export from the Downloads folder into the run's exports folder.

Usage: python <skill>/scripts/collect_download.py <dest-dir> <name> [--downloads DIR] [--max-age 180]
  e.g. collect_download.py 03_erank/exports japandi-wall-art__keywords
Keeps the file's own extension (.csv or .xlsx). Fails if nothing new arrived, so a missed
click is caught instead of saving the previous seed's file twice.
"""
import argparse
import shutil
import sys
import time
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dest")
    ap.add_argument("name")
    ap.add_argument("--downloads", default=str(Path.home() / "Downloads"))
    ap.add_argument("--max-age", type=float, default=180, help="seconds; only files newer than this count")
    ap.add_argument("--wait", type=float, default=15, help="seconds to wait for the download to finish")
    a = ap.parse_args()
    downloads = Path(a.downloads)
    deadline = time.time() + a.wait
    while True:
        now = time.time()
        files = [p for p in downloads.iterdir()
                 if p.is_file() and p.suffix.lower() in (".csv", ".xlsx", ".xls")
                 and now - p.stat().st_mtime <= a.max_age and not p.name.endswith((".crdownload", ".part"))]
        if files or now > deadline:
            break
        time.sleep(1)
    if not files:
        sys.exit(f"No CSV/XLSX newer than {a.max_age:g}s in {downloads}. Did the export download?")
    newest = max(files, key=lambda p: p.stat().st_mtime)
    dest_dir = Path(a.dest)
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / f"{a.name}{newest.suffix.lower()}"
    shutil.move(str(newest), target)
    print(f"{newest.name} -> {target}")


if __name__ == "__main__":
    main()
