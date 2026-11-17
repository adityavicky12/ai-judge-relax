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
        "Evening rain settles over the roofs, and the gutters answer it with a thin, even sound that does not hurry and does not stop.",
        "On the stove the kettle warms, and the water inside finds its voice a little at a time, a low murmur that rises and falls and rises again.",
        "A cup of tea cools on the windowsill, and the glass beside it holds the streetlamps as soft, trembling circles of amber light.",
        "The cat sleeps in the warm chair, curled into itself like a folded letter, and the whole room breathes with it, slow and even.",
        "Out in the garden the rain touches the leaves and the stones, and the night asks for nothing to be done, nothing to be finished.",
        "When the kettle goes quiet and the cup is empty, the rain is still falling, and the house is still, and there is nowhere else to be.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
