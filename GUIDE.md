# Guide: how the repo works and what each file is for

## The workflow

A study session is started by saying "go" (or naming a workspace) in a Claude Code session. `CLAUDE.md` tells Claude what to do, so there is nothing to remember.

1. **Pick the workspace.** A named one wins. At the weekend, `systems/` comes first if it hasn't had a session that week. Otherwise the workspace with the most overdue items.
2. **Read `NEXT.md`.** It gives the next step in one sentence, and says what to read or do beforehand.
3. **Reviews first.** Due items from `reviews.md` and open items from `gaps.md` are quizzed from memory, typed. A correct answer moves an item up (1, 3, 7, 14, 30 days); a miss sends it back to 1 day and into `gaps.md`.
4. **New material, if there's energy.** Quiz first, then explain, then explain it back in my own words, then a small exercise. On a tired day: reviews only, then a brain dump.
5. **Wrap up ("done").** Learning record, `reviews.md`, `gaps.md`, `progress.md`, `NEXT.md`, a log line, then a branch and a pull request.
6. **Merge the PR.** The next session only sees what is on `main`.

Anki runs on its own schedule outside the repo.

## The root

| File or folder | What it's for |
|---|---|
| `CLAUDE.md` | The rules Claude follows to run a session, and the privacy rule below |
| `README.md` | The public overview: workspaces, the short workflow, the 12-week web plan |
| `GUIDE.md` | This file |
| `NEXT.md` | The next step in each workspace, what to read or do before it, and what to revisit. Updated at every wrap-up |
| `log/` | One line per session, tagged by workspace. Showing up counts, even on tired weeks |

## Inside a workspace (`web/`, `japanese/`, `systems/`)

| File or folder | What it's for |
|---|---|
| `README.md` | What the workspace is, in a few lines |
| `MISSION.md` | The goal and what "done" looks like |
| `PLAN.md` | The order of topics and the dates (`web/`, `systems/`; `japanese/` has a phased plan) |
| `NOTES.md` | How Claude should teach in this workspace, and its end-of-session routine |
| `RESOURCES.md` | The sources used (MDN, books, apps) |
| `reviews.md` | The live review queue: item, stage, last result, due date |
| `gaps.md` | What I missed, until I get it right at two re-tests in a row |
| `progress.md` | A checklist of skills in order; ticked only when mastered |
| `connections.md` | Where new ideas link to things I already know, and where the comparison breaks |
| `exercises.md` | Hands-on things to try later |
| `learning-records/` | A short numbered record of each session: what was covered and how it went |
| `lessons/` | Lesson pages written for me to read |
| `reference/` | Notes and glossaries to look things up in |
| `assets/` | Styles and scripts the lesson pages use |
| `anki/` | Anki card files (`web/` only): the note type, the card data, a build script, exported decks |
| `practice/` | Code I write by hand, no AI (`web/` only) |
| `genki.md` | The Genki I map: textbook and workbook pages per lesson (`japanese/` only) |
| `PARKING-LOT.md` | Topics parked on purpose, not worked on unless I ask (`systems/` only) |

## Notebooks (no lessons)

| File or folder | What it's for |
|---|---|
| `korean/words.md` | Korean words I asked about, with how they sound in other languages as memory aids. Anki does the scheduling |
| `how-to-learn/` | Notes on learning better: `reading.md` (what I read), `reviews.md` and `gaps.md` (the same queue as elsewhere) |

## Keep the repo clean

This repo is public. Don't put anything personal in it: no real names, contact details, dates or places that identify me or my plans, and no private messages or account details. Don't commit secrets either (keys, tokens, passwords, `.env` files), or anything else that doesn't belong in a public learning log, like private documents, copyrighted books or pirated material. If something like that is shared in a session, Claude should leave it out and say so. If something slips in, tell Claude so it can be removed. Note that deleting a file doesn't remove it from git history, so anything sensitive needs more than a delete.
