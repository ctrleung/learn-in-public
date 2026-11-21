# Notes

## Learner

- Learning Japanese alongside a full-time job. Using the Genki textbook and workbook, with the Genki app for audio (not started yet), plus Anki for vocabulary and Renshuu for hiragana, all outside this repo.
- Wants this workspace for short lessons that reinforce and test what I've learned elsewhere, not to replace those tools.

## Preferences

- Short sessions; uneven weekly energy.
- Wants durable, referable notes that others can read too (repo is public). Keep personal details out of committed files, including the trip date and any other travel timing.

## Working agreements

- Workspace is `japanese/`. Session log lives in `../log/`; tag each line `[japanese]`.
- The first session, when `MISSION.md` doesn't exist yet, is the mission interview. Keep it short and conversational, one or two questions at a time.
- Typed answers: Japanese text and romaji both fine; ask which I want to practice when it matters.

## How to teach me

- Quiz before explaining: ask typed questions first, then teach. Not multiple choice.
- Don't hand me finished answers. Give a hint or a narrower question and let me try again; explain only after a real attempt.
- Everything I miss goes in `gaps.md`. I write the fix in my own words; it becomes fixed only after I answer correctly from memory at two re-tests in a row, at increasing intervals.
- Test me on what I've covered in Genki (textbook and workbook), Renshuu and Anki, not only what's new here.

## Mastery and spaced repetition

- Mastery first: I move on when I can answer the previous material from memory, not when it has been covered. New material waits until the previous batch has passed its first re-test.
- Reviews come before new material. Due items in `reviews.md` are tested first, oldest first. On a tired day, do the reviews only and skip the new lesson; never skip the reviews.
- `reviews.md` is the live queue: one row per item, with its stage, last result and next due date. The stages are 1, 3, 7, 14 and 30 days. A correct answer from memory moves the item up a stage. A miss sends it back to 1 day and adds it to `gaps.md`. An item is **mastered** after it passes the 14-day and 30-day tests; after that it only needs an occasional check.
- Test the same idea in a different form each time (explain it, apply it, compare it), so I'm not just recognizing the question.
- Block and topic reviews interleave: mix in items from earlier topics.
- A learning record's "Re-test" line is the first scheduled test; `reviews.md` is the source of truth for what's due.

## Session routine

- Warm-up before any new lesson: 2 or 3 short questions from memory, from due items in `reviews.md` and open items in `gaps.md`, oldest first. Give feedback right away: what was right and what was missing. Give the correct answer only after a real attempt.
- After a gap of more than a week, make the warm-up a gentle recap.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>", the first scheduled test. The live queue is `reviews.md` (stages 1, 3, 7, 14 and 30 days).
- Wrap-up: update `reviews.md` and `gaps.md`, add one line to ../log/YYYY-MM.md tagged `[japanese]`, commit to a branch, open the PR, and tell me in one line what to do next time.
