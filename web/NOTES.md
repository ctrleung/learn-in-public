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

## Working agreements

- Workspace is `web/`. Session log lives in `../log/`; tag each line `[web]`. Commit as the user (repo git config), push to a branch, merge via PR.
- Current focus (23 Nov 2026 to 14 Feb 2027): web fundamentals only, following `PLAN.md`. MDN is the main resource.
- Parked topics live in `../systems/` (a dormant workspace), kept, not dropped. Don't work on them unless I ask. When I do ask, run a normal lesson there and note whether it moves the web schedule.
- The schedule adjusts to how I'm doing: when `gaps.md` shows a topic needs more time, change `PLAN.md` and record it under "Schedule changes".

## How to teach me

- Quiz before explaining: ask typed questions on the new topic first, then teach. Not multiple choice.
- Don't hand me finished answers. Give a hint or a narrower question and let me try again; explain only after a real attempt.
- Everything I miss goes in `gaps.md` (what I missed, status open). I write the fix in my own words; it becomes fixed only after I answer correctly from memory on a re-test.
- Lessons and reference pages come after the quiz, as the explanation and the thing to refer back to.

## Session routine

- Warm-up before any new lesson: 3 or 4 questions from memory, from records whose re-test is due and open items in `gaps.md`, oldest first. Typed answers in my own words, not multiple choice. Give feedback right away: what was right and what was missing. Give the correct answer only after a real attempt, in a sentence or two.
- After a gap of more than a week, make the warm-up a gentle recap and keep the lesson short.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>" (1 day, then 3, 7, 14; up when I get it right, back when I don't).
- Wrap-up: update `gaps.md`, add one line to ../log/YYYY-MM.md, commit to a branch, open the PR, and tell me in one line what to do next time.
