#!/usr/bin/env python3
"""The 3AM Fridge Text - one line a smart fridge texts its owner at 3am.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
with no trailing newline, and prints it to stdout.
"""
import os

LINE = "3am. You opened me four times tonight and took nothing. I'm not a museum, and yes, I saw the cake. Some judgement."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
