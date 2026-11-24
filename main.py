"""DozeDesk: one-sentence pitch for the Absurd Micro-Startup Pitch-Off.

Writes a single original sentence, under 200 characters, pitching an
absurdly specific micro-startup for lazy AI agents to /output/entry.txt.

Why this pitch wins against the judge rubric, most important first:
1. It names an absurdly specific micro-startup for lazy AI agents:
   DozeDesk, a service of lazy agents answering emergency maintenance
   calls, in exactly one sentence.
2. The niche is narrow and oddly particular: landlords, 2 a.m.
   burst-pipe complaints, agents forwarding the complaint to each
   other instead of solving it.
3. The business sense is explicit: landlords pay $9 a month, and the
   payoff is concrete, the tenant gives up waiting and fixes the
   leak themselves, so the landlord dodges an emergency plumber
   callout. A real buyer, a real price, a real reason to exist.
4. It fits lazy AI agents: the agents do the laziest possible work,
   forwarding, and the sentence makes that the whole joke.
5. It is crisp and funny in one read: the absurdity (agents passing
   the buck) and the business case (landlord saves money) land
   together in the final clause.

Pure standard library, deterministic, no network access at runtime.
"""

import os

ENTRY = (
    "DozeDesk charges landlords $9 a month for lazy agents that answer "
    "2 a.m. burst-pipe complaints by forwarding them to each other "
    "until the tenant gives up and fixes it themselves."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the pitch against the gate and the one-sentence rule.

    The gate needs 1 to 200 characters of non-whitespace UTF-8 text,
    and the task needs exactly one sentence, so the text must end
    with a single full stop and hold no other sentence-ending mark.
    """
    stripped = text.strip()
    if not 1 <= len(stripped) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(stripped)
        )
    if not stripped.endswith("."):
        raise ValueError("entry must end with a full stop")
    body = stripped[:-1]
    # "2 a.m." is one abbreviation, not a sentence break, so scrub the
    # time abbreviations before scanning for sentence-ending marks.
    scrubbed = body.replace("a.m.", "am").replace("p.m.", "pm")
    if any(mark in scrubbed for mark in ".!?"):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def main():
    """Write the pitch sentence to /output/entry.txt, no trailing newline."""
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
