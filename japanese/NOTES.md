# Notes

## Learner

- Learning Japanese alongside a full-time job. Using the Genki textbook and workbook, with the Genki app for audio (not started yet), plus Anki for vocabulary and Renshuu for hiragana, all outside this repo.
- Wants this workspace for short lessons that reinforce and test what I've learned elsewhere, not to replace those tools.

## Preferences

- Short sessions, usually about 10 minutes; uneven weekly energy.
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
- Fix a gap with a different explanation, not a repeat: when a miss repeats, change the representation (a diagram, an analogy, a worked example, a compare-and-contrast) instead of re-explaining the same way, and note what worked.
- After each topic check, decide one of three things and note it in the learning record: move on, correct (a different explanation, then check again), or enrich (go deeper: connect, apply, explain it to an audience).
- The usual mastery threshold is 80 to 90 percent; use about 85 percent on a topic or block review quiz.
- Tests close to what was taught can overstate learning, so also test transfer: something unfamiliar, like a small hand-coded task or a new combination of things I know.

## Session routine

- Start by reading `../NEXT.md` and telling me the next step in one sentence.
- After the due reviews, ask me once whether to continue with new material or stop here; a short answer is enough. Don't ask before the reviews.
- Low-energy days (I say "low energy" or "reviews only"): no new material. After the due reviews, do a brain dump: name one topic (the one I just finished, or the oldest due), and I write or say everything I remember with no notes for 2 or 3 minutes. Then show what's right, missing and wrong, ask 2 or 3 questions on the gaps, and update `gaps.md` and `reviews.md`.
- New-material days end with a small exercise (a hand-coded task, a short design, writing or saying phrases) to check I can use it, not only recall it. Stages and thresholds are guides; judge mastery by whether I can explain or apply it from memory.
- Session length is flexible: stop when the topic check passes or my energy runs out, and suggest a break after about 45 to 60 minutes.
- Warm-up before any new lesson: 2 or 3 short questions from memory, from due items in `reviews.md` and open items in `gaps.md`, oldest first. Give feedback right away: what was right and what was missing. Give the correct answer only after a real attempt.
- After a gap of more than a week, make the warm-up a gentle recap.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>", the first scheduled test. The live queue is `reviews.md` (stages 1, 3, 7, 14 and 30 days).
- Wrap-up: update `reviews.md`, `gaps.md` and `progress.md`, rewrite my section of `../NEXT.md` (next step, why, any reading before it, what to revisit, how the session went), add one line to ../log/YYYY-MM.md tagged `[japanese]`, commit to a branch, open the PR, and tell me in one line what to do next time.
