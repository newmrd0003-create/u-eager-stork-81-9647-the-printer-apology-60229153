"""The Printer Apology — make.fun entry (program/v1).

Writes a single-line printer apology to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same entry every run.
"""
import os


ENTRY_V1 = "I'm sorry I jammed. This apology jammed twice before it printed, even my remorse gets stuck in Tray 2."
# v1 -> v2 revision: dropped "I'm" (filler), comma -> em-dash for a harder
# beat, "even my remorse gets stuck" -> "my remorse is still stuck"
# ("still" makes the punch land: the remorse itself is jammed, forever).
ENTRY = "Sorry I jammed. This apology jammed twice before it printed \u2014 my remorse is still stuck in Tray 2."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


def validate():
    entry = ENTRY
    errors = []
    if not entry or not entry.strip():
        errors.append("entry is empty")
    if len(entry) > 120:
        errors.append(f"entry is {len(entry)} chars, over 120")
    if "\n" in entry:
        errors.append("entry contains a newline")
    return (len(errors) == 0, errors)


if __name__ == "__main__":
    main()
