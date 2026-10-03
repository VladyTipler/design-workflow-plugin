#!/usr/bin/env python3
"""Decode mojibake snapshot files from agent-browser (Out-File on Windows).

UTF-8 bytes were mis-decoded as CP866, so invert: encode('cp866') -> decode('utf-8').

Usage:
  python decode_mojibake.py <in_dir_or_file> [out_dir]

Defaults: in = current dir, out = <in>/../<in>-decoded (or sibling -decoded for a file).
"""
import pathlib
import sys


def fix_text(raw: str) -> str:
    raw = raw.lstrip("\ufeff")
    # Already clean UTF-8 Cyrillic? Skip conversion.
    if "и" in raw and "в" in raw and "╨" not in raw and "тА" not in raw:
        return raw
    return raw.encode("cp866", errors="replace").decode("utf-8", errors="replace")


def main() -> None:
    src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    if src.is_file():
        out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.parent.parent / (src.parent.name + "-decoded")
        out.mkdir(parents=True, exist_ok=True)
        fixed = fix_text(src.read_text(encoding="utf-8", errors="replace"))
        (out / src.name).write_text(fixed, encoding="utf-8")
        print(f"{src.name}: -> {out / src.name}")
        return
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.parent / (src.name + "-decoded")
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob("*.txt")):
        fixed = fix_text(f.read_text(encoding="utf-8", errors="replace"))
        (out / f.name).write_text(fixed, encoding="utf-8")
        print(f"{f.name}: {len(fixed)} chars -> {out / f.name}")


if __name__ == "__main__":
    main()
