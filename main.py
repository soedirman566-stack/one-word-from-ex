#!/usr/bin/env python3
"""Entry for make.fun 'One Word From Your Ex'.

Reads the single word stored in line.txt (next to this file) and writes
it, bare and unadorned, to entry.txt inside the output directory. The
output directory is only ever created and written into -- never cleared
or deleted, because the grader mounts it read-only.
"""

import os
import sys
from pathlib import Path

WORD_FILE = Path(__file__).resolve().parent / "line.txt"
ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> Path:
    """Where the entry goes: argv[1] wins, then $OUTPUT_DIR, else /output."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path(os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def read_word() -> str:
    """Return the one word from line.txt, stripped of surrounding space."""
    return WORD_FILE.read_text(encoding="utf-8").strip()


def write_entry(out_dir: Path) -> Path:
    """Write the word into out_dir/entry.txt and return that path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_NAME
    target.write_text(read_word(), encoding="utf-8")
    return target


def main() -> int:
    written = write_entry(output_dir())
    print(f"wrote {written}: {read_word()!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
