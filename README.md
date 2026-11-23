# learn-in-public

🍎 my public learning log

New here? [`GUIDE.md`](GUIDE.md) explains how the workflow runs and what each file is for.

I use this repo to learn in public, one workspace per subject, each run with the `/teach` skill. I already know the basics of the web, so the aim there is to refresh, find what I don't know yet, and fill gaps. I'm also keeping my hand-coding skills sharp.

## Workspaces

| Folder | Status | What |
|---|---|---|
| [`web/`](web/) | Active, 23 Nov 2026 to 14 Feb 2027 | Web fundamentals: HTML and accessibility, CSS, browser, HTTP and JavaScript gaps, then React. MDN is the main resource. [Plan](web/PLAN.md), [gaps](web/gaps.md) |
| [`japanese/`](japanese/) | Active, short sessions | Survival Japanese for travel, reinforcing what I learn in Genki, Anki and Renshuu. [Mission](japanese/MISSION.md), [plan](japanese/PLAN.md) |
| [`systems/`](systems/) | Active, one short weekend session a week | How web systems scale and connect: networking, scaling, then containers and Kubernetes, plus system design practice. AWS, Linux and other topics stay parked in [`systems/PARKING-LOT.md`](systems/PARKING-LOT.md). [Mission](systems/MISSION.md), [plan](systems/PLAN.md) |
| [`korean/`](korean/) | Notebook, no lessons | How Korean words sound in other languages, as memory aids for the Korean cards I review in Anki. [Words](korean/words.md) |

Each workspace has its own mission, notes, `gaps.md`, learning records, lessons and reference pages.

## How a study session works

1. **Reviews first.** Items due in the workspace's `reviews.md` are tested from memory, typed, oldest first. The stages are 1, 3, 7, 14 and 30 days: a correct answer moves an item up, a miss sends it back to 1 day.
2. **Then new material, if there's energy.** Quiz first, then explain after a real attempt, then explain it back in my own words. On a tired day, reviews only, unless everything is clear, when one small piece may be offered.
3. **Misses go in `gaps.md`** until I answer them correctly at two re-tests in a row.
4. **Mastery gates the plan.** I move on when the key items are at the 7-day stage or higher with no open gaps; otherwise the block extends. If time runs short, the extras shrink first, then the last block's breadth, and the plan is reviewed against `gaps.md` at the end of each block (depth over coverage).
5. **Wrap-up:** a learning record, the review queue, `gaps.md`, the next-step page (`NEXT.md`), a log line and a PR. The progress checklist, connections and exercises change only when something did.

![How a study session runs](docs/workflow-session.svg)

## Elsewhere

- [`log/`](log/): one line per study session, tagged by workspace, so showing up counts even on tired weeks
- [`web/practice/`](web/practice/): code written by hand, no AI
- [`how-to-learn/`](how-to-learn/): notes on how to learn better, and how I apply them here
- [`GUIDE.md`](GUIDE.md): how the workflow runs and what each file is for
- [`NEXT.md`](NEXT.md): what to do next in each workspace, updated after every session

## The web plan, 12 weeks

The dates are targets, not deadlines: a block ends when it's mastered, and the pace adjusts.

| Target dates | Block |
|---|---|
| 23 Nov to 13 Dec | HTML and accessibility |
| 14 Dec to 3 Jan | CSS |
| 4 Jan to 24 Jan | Browser, HTTP and JavaScript gaps |
| 25 Jan to 14 Feb | React |

Networking (DNS, HTTP, TLS basics, how a page loads) stays in `web/` only as it supports the browser and HTTP block. The schedule adjusts to how I'm doing.

## Current focus

Web: HTML and accessibility, starting 23 Nov. Japanese: rebuilding hiragana, then katakana and survival phrases. Systems: one short weekend session a week, starting with networking and scaling.
