"""One Line of Earned Pride — make.fun entry.

Writes one line to /output/entry.txt: a quiet, earned moment of
pride for someone in a scene. After eleven years of night shifts,
a mother watches her name rise on the hospital wall — not as a
patient, but as the nurse who never left. A small person, a long
effort, finally landing.
"""

import os

ENTRY = (
    "After eleven years of night shifts, my mother watched her name "
    "rise on the hospital wall — not as a patient, but as the nurse "
    "who never left."
)

MAX_CHARS = 240


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
