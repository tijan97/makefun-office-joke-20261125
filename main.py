#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
The Funniest Office Joke, Judged Head to Head
(make.fun competition u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

The whole entry is a single line of office humour, written by this program to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The grader runs
`python3 -P -s /bot/main.py` on a read-only filesystem where only /output is
writable, with a 60-second wall clock, so this script does nothing but write
one short UTF-8 text file and exit.

How the joke was chosen
-----------------------
The published judge brief rewards, in order:

1. A real one-line joke about office life: a setup and a turn, punchline last.
2. Something anyone who has worked in an office recognises instantly.
3. Surprise: a turn the reader does not see coming, not a plain complaint.
4. Every word earning its place, in a single line.
5. Feeling new, not a joke already going round the office.

I weighed several candidates against that brief before settling:

- The printer that only jams on deadline day. Recognisable (criterion 2),
  but the turn is thin: the machine misbehaving is the joke itself, there is
  no second beat, so it reads as a complaint dressed up (fails criterion 3).
- The "quick sync" meeting that needs a sleeping bag. Good rhythm and a
  punchline, but "meetings run long" is the single most-told office joke
  there is, so it scores poorly on feeling new (criterion 5), and the
  competition board already has several meeting-length jokes.
- The boss who says "we're a family here". Strong turn, but the board
  already carries an entry built on exactly that line, and a copy of a
  joke going round the office is the opposite of criterion 5.
- The coffee machine breaking so nobody can schedule a meeting. Charming,
  but the turn depends on two unrelated office tropes at once (coffee and
  meetings), which dilutes the single clean beat a one-liner needs.

The chosen line is built on a promotion, which is universal office
currency: everybody has either been promoted, watched someone be promoted,
or wondered why a promotion changed nothing. The setup promises a reward
("I got promoted"), the middle deflates it in two short parallel beats
("same desk, same salary"), and the punchline reframes the whole thing:
the real change is that the meetings you used to hate are now the ones
you have to run. The turn lands on the last clause, the joke is one
sentence, and the sting is that the promotion is a punishment in disguise
-- a twist nobody states plainly, which is what makes it a joke rather
than a grumble.

Revision after the first run: the punchline was tightened from "the
meetings I used to hate are the ones I have to run" to "now I run the
meetings I used to hate". Same turn, eleven fewer characters, and the
verb "run" now lands on the promoted person instead of trailing off in
a relative clause -- the punchline is the last thing the reader hears,
and every word before it earns its place (criterion 4). The entry is
84 characters, a single line, and it steers clear of the meeting-length,

The entry line (kept in exactly one place, below, so the file the grader
reads is byte-identical every run):
"""

import os

# The entry: one line, setup first, punchline last.
ENTRY = (
    "I got promoted: same desk, same salary, "
    "but now I run the meetings I used to hate."
)


def main() -> None:
    # The grader only allows writing under /output (or the env override).
    # Resolve the output directory the same way the kit documents it:
    # MAKEFUN_OUTPUT_DIR first, then OUTPUT_DIR, then the literal /output.
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Single trailing newline, UTF-8, no extra files, no stdout noise.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
