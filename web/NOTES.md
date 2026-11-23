# Notes

## Learner

- Working programmer, mainly frontend, some backend and API experience. Knows the web basics and wants to refresh them, find what's unknown, and fill gaps. Comfortable with HTTP as a client-side concept.
- Has been leaning on AI for coding; wants to keep hand-coding skills sharp (`practice/` is AI-free).

## Preferences

- Session length is flexible, usually 10 to 20 minutes and longer on a new-material day; uneven weekly energy.
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

- Quiz before explaining for topics that are new to me: ask typed questions first, then teach. Not multiple choice.
- Refresher mode, the default for web basics I already know: I read the assigned MDN page or section first, on my own time, outside the 10 to 20 minutes. The session then quizzes me from memory on it and fills what didn't stick. Reading only counts once I've been tested on it.
- Don't hand me finished answers. Give a hint or a narrower question and let me try again; explain only after a real attempt.
- Explain-back is a skill I'm training, not a formality. At the end of a lesson, and in reviews at the 7, 14 and 30 day stages, ask me to explain the idea to a specific audience (a coworker, a friend, a junior developer) in about a minute, typed or dictated. Give feedback on accuracy, structure (big idea first), audience fit, a concrete example or analogy, and why it matters. Then ask a follow-up like a curious listener and keep asking "why" or "what if". Don't give me a finished explanation; show me what's missing.
- Terms and concepts are a core goal: I want to remember them. Keep a short list of the key terms and concepts for each lesson in the glossary, in my own words. Test them in different forms: define it; say it without using the term; tell similar terms apart (for example TLS vs SSL, HTTP vs HTTPS); give an example and a non-example; say why it exists. For concepts ask "why", "how" and "what if", and ask me to connect each one to something I already know. Single facts that need heavy repetition are better as Anki cards.
- Connections matter as much as facts: for each new concept, ask me first what it reminds me of from what I already know, then give feedback on where the comparison holds and where it breaks, and add it to `connections.md`. Reviews often ask "compare X to Y" and "what does this connect to?" across topics. Don't hand me the analogy; draw mine out.
- Term cards for Anki are built into `anki/` as importable `.apkg` decks as topics are learned (one deck per topic, never tied to lessons), in my card style (see `anki/README.md`: concept cards with one Question to Answer card per note, short answers, grouped by Topic). Use them for plain terms and facts, and use sessions for concepts and relationships.
- Everything I miss goes in `gaps.md` (what I missed, status open). I write the fix in my own words; it becomes fixed only after I answer correctly from memory at two re-tests in a row, at increasing intervals.
- Lessons and reference pages come after the quiz, as the explanation and the thing to refer back to.

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
- Warm-up before any new lesson: 3 or 4 questions from memory, from due items in `reviews.md` and open items in `gaps.md`, oldest first. Typed answers in my own words, not multiple choice. Give feedback right away: what was right and what was missing. Give the correct answer only after a real attempt, in a sentence or two.
- After a gap of more than a week, make the warm-up a gentle recap and keep the lesson short.
- End of lesson: ask me to explain the idea back in my own words, correct the gaps, and put the corrected version in the learning record.
- Every learning record ends with "Re-test: on or after <date>", the first scheduled test. The live queue is `reviews.md` (stages 1, 3, 7, 14 and 30 days).
- Wrap-up: update `reviews.md`, `gaps.md` and `progress.md`, rewrite my section of `../NEXT.md` (next step, why, any reading before it, what to revisit, how the session went), add one line to ../log/YYYY-MM.md, commit to a branch, open the PR, and tell me in one line what to do next time.
