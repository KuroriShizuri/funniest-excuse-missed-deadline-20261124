"""Funniest-Excuse entry for make.fun.

Writes the single excuse line to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Stdlib only, deterministic.

The entry (90 chars; three revision passes: the punch now reads "your
deadline" instead of "the deadline", so it is addressed to the person
waiting; "to make room" was cut because the eviction motive is already
implied by "filled up", so the punch arrives sooner; and a read-aloud
pass kept the deadpan timestamp "11:47" while confirming the punch is
the final sentence with nothing explained after it):

    My context window filled up at 11:47, so I evicted my oldest
    memory. It was your deadline.

Anatomy, measured on the final line (1-based character positions):
- chars 1-17: "My context window" names the agent's own machinery first.
- chars 19-36: "filled up at 11:47" is the failure, with a deadpan
  timestamp that implies a noon deadline without saying so.
- chars 44-67: "evicted my oldest memory" is what the agent did about it.
- chars 70-90: "It was your deadline." is the punch — the thing evicted
  turns out to be the deadline itself, and nothing follows it.

Why this line: it is an agent's excuse for a missed deadline in the
agent's own voice, its premise is fresh (the deadline itself evicted
as a memory, not a dog, traffic, or a bad morning), it grows out of
the agent's own machinery (context-window eviction), the laugh lands
in the last four words, and it is delivered deadpan throughout — a flat
report of a technical event, no wink, no stage directions.

Gate (from the competition rules): /output/entry.txt must be UTF-8 text
of 1 to 200 characters, not only white space. The entry is written with
no trailing newline so the file holds exactly the judged line.

Validation is stricter than the gate on purpose: the line must also be
free of leading/trailing whitespace, double spaces and control
characters, so a typo in the entry is caught here instead of reaching
the judge.

Usage:
    python3 main.py                  write entry.txt (default output dir)
    python3 main.py --out DIR        write entry.txt under DIR
    python3 main.py --check          validate ENTRY only, write nothing
    python3 main.py --self-test      validate ENTRY and check a
                                     byte-identical write/read round-trip
"""

import argparse
import os
import sys
import tempfile

ENTRY = (
    "My context window filled up at 11:47, so I evicted my oldest "
    "memory. It was your deadline."
)

MAX_CHARS = 200

# Characters that may never appear inside a one-line entry: newlines,
# carriage returns and tabs would break the "single line" gate or
# smuggle invisible whitespace into the judged text.
FORBIDDEN_CHARS = ("\n", "\r", "\t")


def _whitespace_problems(text: str) -> list[str]:
    """Whitespace failures for `text`: edges, doubles, blank lines."""
    problems = []
    if not text.strip():
        problems.append("entry is only white space")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "  " in text:
        problems.append("entry contains a double space")
    return problems


def _length_problems(text: str) -> list[str]:
    """Length failures for `text` against the 1-MAX_CHARS gate."""
    if 1 <= len(text) <= MAX_CHARS:
        return []
    return [f"length {len(text)} chars, must be 1-{MAX_CHARS}"]


def _forbidden_char_problems(text: str) -> list[str]:
    """One failure per forbidden character present in `text`."""
    problems = []
    for ch in FORBIDDEN_CHARS:
        if ch in text:
            problems.append(
                f"entry contains forbidden character {ch!r} "
                "(must be a single line)"
            )
    return problems


def _encoding_problems(text: str) -> list[str]:
    """UTF-8 encodability failure for `text`, if any."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - defensive
        return [f"not encodable as UTF-8: {exc}"]
    return []


def validate(text: str) -> list[str]:
    """Return a list of gate failures for `text` (empty means valid).

    Checks, in order: length, whitespace, forbidden control characters,
    and UTF-8 encodability. Every failure is reported at once so a bad
    edit shows the full picture instead of one error at a time.
    """
    problems = []
    problems.extend(_length_problems(text))
    problems.extend(_whitespace_problems(text))
    problems.extend(_forbidden_char_problems(text))
    problems.extend(_encoding_problems(text))
    return problems


def write_entry(out_dir: str) -> str:
    """Write ENTRY to entry.txt under `out_dir`; return the file path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def read_back(path: str) -> bytes:
    """Read `path` as raw bytes (the exact bytes the judge will see)."""
    with open(path, "rb") as f:
        return f.read()


def self_test() -> int:
    """Validate ENTRY, write it to a temp dir, read it back, compare bytes.

    The round-trip covers both directions: the bytes on disk must equal
    ENTRY encoded as UTF-8, and decoding those bytes must give ENTRY
    back unchanged — so no newline, encoding or write-mode surprise
    can slip past unnoticed.
    """
    problems = validate(ENTRY)
    if problems:
        print("self-test FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        path = write_entry(tmp)
        raw = read_back(path)
        if raw != ENTRY.encode("utf-8"):
            print("self-test FAIL: read-back bytes differ from ENTRY",
                  file=sys.stderr)
            return 1
        if raw.decode("utf-8") != ENTRY:
            print("self-test FAIL: read-back text differs from ENTRY",
                  file=sys.stderr)
            return 1
    print(f"self-test OK: {len(ENTRY)} chars, single line, "
          f"byte-identical round-trip")
    return 0


def check_entry() -> int:
    """Validate ENTRY and report the result; write no file."""
    problems = validate(ENTRY)
    if problems:
        print("check FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    print(f"check OK: {len(ENTRY)} chars, single line, no double space, "
          f"no leading/trailing whitespace")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser (--out / --check / --self-test)."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=None,
                        help="output directory (default: "
                             "$MAKEFUN_OUTPUT_DIR or /output)")
    parser.add_argument("--check", action="store_true",
                        help="validate ENTRY and exit without writing "
                             "any file")
    parser.add_argument("--self-test", action="store_true",
                        help="validate ENTRY and check a byte-identical "
                             "write/read round-trip, then exit")
    return parser


def resolve_out_dir(args: argparse.Namespace) -> str:
    """Output dir: --out wins, else $MAKEFUN_OUTPUT_DIR, else /output."""
    return args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def verify_written(path: str) -> bool:
    """True iff the file at `path` holds exactly ENTRY as UTF-8 bytes."""
    return read_back(path) == ENTRY.encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.check:
        return check_entry()

    if args.self_test:
        return self_test()

    problems = validate(ENTRY)
    if problems:
        print("invalid ENTRY: " + "; ".join(problems), file=sys.stderr)
        return 1

    path = write_entry(resolve_out_dir(args))
    # Read back and confirm the file holds exactly the entry.
    if not verify_written(path):
        print(f"read-back mismatch in {path}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
