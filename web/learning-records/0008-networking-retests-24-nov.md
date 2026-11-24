# Networking re-tests: the request journey and TLS held up, redirects and DNS-vs-HTTP needed work

A warm-up of five questions from overdue and due items. The learner stopped after the reviews.

## Evidence
- **Four steps of a request (overdue since 5 Nov):** described address lookup and the caches in good detail and correctly guessed that "can't be reached" is a step 1 failure. They reversed TCP and TLS at first and then explained correctly that TLS builds on TCP. They did not name request, response and assembly as the steps: the connection, request and response were merged and assembly was missing. Partly right, sent back to 1 day.
- **HTTP, HTTPS and TLS (roles item):** correct. HTTPS is HTTP over TLS, which adds the security. Moved to 14 days.
- **301:** knew it is a permanent move and that the new location is in the response, but not the `Location` header (not yet covered). Wondered if DNS would handle a temporary move; after a narrower question they saw that DNS maps only a hostname to an IP, cannot handle paths and would not change the address bar. Moved to 14 days.
- **503 in a new form (an API under load):** correct from memory. Backend overloaded, show an error in the client, look at load balancing and issues on the server. Needed prompting to add retry with backoff and `Retry-After`. Moved to 3 days.
- **Mastery threshold (learning notes):** gave the 80 to 90 percent range, but first said it protects against staying too long; after a narrower question said gaps stay and weaken the next topic. Partly right.
- **Extra questions while reading the notes:** the browser does not query DNS servers directly (the OS does, then the resolver); only the recursive resolver queries the root, TLD and authoritative servers, and the shared cache is why; 3xx is not all redirects (304 is a cache answer); an IP packet header holds source and destination IP; a packet is a chunk of data.

## Decision
Correct: re-test the four steps by name tomorrow. Enrich, then move on: the rest held. The DNS items and the four HTML items (due today) were not reached and carry over. No explain-back this session.

## Later in the session: the four HTML items
The learner chose to continue with the HTML items from the 23 Nov pre-test, now in new forms (apply and predict).
- **Elements and void elements:** correct after one retry. First said "an element is the element in general"; then said an element is the tags, attributes and content, and the tags are the markup in angle brackets. Named `p`, `br` and `a` and said only `br` is void.
- **The doctype:** correct. Without it the browser uses quirks mode and behaviour can differ across browsers. Thought it is not an element "because it is not displayed"; corrected: it is a declaration, and `head`, `title` and `meta` are elements that are not displayed.
- **`lang`, viewport, charset and what is required:** named `lang` and viewport, and charset after a hint. Said only the title would be an error, which is right for the title; charset's encoding declaration is also required by the spec.
- **Heading levels:** found `h1` jumping to `h4` and an `h4` before an `h2`. Said screen readers read headings "by size"; corrected: they use the level, and size is only CSS. Missed that a paragraph styled to look like a heading is not a heading until prompted.

Re-test: on or after 2026-11-25 for `lang` and the head and for heading levels. On or after 2026-11-27 for element vs tag and the doctype.

Re-test (networking): on or after 2026-11-25 for the four steps, redirects, TCP and TLS, and the mastery threshold. On or after 2026-11-27 for 503. On or after 2026-12-08 for the roles item and 301.
