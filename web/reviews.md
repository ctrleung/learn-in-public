# Reviews

The live review queue: one row per item. The stages are 1, 3, 7, 14 and 30 days. A correct answer from memory moves an item up a stage; a miss sends it back to 1 day and adds it to `gaps.md`. An item is **mastered** after it passes the 14-day and 30-day tests. Reviews come before new material. The test should vary in form each time (explain, apply, compare). At the 7, 14 and 30 day stages, at least one test is an explanation to a specific audience.

| Item | Topic | Source | Stage | Last result | Due |
|---|---|---|---|---|---|
| 503 status code | HTTP and the web: Status codes | gaps.md, record 0003 | 1 day | correct with hints, 2026-11-23 (the status-family table worked: 5xx is the server's problem, retry later); test again in a different form, without the table | 2026-11-24 |
| DNS terms: Domain Name System, maps a domain name to an IP address | Networking: DNS and name resolution | gaps.md | 3 days | correct, 2026-11-23 (name and mapping right; hostname vs URL, including www, was shaky at first) | 2026-11-26 |
| Integrity detects tampering; all three TLS services together stop a man-in-the-middle attack | Networking: TLS and HTTPS | gaps.md, record 0003 | 3 days | correct, 2026-11-23 (integrity detects, not prevents; all three together stop the attack) | 2026-11-26 |
| The four steps of a request | Networking: The request journey | record 0001 | 7 days | correct, 2026-10-29 | overdue (2026-11-05) |
| The three TLS services and the attack each stops | Networking: TLS and HTTPS | record 0003 | 7 days | mostly correct, 2026-11-23 (briefly gave impersonation to integrity; fixed in the session); stage held | 2026-11-26 |
| Roles of DNS, TCP/IP, TLS and HTTP | Networking: The request journey | record 0003 | 7 days | correct, 2026-10-29 | overdue (2026-11-05) |
| 301 means permanently moved | HTTP and the web: Status codes | record 0002 | 7 days | correct, 2026-10-29 | overdue (2026-11-05) |
| What a DNS answer contains (name, TTL, type A or AAAA, IP) and what the TTL is for | Networking: DNS and name resolution | chat, 2026-11-23 | 1 day | correct on TTL trade-off; record types not yet tested | 2026-11-24 |
| The order of DNS caches (browser, OS, recursive resolver, then the DNS hierarchy) | Networking: DNS and name resolution | chat, 2026-11-23 | 1 day | order right; needs the hierarchy step and "resolver does the legwork" | 2026-11-24 |
| After an IP change, who may still hold the old IP and for how long (up to the TTL, per cache) | Networking: DNS and name resolution | chat, 2026-11-23 | 1 day | named the three caches, timing needed hints | 2026-11-24 |
| URL vs hostname: which part goes to DNS (the full hostname, including www) | HTTP and the web: URLs | chat, 2026-11-23 | 1 day | corrected in the session | 2026-11-24 |
| Recursive vs iterative DNS queries: who does the work in each, and which step uses which | Networking: DNS and name resolution | record 0006 | 1 day | correct in own words, 2026-11-23 | 2026-11-24 |
| On a cache miss the resolver asks root, then TLD, then authoritative server; each answers with a referral | Networking: DNS and name resolution | record 0006 | 1 day | root-first fixed after one prompt | 2026-11-24 |
| Explain-back: address lookup to a non-technical friend (big idea first, analogy, why it matters) | Networking: DNS and name resolution | record 0006 | 7 days | first explain-back strong; missing big-idea opening and an analogy | 2026-11-30 |
| HTML element vs tag, and void elements | HTML: Element anatomy and attributes | HTML pre-test, record 0007 | 1 day | named after a prompt, 2026-11-23 | 2026-11-24 |
| What the doctype does (standards mode vs quirks mode) | HTML: Document structure | HTML pre-test, record 0007 | 1 day | partly right, 2026-11-23 | 2026-11-24 |
| What goes in `<html>` and `<head>`: lang, title, charset, viewport, and which are required | HTML: Document structure | HTML pre-test, record 0007 | 1 day | missed lang, charset, viewport, 2026-11-23 | 2026-11-24 |
| Why heading levels matter (outline, screen readers, no skipped levels) | HTML: Headings and paragraphs | HTML pre-test, record 0007 | 1 day | partly right, 2026-11-23 | 2026-11-24 |
