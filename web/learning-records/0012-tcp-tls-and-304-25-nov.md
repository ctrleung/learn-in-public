# HTTP over TCP and TLS, and 304: both held

Later on 25 Nov the learner continued with the two items left over from the 1-day batch.

## Evidence
- **HTTP vs HTTPS (a comparison):** after the IP is found, HTTP opens a TCP connection and sends the request over it; HTTPS does the same TCP handshake, then a TLS handshake, then sends the request. First said HTTPS is "built on top of HTTP"; when asked to stack HTTP, TLS and TCP, said TCP is the bottom, HTTP runs on it, TLS is added to make it secure for HTTPS. My reply described the stack as if TLS always sat between HTTP and TCP, which is only true for HTTPS; the learner pointed this out and drew it correctly: HTTP over TCP, and HTTPS as HTTP over TLS over TCP. Correct.
- **304 Not Modified:** correct. It is not a redirect; it means the saved copy is still current, so the browser uses its cached stylesheet and does not download it again. Conditional requests (`ETag`, `If-None-Match`) were mentioned only as a preview for the caching topic.

## Decision
Move on: both items to 3 days. No explain-back this session.

Re-test: on or after 2026-11-28.
