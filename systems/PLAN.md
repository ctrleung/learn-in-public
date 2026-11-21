# Plan: systems thread (draft)

One short weekend session a week, starting after web week 1 (weekend of 28 to 29 Nov). Sessions are numbered, not dated: the thread keeps going past the web plan, and the order flexes with `gaps.md` and how I'm doing. Changes go in "Schedule changes" at the bottom.

## Order

| Sessions | Phase | Focus |
|---|---|---|
| 1 to 3 | Networking through the scaling lens | Refresh DNS, HTTP and TLS from the web records, then latency vs throughput and DNS as a system |
| 4 to 9 | Scaling basics | Performance vs scalability, availability vs consistency, CDNs, load balancers (layer 4 and 7, horizontal scaling), reverse proxies, caching |
| 10 to 12 | Estimates and the design approach | Back-of-the-envelope calculations and the four-step approach; a first walk-through (a URL shortener) |
| 13 onward | System design practice | Timed designs from the Alex Xu books' (Volume 1 first, Volume 2 later) and the primer's question lists, attempt first, feedback after; keeps going alongside the phases below |
| after the basics | Containers | What a container is and what Docker does; run one locally. Needs `docs.docker.com` allowed |
| then | Kubernetes | What it does and why, assuming containers and networking. Needs `kubernetes.io` allowed |

## First session

The learner is rereading chapter 1 of Volume 1 of the Alex Xu book on their own time. Session 1 starts with a typed, from-memory quiz on what stuck, then uses the primer's scalability section to fill gaps. The reading doesn't count against the 10 minutes.

## How each session works

1. Warm-up: 1 or 2 typed questions from due re-tests and open items in `gaps.md`.
2. Quiz first on the new topic, then explain. A miss goes in `gaps.md`.
3. Designs: I attempt first, then get feedback on what's missing.
4. Explain it back in my own words, then a learning record with a Re-test date.

## Overlap with the web plan

Where a web topic overlaps (how a page loads and DNS in week 7, caching, cookies and sessions in week 9), the web lesson asks one "what changes at scale?" question and leaves the depth for this thread.

## Schedule changes

| Date | Change | Reason |
|---|---|---|
