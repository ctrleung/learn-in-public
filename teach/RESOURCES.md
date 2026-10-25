# Networking Resources

> Sources marked **read** have been fetched and read in full for the cited section. Unverified entries were found by search only and must be read before any lesson cites them.

## Knowledge

### Read

- [MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
  Beginner-level walk through clients and servers, DNS, TCP/IP, packets, HTTP, status codes and URL parts. Use for: the first mental model of a request. (The older URL under `Learn/Getting_started_with_the_web/` redirects here.)
- [High Performance Browser Networking, Ilya Grigorik: Transport Layer Security (TLS)](https://hpbn.co/transport-layer-security-tls/)
  Freely readable online (O'Reilly, 2013). Only the opening section (encryption, authentication, integrity) has been read so far. Use for: what TLS provides and why. Its table of contents also covers TCP, UDP, HTTP/2, certificates and chain of trust; check chapter content is still current before relying on specific settings, since the book is from 2013.

- [Julia Evans: Networking! ACK! (free zine, PDF)](https://wizardzines.com/zines/networking/)
  A free, 24-page comic for working programmers that follows one cat picture from a server to your laptop, written for web developers who know the names (HTTP, DNS, TCP) but not how they fit together. Read so far: pages 1-7 and 23-24 (cast of characters, the packet, the six steps, and DNS including recursive vs authoritative servers, the root / TLD / site lookup chain, and TTL caching) plus the closing page, which recommends HPBN and the tools `dig`, `traceroute`, `tcpdump`, `ifconfig`, `netcat`, `wireshark` and `netstat` for practice. Pages 8-22 (sockets, TCP, HTTP and more) not yet read. Licensed CC-BY-NC-SA, so link to it; don't copy it into this repo. Use for: a friendly second explanation of the request journey and DNS.
- [MDN Glossary: DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS)
  Short definition: a hierarchical, decentralized naming system that maps domain names to IP addresses (a DNS lookup), with reverse DNS going the other way. Use for: a precise one-line definition.

- [OWASP Cheat Sheet Series: Transport Layer Security](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
  Practitioner guidance on TLS. Read: the introduction (TLS gives confidentiality, integrity and authentication) and the SSL vs TLS section (SSL versions 2 and 3 have serious cryptographic weaknesses and should no longer be used; TLS 1.0 to 1.3 followed). The server configuration and certificates sections are not yet read. Use for: what a secure TLS setup looks like, once those sections are read.
- [OWASP: Manipulator-in-the-Middle attack](https://community.owasp.org/attacks/Manipulator-in-the-middle_attack)
  Describes how an attacker splits a TCP connection in two and acts as a proxy that can read, insert and modify data; most effective over unencrypted HTTP; still possible over HTTPS with two separate TLS sessions; listed controls are enforcing HTTPS and HSTS, secure session management and proper certificate validation. Caveat: the page says it was ported from an old wiki and still needs work, so treat it as an overview and cross-check specifics. Use for: the attacker's view of why TLS authentication matters.
- [AWS: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  Defines a VPC as a logically isolated virtual network, a subnet as a range of IP addresses in a VPC (within a single Availability Zone), route tables as deciding where traffic goes, and internet gateways as connecting the VPC to the internet. Use for: subnets and routing before going deeper into AWS.
- [AWS: Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
  A security group acts as a virtual firewall with inbound and outbound rules (source or destination, port range, protocol); only traffic allowed by the rules reaches the instance; security groups are stateful. Only the opening and basics sections have been read. Use for: firewalls as AWS applies them.

### Unverified (not yet read)

- [Julia Evans: "Bite Size Networking" (paid zine, $10)](https://jvns.ca/blog/2019/03/15/new-zine--bite-size-networking-/)
  A separate, paid zine from 2019 on practical tools (tcpdump, DNS queries, inspecting SSL certificates, checking firewalls). Only the announcement post has been read, and the zine itself has not. Use for: hands-on command-line troubleshooting, if you decide to buy it.
- Cloudflare Learning Center articles on DNS and TLS handshakes (cloudflare.com/learning). The site shows a bot-check page ("Just a moment... Enable JavaScript") instead of the article, so it can't be read from here. Use for: DNS resolution steps and the TLS handshake, if you paste the text in.

## Wisdom (Communities)

- None chosen yet. Ask before suggesting any; the learner hasn't said whether they want communities.

## Gaps

- Cloudflare's DNS and TLS articles are still blocked by a bot check; not needed now that the zine and MDN cover DNS.
- Not yet read: the rest of the OWASP TLS cheat sheet (server configuration, certificates), AWS network ACLs (the stateless counterpart to security groups), and how routing works outside AWS.
