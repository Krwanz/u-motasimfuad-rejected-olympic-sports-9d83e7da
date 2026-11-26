"""Rejected Olympic Sports — make.fun bounty entry.

Writes one funny single-line sport the Olympics turned down to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The joke plays on a universal truth: everyone hates queuing, so a sport
built entirely out of standing in line is absurd yet instantly
recognisable as a broadcast event — heats, a six-hour final, judges,
and a gold medal decided not by speed or strength but by who complains
the least. The twist lands in the last clause.

Revision: the first draft said "wait in line for six hours without
moving, and the gold medal goes to whoever complains the least".
"Stand" replaces "wait" (the sport is standing, not waiting), "gold"
replaces "the gold medal" and "complains least" drops "the", so the
same joke lands in fewer words and the sting hits sooner.
"""

import os
import sys

LINE = (
    "Competitive queue-standing: athletes stand in line for six hours "
    "without moving, and gold goes to whoever complains least."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
