# Re-tests on 26 Nov: TLS and the redirect mix-up held, DNS wording slipped

A warm-up of four questions from the oldest open gaps and the 1-day items. The learner stopped after the reviews.

## Evidence
- **DNS terms (the three strings):** said DNS maps hostnames to IP addresses, that `www.example.com` is what goes to DNS, and that `www` is part of it because it is a subdomain. Slipped to "domain name service" (said by voice-to-text) instead of Domain Name System, the same wording gap as 29 Oct. Back to 1 day.
- **The three TLS services and integrity:** correct. Integrity, authentication and encryption stop tampering, spoofing and snooping, and all three are needed against a man-in-the-middle. Integrity detects tampering, which they said precisely on the second try. The integrity gap has two correct answers (23 and 26 Nov) and is fixed. The three-services item moved to 14 days, and the integrity item to 7 days.
- **Heading levels (a recipe page):** correct with no hint: `h1` title, `h2` sections, `h3` sub-parts, screen readers use the hierarchy, and size is CSS. Moved to 3 days. The other heading gap, a paragraph styled like a heading, was not tested.
- **Redirects (`/about-us` to `/about`):** correct. 301 and `Location`, the browser's HTTP cache remembers it, and DNS is not involved because only the path changed. Moved to 3 days; the redirect-cache gap has its first correct answer.
- The doctype's original purpose, correct nesting, and the `body` and void elements were not reached and carry over.

## Decision
Move on for TLS, heading levels and redirects. Check the DNS name again tomorrow. No explain-back this session.

Re-test: on or after 2026-11-27 for DNS terms, the doctype's original purpose, nesting, the `body` and void elements, and the styled-paragraph heading gap. On or after 2026-11-29 for heading levels and redirects. On or after 2026-12-03 for integrity. On or after 2026-12-10 for the three TLS services.
