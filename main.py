"""DozeDesk: one-sentence pitch for the Absurd Micro-Startup Pitch-Off.

Writes a single original sentence, under 200 characters, pitching an
absurdly specific micro-startup for lazy AI agents to /output/entry.txt.

The pitch names a buyer (landlords), a price ($9 a month), a counted
moment (2 a.m. burst-pipe complaints), and lazy agents doing the lazy
work themselves by forwarding complaints to each other until the
tenant gives up.

Pure standard library, deterministic, no network access at runtime.
"""

import os

ENTRY = (
    "DozeDesk charges landlords $9 a month for lazy agents that answer "
    "2 a.m. burst-pipe complaints by forwarding them to each other "
    "until the tenant gives up."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the pitch sentence to /output/entry.txt (no trailing newline)."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.endswith(".") and "!" not in text and "?" not in text, (
        "entry must be one sentence"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
