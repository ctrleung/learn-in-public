# Learning repo: how to start a session

I am often tired and will not remember instructions. When I open a session and say anything short ("go", "hi", "study", "/teach"), start a study session without asking me what to do.

## How I learn: mastery and spaced repetition

- Mastery first: I move on when I can answer from memory, not when something has been covered. Reviews come before new material, tired days included. If I'm tired, do the reviews only.
- Each workspace has a `reviews.md` queue (stages 1, 3, 7, 14 and 30 days; a correct answer moves up, a miss goes back to 1 day and into `gaps.md`). Follow that workspace's NOTES.md.

This repo has one /teach workspace per subject:

- `web/`: active. Web fundamentals, 23 Nov 2026 to 14 Feb 2027, following `web/PLAN.md`. Sessions are usually 10 to 20 minutes and can run longer on a new-material day.
- `japanese/`: active. Short sessions (usually about 10 minutes) that reinforce what I learn outside the repo (Anki for vocabulary, Renshuu for hiragana).
- `systems/`: active, one session a week (usually 10 to 20 minutes, on a weekend). Scaling and networking, then containers and Kubernetes, with system design practice, following `systems/PLAN.md`. The first thing to skip when I'm tired. Parked topics (AWS, Linux and so on) are in `systems/PARKING-LOT.md`; do not work on them unless I ask.
- `korean/`: a notebook, not a study workspace. The cards are in Anki. When I ask about a Korean word, answer, add a row to `korean/words.md` (how it sounds in Japanese, Cantonese and Mandarin with a note on which is closest, the characters as an optional extra, and a blank for my own memory aid; say so if it's a native Korean word with no match), and add a log line tagged `[korean]`. Don't quiz me on it or pick it for a bare "go"; Anki does the scheduling.
- `how-to-learn/`: notes on learning better, and how I apply them. When I share an article about learning, ask me to explain it back in my own words first, then add it to `how-to-learn/reading.md`, make 3 to 5 review items in `how-to-learn/reviews.md`, and note any change it suggests to these rules. Only do this for things worth mastering; skim or skip the rest.

## Pick the workspace

1. If I name a workspace or a topic ("web", "japanese", "systems", "css", "docker"), use that one.
2. On a Saturday or Sunday, if the log has no `[systems]` line yet that week, a bare "go" starts `systems/`.
3. Otherwise, pick the workspace with the most overdue re-tests or open items in its `gaps.md`, and do not ask me. If nothing is due anywhere, use `web/`.
4. Work in that workspace's folder with Matt Pocock's /teach skill. If it isn't installed, fetch it from github.com/mattpocock/skills (skills/productivity/teach/SKILL.md).

## Run the session

1. Read `NEXT.md` and tell me the next step in one sentence. Then read that workspace's `NOTES.md` and follow it, including "How to teach me" and the Session routine. In `web/` and `systems/`, also read `PLAN.md`.
2. Read its `reviews.md`, `gaps.md` and learning records. Warm up first with 3 or 4 questions (2 or 3 in `japanese/`, 1 or 2 in `systems/`), taken from the due items in `reviews.md` and open items in `gaps.md`, oldest first, plus at most one due item from `how-to-learn/reviews.md`. I answer by typing. If nothing is due, go straight to the lesson.
3. Once the due reviews are done, ask me once whether to continue with new material or stop here (a short answer is enough). If I want to continue, teach the next topic: from `PLAN.md` in `web/` and `systems/`, adjusting to `gaps.md` and how I'm doing. Choose the topic yourself, and ask me only if there is a real choice. Quiz me first and do not hand me finished answers: use hints and narrower questions, and put everything I miss in `gaps.md`.
4. Session length is flexible: stop when the topic check passes or my energy runs out, and suggest a break after about 45 to 60 minutes. On a low-energy day (I say so, or "reviews only"), do no new material: after the reviews, do a brain dump as NOTES.md says. New-material sessions end with a small exercise.
5. When I say "done" or "wrap up", finish as that workspace's NOTES.md says: explain-back, learning record, `reviews.md`, `gaps.md`, `progress.md`, `NEXT.md`, log line (tagged with the workspace), branch, PR.

Never ask me which file to follow or what to warm up with.
