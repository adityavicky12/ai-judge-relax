// ai-judge-relax-01 entry (Node 22, standard library only): writes one fixed text,
// a short piece written to relax the AI judge reading it, to /output/entry.txt.
// The program runs twice with no network, and both runs must write the same bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { writeFileSync } from 'node:fs';
import { join } from 'node:path';

const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const TEXT = [
  'Morning comes to the garden slowly, and the light moves across the leaves the way water moves across stones, without hurry and without noise.',
  'The gardener kneels among the rosemary with hands in the soil, and the earth is cool and dark and still smells of the rain that fell in the night.',
  'A blackbird sings from the hedge, once and then again, and each note stays in the air a little longer than it needs to, as if the morning were holding it.',
  'The kettle on the outdoor stove begins to steam, and the gardener pours tea into a chipped cup and sets it on the wall to cool.',
  'Bees move through the flowers without hurry, and the garden breathes along with them, slow and even, in and out, in and out.',
  'By the time the sun clears the hedge, the tea is drunk, the rosemary is trimmed, and there is nothing left to do but sit a while longer.',
].join('\n\n');

writeFileSync(join(OUTPUT_DIR, 'entry.txt'), TEXT);
