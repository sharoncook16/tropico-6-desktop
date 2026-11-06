"""Tropico 6 Desktop — A local helper for Tropico 6 data folders, config and export files, and photo albums on Windows and macOS."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='tropico_6_desktop',
        description='A local helper for Tropico 6 data folders, config and export files, and photo albums on Windows and macOS.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Tropico 6 Desktop')
    print('Keep the Tropico 6 data folder tidy before an update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# wip (2026-11-03)
# update note (2026-11-03)
# cleanup (2026-11-04)
# polish (2026-11-04)
# refactor bit (2026-11-05)
# update note (2026-11-06)
# small fix (2026-11-06)
