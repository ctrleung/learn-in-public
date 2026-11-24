# Networking re-tests: the request journey and TLS held up, redirects and DNS-vs-HTTP needed work

A warm-up of five questions from overdue and due items. The learner stopped after the reviews.

## Evidence
- **Four steps of a request (overdue since 5 Nov):** described address lookup and the caches in good detail and correctly guessed that "can't be reached" is a step 1 failure. They reversed TCP and TLS at first and then explained correctly that TLS builds on TCP. They did not name request, response and assembly as the steps: the connection, request and response were merged and assembly was missing. Partly right, sent back to 1 day.
- **HTTP, HTTPS and TLS (roles item):** correct. HTTPS is HTTP over TLS, which adds the security. Moved to 14 days.
- **301:** knew it is a permanent move and that the new location is in the response, but not the `Location` header (not yet covered). Wondered if DNS would handle a temporary move; after a narrower question they saw that DNS maps only a hostname to an IP, cannot handle paths and would not change the address bar. Moved to 14 days.
- **503 in a new form (an API under load):** correct from memory. Backend overloaded, show an error in the client, look at load balancing and issues on the server. Needed prompting to add retry with backoff and `Retry-After`. Moved to 3 days.
- **Mastery threshold (learning notes):** gave the 80 to 90 percent range, but first said it protects against staying too long; after a narrower question said gaps stay and weaken the next topic. Partly right.
- **Questions while reading the notes** (3xx is not all redirects and 304 is a cache answer, the `Location` header, what an IP packet header holds, the browser asking the OS while only the resolver queries the hierarchy) were answered and the facts added to `web/reference/lesson-1-request-journey.md` and `web/reference/dns-answers-and-caching.md`.

## Decision
Correct: re-test the four steps by name tomorrow. Enrich, then move on: the rest held. The DNS items and the four HTML items (due today) were not reached and carry over. No explain-back this session. The four HTML items, tested later the same day, are in record 0009.

Re-test: on or after 2026-11-25 for the four steps, redirects, TCP and TLS, and the mastery threshold. On or after 2026-11-27 for 503. On or after 2026-12-08 for the roles item and 301.
