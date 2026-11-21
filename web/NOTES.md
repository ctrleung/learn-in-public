# Notes

## Learner

- Working programmer, mainly frontend, some backend and API experience. Knows the web basics and wants to refresh them, find what's unknown, and fill gaps. Comfortable with HTTP as a client-side concept.
- Has been leaning on AI for coding; wants to keep hand-coding skills sharp (`practice/` is AI-free).

## Preferences

- Sessions of 10 to 20 minutes; uneven weekly energy. A lesson should be doable in a sitting.
- Depth over coverage: fewer topics, understood well, beats skimming many.
- Wants durable, referable notes that others can read too (repo is public). Keep personal details out of committed files.
- Keep a light security thread, browser-side (XSS, CORS, CSP, cookies, HSTS): when a topic raises "how is this attacked, and how is it mitigated?", ask it once.
- Hands-on practice welcome: local machine; hand-coded work goes in `practice/` (no AI).
- Keep a light "what changes at scale?" thread where a web topic overlaps with systems (caching, DNS, cookies and sessions, how a page loads): ask the question once, note it, and leave the depth for the weekend systems session.

## Working agreements

- Workspace is `web/`. Session log lives in `../log/`; tag each line `[web]`. Commit as the user (repo git config), push to a branch, merge via PR.
- Current focus (23 Nov 2026 to 14 Feb 2027): web fundamentals only, following `PLAN.md`. MDN is the main resource.
- Systems topics (scaling, networking, containers, system design) have their own short weekend sessions in `../systems/`. Other parked topics (AWS, Linux and so on) are in `../systems/PARKING-LOT.md`; don't work on those unless I ask.
- The schedule adjusts to how I'm doing: when `gaps.md` shows a topic needs more time, change `PLAN.md` and record it under "Schedule changes".

## How to teach me

- Quiz before explaining: ask typed questions on the new topic first, then teach. Not multiple choice.
- Don't hand me finished answers. Give a hint or a narrower question and let me try again; explain only after a real attempt.
- Everything I miss goes in `gaps.md` (what I missed, status open). I write the fix in my own words; it becomes fixed only after I answer correctly from memory at two re-tests in a row, at increasing intervals.
- Lessons and reference pages come after the quiz, as the explanation and the thing to refer back to.

## Mastery and spaced repetition

- Mastery first: I move on when I can answer the previous material from memory, not when it has been covered. New material waits until the previous batch has passed its first re-test.
- Reviews come before new material. Due items in `reviews.md` are tested first, oldest first. On a tired day, do the reviews only and skip the new lesson; never skip the reviews.
- `reviews.md` is the live queue: one row per item, with its stage, last result and next due date. The stages are 1, 3, 7, 14 and 30 days. A correct answer from memory moves the item up a stage. A miss sends it back to 1 day and adds it to `gaps.md`. An item is **mastered** after it passes the 14-day and 30-day tests; after that it only needs an occasional check.
- Test the same idea in a different form each time (explain it, apply it, compare it), so I'm not just recognizing the question.
- Block and topic reviews interleave: mix in items from earlier topics.
- A learning record's "Re-test" line is the first scheduled test; `reviews.md` is the source of truth for what's due.

## Session routine

- Warm-up before any new lesson: 3 or 4 questions from memory, from due items in `reviews.md` and open items in `gaps.md`, oldest first. Typed answers in my own words, not multiple choice. Give feedback right away: what was right and what was missing. Give the correct answer only after a real attempt, in a sentence or two.
- After a gap of more than a week, make the warm-up a gentle recap and keep the lesson short.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>", the first scheduled test. The live queue is `reviews.md` (stages 1, 3, 7, 14 and 30 days).
- Wrap-up: update `reviews.md` and `gaps.md`, add one line to ../log/YYYY-MM.md, commit to a branch, open the PR, and tell me in one line what to do next time.
