# DNS and URL re-tests: the lookup chain held, URL parts needed a second pass

Later on 24 Nov the learner continued with the DNS items still due from the day before, in applied forms. They also decided to stop being tested on mastery learning, so those items were removed from `how-to-learn/`.

## Evidence
- **A DNS answer, the TTL and a stale IP (applied):** for a TTL of 3600 and a server switch at noon, said a DNS answer has the IP and the TTL, that visitors can reach the old IP for up to 3600 seconds after it was cached, and that you should lower the TTL beforehand. Corrected: the TTL is a duration in seconds, not a time. After a narrower question, said to lower it at least the old TTL (3600 seconds) before the switch, and to raise it again afterwards. Correct.
- **Recursive vs iterative, and root, TLD, authoritative:** correct. Walked through an empty-cache lookup in order, with a referral at each step and the resolver caching the answer; the OS-to-resolver query is recursive and the resolver's queries are iterative. Fine point added: the resolver also caches the in-between answers, such as the `.com` servers.
- **The order of the caches:** correct. Browser cache, then the `hosts` file and OS cache, then the resolver; each stops if it has the answer, and the answer is cached back down the chain.
- **URL parts (a transfer, `https://shop.example.com:8443/cart?item=3#reviews`):** muddled at first. Said only the hostname goes to the server, that "the stuff after `/`" stays in the browser, and was unsure if the port goes to DNS. After narrower questions: only the hostname goes to DNS, the browser adds the port itself when it connects, `/cart?item=3` is in the request line, the fragment `#reviews` scrolls to the element with that id and never leaves the browser, and `https://` means HTTP over TLS. Held at 1 day.

## Decision
Move on for the DNS items (3 days). Correct the URL parts with another pass tomorrow or the day after. The mastery learning items are no longer tested by choice. No explain-back this session.

Re-test: on or after 2026-11-26 for URL vs hostname. On or after 2026-11-28 for the five DNS items.
