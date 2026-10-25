# Networking Resources

> Sources marked **read** have been fetched and read in full for the cited section. Unverified entries were found by search only and must be read before any lesson cites them.

## Knowledge

### Read

- [MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
  Beginner-level walk through clients and servers, DNS, TCP/IP, packets, HTTP, status codes and URL parts. Use for: the first mental model of a request. (The older URL under `Learn/Getting_started_with_the_web/` redirects here.)
- [High Performance Browser Networking, Ilya Grigorik: Transport Layer Security (TLS)](https://hpbn.co/transport-layer-security-tls/)
  Freely readable online (O'Reilly, 2013). Only the opening section (encryption, authentication, integrity) has been read so far. Use for: what TLS provides and why. Its table of contents also covers TCP, UDP, HTTP/2, certificates and chain of trust; check chapter content is still current before relying on specific settings, since the book is from 2013.

### Unverified (found by search, not yet read)

- [Julia Evans: "Bite Size Networking" zine announcement](https://jvns.ca/blog/2019/03/15/new-zine--bite-size-networking-/)
  Announcement of a paid zine on practical tools such as tcpdump, DNS queries and inspecting certificates. Use for: hands-on command-line tooling, once the zine is confirmed.
- Cloudflare Learning Center articles on DNS and TLS handshakes (cloudflare.com/learning). The site returned HTTP 403 to automated requests, so the pages couldn't be read. Use for: DNS resolution steps and the TLS handshake, once readable (try pasting the text in).

## Wisdom (Communities)

- None chosen yet. Ask before suggesting any; the learner hasn't said whether they want communities.

## Gaps

- A readable source for DNS resolution steps (resolver, root, TLD, authoritative servers). Cloudflare pages blocked automated reads.
- A primary source for security-focused networking (DNS spoofing, man-in-the-middle, firewalls); OWASP and vendor docs are candidates to check once reachable.
- A source for subnets, routing and firewalls (needed before AWS VPCs).
