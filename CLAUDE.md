# Learning repo: how to start a session

I am often tired and will not remember instructions. When I open a session and say anything short ("go", "hi", "study", "/teach"), start a study session without asking me what to do.

This repo has one /teach workspace per subject:

- `web/`: active. Web fundamentals, 23 Nov 2026 to 14 Feb 2027, following `web/PLAN.md`. Sessions of 10 to 20 minutes.
- `japanese/`: active. Short sessions (about 10 minutes or less) that reinforce what I learn outside the repo (Anki for vocabulary, Renshuu for hiragana).
- `systems/`: active, one short session a week (about 10 minutes, on a weekend). Scaling and networking, then containers and Kubernetes, with system design practice, following `systems/PLAN.md`. The first thing to skip when I'm tired. Parked topics (AWS, Linux and so on) are in `systems/PARKING-LOT.md`; do not work on them unless I ask.

## Pick the workspace

1. If I name a workspace or a topic ("web", "japanese", "systems", "css", "docker"), use that one.
2. On a Saturday or Sunday, if the log has no `[systems]` line yet that week, a bare "go" starts `systems/`.
3. Otherwise, pick the workspace with the most overdue re-tests or open items in its `gaps.md`, and do not ask me. If nothing is due anywhere, use `web/`.
4. Work in that workspace's folder with Matt Pocock's /teach skill. If it isn't installed, fetch it from github.com/mattpocock/skills (skills/productivity/teach/SKILL.md).

## Run the session

1. Read that workspace's `NOTES.md` and follow it, including "How to teach me" and the Session routine. In `web/` and `systems/`, also read `PLAN.md`.
2. Read its `gaps.md` and learning records. Warm up first with 3 or 4 questions (2 or 3 in `japanese/`, 1 or 2 in `systems/`), taken from the records' "Re-test" dates that are due and open items in `gaps.md`, oldest first. I answer by typing. If nothing is due, go straight to the lesson.
3. Then teach the next topic: from `PLAN.md` in `web/` and `systems/`, adjusting to `gaps.md` and how I'm doing. Choose the topic yourself, and ask me only if there is a real choice. Quiz me first and do not hand me finished answers: use hints and narrower questions, and put everything I miss in `gaps.md`.
4. Keep it to the session length above unless I say otherwise.
5. When I say "done" or "wrap up", finish as that workspace's NOTES.md says: explain-back, learning record, `gaps.md`, log line (tagged with the workspace), branch, PR.

Never ask me which file to follow or what to warm up with.
