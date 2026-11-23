# Explain-back: address lookup (DNS and the cache chain)

The learner explained step 1 of a page load (address lookup) from memory, by dictation, to a junior developer. They then answered two follow-ups and a question on recursive vs iterative queries.

## Evidence
- Order of the chain was right: browser DNS cache, a call to the OS, the `hosts` file, the OS cache, the recursive resolver (ISP or a public one), then the lookup down the hierarchy. The TTL check was applied at each cache, and the TCP handshake came after the lookup.
- Reasons given for the lookup: names are easier to remember than IPs, and IPs can change.
- Why three caches: browser (you), OS (everything on the machine), resolver (everyone using it), so a lookup by one person helps the next.
- Recursive vs iterative, in their words: in a recursive query the side asked does all the work and returns only the final answer (OS to resolver). In an iterative query the side asked returns only what it knows, and the asker does the next step (resolver to root, TLD and authoritative servers).

## Corrections
- Say "DNS cache", not "IP cache", and define DNS early (Domain Name System: maps a domain name to an IP address).
- The hostname is looked up, not the whole web address.
- On a miss the resolver asks the root server first, then the TLD server, then the authoritative server (first attempt said "TLD first"; fixed when asked again).
- The answer is cached at each level on the way back, with its TTL.
- A stale cached IP does not make an invalid request: the request goes to the old IP. A shut-down server means a failed connection, a still-running one may serve old content, and a different site on that IP should fail the TLS certificate check. The TTL is set by the site owner; 300 seconds was only an example.
- The resolver's cache also takes load off the root, TLD and authoritative servers.
- For HTTPS, a TLS handshake follows the TCP handshake and comes before the request.
- Still to practice: open with a one-sentence big idea, and add an analogy of their own.

## Decision
Enrich, then move on: the explanation held up. Re-test with an explain-back to a different audience.

Re-test: on or after 2026-11-30 for a one-minute explain-back of address lookup to a non-technical friend, with an analogy and the big idea first.
