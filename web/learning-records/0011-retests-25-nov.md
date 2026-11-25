# Re-tests on 25 Nov: the four steps and the head held, heading levels and redirects need another pass

A warm-up of four questions from the 1-day items. The learner stopped after the reviews.

## Evidence
- **The four steps of a request, by name:** correct (address lookup, request, response, assembly). Moved to 3 days; the gap from 24 Nov has its first correct answer.
- **The head (a diagnosis):** from a page that showed "cafÃ©" and looked zoomed out on a phone, correctly named charset and viewport and said what each does, and said `lang` sets the page language. Corrected: they are `<meta>` elements, and the viewport meta makes the page use the device width. Correct with no hint. Moved to 3 days.
- **Heading levels (a designer's request):** would keep the `h2` and use CSS to change the size, but the reason a user cares (screen reader users navigate by the heading hierarchy, so the level tells them what sits under each heading) came only after my explanation. Held at 1 day.
- **Redirects (a two-week campaign page):** chose 302 or 307 and the `Location` header correctly. For why not a 301, first said a visitor might still be redirected "because of the DNS cache"; after a correction said the HTTP cache stores the status and path, so a permanent redirect can be followed without asking the server. This repeats the DNS-vs-HTTP mix-up from 24 Nov. Held at 1 day with a gap.
- TCP before TLS and 304 were not reached and carry over.

## Decision
Move on for the four steps and the head. Correct the heading-level reason and the redirect caching with another pass tomorrow, in a different form each. No explain-back this session.

Re-test: on or after 2026-11-26 for heading levels and redirects (and TCP before TLS and 304, which were due 25 Nov). On or after 2026-11-28 for the four steps and the head.
