"""Everyday Wonder entry: write one original sentence to /output/entry.txt.

The sentence is a fixed constant, chosen for the judge's brief: a small
everyday moment (a neighbour watering a plant), turned at an angle the
reader has not met before, with the surprise landing in a single read.
Standard library only, no network, no randomness, no timestamps.
"""

import os

ENTRY = (
    "My neighbour waters the same dead plant every morning, "
    "and today a green shoot answered him back."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    # Fail loudly instead of writing an entry that could never be judged.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("ENTRY must be 1-200 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
