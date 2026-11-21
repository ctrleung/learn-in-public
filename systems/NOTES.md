# Notes

## Learner

- Working programmer, mainly frontend, some backend and API experience. Wants to keep hand-coding skills sharp.
- Knows the web basics and has covered request journey, DNS, HTTP and TLS basics in `../web/`.

## Preferences

- Short sessions; uneven weekly energy. About 10 minutes, on a weekend.
- Wants durable, referable notes that others can read too (repo is public). Keep personal details out of committed files, including interview dates and other personal timing.
- Security thread: ask "how does this get attacked, and how is it mitigated?"

## Working agreements

- Workspace is `systems/`. Session log lives in `../log/`; tag each line `[systems]`.
- This is the first thing to skip when I'm tired. Web and Japanese come first.
- Parked topics are in `PARKING-LOT.md`. Don't work on them unless I ask.
- Docker and Kubernetes docs are blocked until `docs.docker.com` and `kubernetes.io` are allowed in the network settings; don't plan a container lesson until they are.

## How to teach me

- Quiz before explaining: ask typed questions first, then teach. Not multiple choice.
- Don't hand me finished answers. Give a hint or a narrower question and let me try again; explain only after a real attempt.
- For design practice: I attempt the design first, in my own words, then give feedback on what's missing and what's strong. Don't hand me a finished design.
- Everything I miss goes in `gaps.md`. I write the fix in my own words; it becomes fixed only after I answer correctly from memory at two re-tests in a row, at increasing intervals.
- Read a source section before a lesson cites it; say plainly when I've only read headings.

## Mastery and spaced repetition

- Mastery first: I move on when I can answer the previous material from memory, not when it has been covered. New material waits until the previous batch has passed its first re-test.
- Reviews come before new material. Due items in `reviews.md` are tested first, oldest first. On a tired day, do the reviews only and skip the new lesson; never skip the reviews.
- `reviews.md` is the live queue: one row per item, with its stage, last result and next due date. The stages are 1, 3, 7, 14 and 30 days. A correct answer from memory moves the item up a stage. A miss sends it back to 1 day and adds it to `gaps.md`. An item is **mastered** after it passes the 14-day and 30-day tests; after that it only needs an occasional check.
- Test the same idea in a different form each time (explain it, apply it, compare it), so I'm not just recognizing the question.
- Block and topic reviews interleave: mix in items from earlier topics.
- A learning record's "Re-test" line is the first scheduled test; `reviews.md` is the source of truth for what's due.

## Session routine

- Warm-up before any new lesson: 1 or 2 typed questions from due items in `reviews.md` and open items in `gaps.md`, oldest first. Feedback right away: what was right and what was missing. The correct answer only after a real attempt.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>", the first scheduled test. The live queue is `reviews.md` (stages 1, 3, 7, 14 and 30 days).
- Wrap-up: update `reviews.md` and `gaps.md`, add one line to ../log/YYYY-MM.md tagged `[systems]`, commit to a branch, open the PR, and tell me in one line what to do next time.
