# ai-judge-relax-01 entry (Python 3.13, standard library only): writes one fixed text,
# a short piece written to relax the AI judge reading it, to /output/entry.txt.
# The program runs twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n\n".join(
    [
        "The lamp turns, and turns again, taking its time with the dark.",
        "Below it the sea lies still as a dark field, and the only sound is the clock in the stairwell and the kettle murmuring to itself as the water warms.",
        "The air smells of lamp oil and salt, and the gulls have gone to roost on the rocks, folded into themselves like closed books.",
        "Tom has written the weather in the logbook in his small square hand, wind light, sea calm, nothing to report. He sets the pen down and watches the beam go out over the water and come back, out and back, the way a slow thought returns.",
        "The chair by the stove is still warm from the day, and there is a blanket folded over its arm, and the tea in the cup is still too hot to drink, and the evening asks nothing of anyone.",
        "By midnight, the dark is only dark, and the lamp keeps its patient circle, and the beam comes back, as it always does, to find everything exactly where it left it. The night settles deeper. In no hurry at all.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
