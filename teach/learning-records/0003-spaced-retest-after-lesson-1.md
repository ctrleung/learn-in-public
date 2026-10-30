# Spaced re-test after lesson 1: layers and TLS solid, 503 still open

Three days after lesson 1 the learner re-tested from memory. They gave the three TLS services and matched them to the right attacks (authentication stops impersonation, encryption stops reading), and described DNS, TCP/IP, TLS and HTTP each in the right role. The 301 mix-up from the first recall check is fixed: they now say 301 is a permanent move. 503 is still unknown to them. Their wording on integrity was loose: they said it "prevents man in the middle", but integrity detects tampering with messages; the man-in-the-middle attack as a whole is stopped by all three services together.

## Evidence
- Written free recall, no looking back, three days after the first session.
- Correct: 301, 403, 404; three TLS services; roles of DNS, TCP/IP, TLS, HTTP.
- Gaps: 503 (should be: the server can't handle the request right now, usually temporarily); integrity detects tampering rather than preventing the attack; says "domain name service" for DNS (it is the Domain Name System) and "URL to IP" (DNS maps a domain name, one part of a URL).

## Implications
- Lesson 1 is solid enough to build on. Move to lesson 2 (DNS in depth, caching, attacks).
- Re-test 503 once more in a few days; the earlier 301 vs 401 and 503 vs 500 worry is half resolved.
- When TLS comes up again, have the learner explain how the three services together answer a man-in-the-middle attack.
