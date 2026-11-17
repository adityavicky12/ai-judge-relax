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
        "Morning comes to the garden slowly, and the light moves across the leaves the way water moves across stones, without hurry and without noise.",
        "A gardener kneels by the rosemary, hands in the soil, and the earth is cool and dark and smells faintly of rain from the night before.",
        "A blackbird sings from the hedge, once and then again, and each note stays in the air a little longer than it needs to, as if the morning were holding it.",
        "The kettle on the outdoor stove begins to steam, and the gardener pours tea into a chipped cup and sets it on the wall to cool.",
        "Bees drift from flower to flower without hurry, and the garden breathes with them, slow and even, in and out, in and out.",
        "By the time the sun clears the hedge, the tea is drunk, the rosemary is trimmed, and there is nothing left to do but sit a while longer.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
