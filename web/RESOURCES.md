# Web Fundamentals Resources

> Sources marked **read** have been fetched and read for the cited section. Everything else is a map or a candidate: read the page before a lesson cites it. Networking and security sources for parked topics live in [`../systems/RESOURCES.md`](../systems/RESOURCES.md).

## Main resource: MDN, Learn web development

Section paths below come from MDN's Learn landing page, checked on 2026-11-20. **None of these section pages has been read yet**; each lesson reads its page first.

- **HTML and accessibility:** [Structuring content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) (basic syntax, headings and paragraphs, lists, links, document structure, metadata, images, forms, tables, table accessibility, debugging HTML) and [Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) (what is accessibility, HTML and accessibility, WAI-ARIA basics, CSS and JavaScript, multimedia, mobile, tooling, troubleshooting). Extension: [Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms) (how to structure a form, form validation).
- **CSS:** [Styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) (selectors, handling conflicts and the cascade, box model, sizing, overflow, values and units, pseudo-classes), [CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout) (flexbox, grids, positioning, responsive design, media queries) and [Text styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling) (fundamentals, web fonts).
- **Browser, HTTP and JavaScript:** [How browsers load websites](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_browsers_load_websites) and [Scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) (variables through functions and objects, events, event bubbling, DOM scripting, JSON, network requests, debugging). Extensions: [Async JS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS) (promises), [Advanced JavaScript objects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects) (prototypes, classes) and [Client-side APIs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs) (client-side storage, third-party APIs). HTTP itself: MDN's HTTP reference (path not yet checked).
- **React:** [Frameworks and libraries](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Frameworks_libraries) (introduction, main features, React getting started, components, to-do list, interactivity and state, filtering and conditional rendering, React accessibility, React resources).

## Supporting: networking (DNS, HTTP, TLS basics, how a page loads)

### Read

- [MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
  Beginner-level walk through clients and servers, DNS, TCP/IP, packets, HTTP, status codes and URL parts. Use for: the first mental model of a request. (The older URL under `Learn/Getting_started_with_the_web/` redirects here.)

- [High Performance Browser Networking, Ilya Grigorik: Transport Layer Security (TLS)](https://hpbn.co/transport-layer-security-tls/)
  Freely readable online (O'Reilly, 2013). Only the opening section (encryption, authentication, integrity) has been read so far. Use for: what TLS provides and why. Its table of contents also covers TCP, UDP, HTTP/2, certificates and chain of trust; check chapter content is still current before relying on specific settings, since the book is from 2013.

- [Julia Evans: Networking! ACK! (free zine, PDF)](https://wizardzines.com/zines/networking/)
  A free, 24-page comic for working programmers that follows one cat picture from a server to your laptop, written for web developers who know the names (HTTP, DNS, TCP) but not how they fit together. **Read in full.** Covers: the six steps of a download, the packet, DNS (recursive vs authoritative servers, root / TLD / site lookup chain, TTL caching, `dig` and `dig +trace`), sockets, TCP (sequence numbers, ACKs, retries, the SYN / SYN-ACK / ACK handshake, `tcpdump`), HTTP by hand with `nc`, headers, networking layers, ports, UDP, local networking (subnets, MAC addresses, ARP), routing across the internet (BGP, `traceroute`), CIDR notation, a one-page TLS overview, and a Wireshark exercise. Does not cover firewalls or attacks. Licensed CC-BY-NC-SA, so link to it; don't copy it into this repo. Use for: the main hands-on companion for the networking lessons.

- [MDN Glossary: DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS)
  Short definition: a hierarchical, decentralized naming system that maps domain names to IP addresses (a DNS lookup), with reverse DNS going the other way. Use for: a precise one-line definition.

- [OWASP Cheat Sheet Series: Transport Layer Security](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
  Practitioner guidance on TLS. Read: introduction, SSL vs TLS, server configuration (default to TLS 1.3, TLS 1.2 only for compatibility, TLS 1.0 and 1.1 formally deprecated and must be disabled, SSLv2 and SSLv3 always disabled, strong ciphers, disable compression, patch cryptographic libraries), the certificates section (key strength, SHA-256, correct domain names in the SAN, caution with wildcard certificates), and the HSTS and mutual TLS opening paragraphs. Later sections (application, references) not read. Use for: what a hardened TLS setup looks like, and as the current counterweight to HPBN's 2013 content.

- [OWASP: Manipulator-in-the-Middle attack](https://community.owasp.org/attacks/Manipulator-in-the-middle_attack)
  Describes how an attacker splits a TCP connection in two and acts as a proxy that can read, insert and modify data; most effective over unencrypted HTTP; still possible over HTTPS with two separate TLS sessions; listed controls are enforcing HTTPS and HSTS, secure session management and proper certificate validation. Caveat: the page says it was ported from an old wiki and still needs work, so treat it as an overview and cross-check specifics. Use for: the attacker's view of why TLS authentication matters.

- [ICANN: DNSSEC, What Is It and Why Is It Important?](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)
  Explains how DNS works (stub resolver, recursive resolver, authoritative name servers) and why DNS by itself is not secure: a resolver can only check that a response appears to come from the IP address it queried, and that source address can be forged. A forged answer accepted by a recursive resolver poisons its cache, so the resolver returns fraudulent data to other devices; the page's example is a fake bank site. DNSSEC adds digital signatures based on public key cryptography. Read through the opening of the DNSSEC section; the key trust and validation sections are not yet read. Use for: DNS attacks, as the follow-on to the zine's DNS pages.

### Not yet read

- [OWASP Cheat Sheet Series: HTTP Strict Transport Security](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
  Linked from the TLS cheat sheet as the guide to HSTS, one of the controls OWASP lists against man-in-the-middle attacks. Reachable but not read. Use for: the lesson on HTTPS enforcement.

- Cloudflare Learning Center articles on DNS and TLS handshakes (cloudflare.com/learning). The site serves a bot check to automated requests, so I can't read it. The learner is reading these themselves.

## Gaps

- **MDN pages unread.** Every section above still has to be read before a lesson uses it.
- **Blocked by the network settings** (tested 2026-11-20): react.dev, w3.org (WAI), web.dev, webaim.org, a11yproject.com, javascript.info and html.spec.whatwg.org. MDN's React module may be enough for an introduction, but React depth beyond it would need react.dev. Add the hosts you want read.
- **MDN's HTTP reference** path is unconfirmed. Check it before the HTTP lessons.
- **Cloudflare's DNS and TLS articles** are blocked by a bot check; the learner reads them directly.
- **Communities for web development** have not been chosen. Earlier community suggestions are in `../systems/RESOURCES.md`.
