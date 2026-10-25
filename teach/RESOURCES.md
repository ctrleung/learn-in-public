# Networking Resources

> Sources marked **read** have been fetched and read in full for the cited section. Unverified entries were found by search only and must be read before any lesson cites them.

## Knowledge

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
- [AWS: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  Defines a VPC as a logically isolated virtual network, a subnet as a range of IP addresses in a VPC (within a single Availability Zone), route tables as deciding where traffic goes, and internet gateways as connecting the VPC to the internet. Use for: subnets and routing before going deeper into AWS.
- [AWS: Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
  A security group acts as a virtual firewall with inbound and outbound rules (source or destination, port range, protocol); only traffic allowed by the rules reaches the instance; security groups are stateful. Only the opening and basics sections have been read. Use for: firewalls as AWS applies them.

- [AWS: Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
  A network ACL allows or denies specific inbound or outbound traffic at the subnet level, as an extra layer on top of security groups. Only the opening and basics read. Use for: subnet-level filtering and how it differs from security groups (the comparison page it links to is not yet read).
- [AWS: Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
  A route table is the traffic controller for a VPC; each route has a destination (CIDR block) and a target (such as an internet gateway, NAT gateway, peering connection or VPN connection); traffic is routed by destination IP address. Only the opening read. Use for: public vs private subnets, once the zine's routing and CIDR pages are done.

- [ICANN: DNSSEC, What Is It and Why Is It Important?](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)
  Explains how DNS works (stub resolver, recursive resolver, authoritative name servers) and why DNS by itself is not secure: a resolver can only check that a response appears to come from the IP address it queried, and that source address can be forged. A forged answer accepted by a recursive resolver poisons its cache, so the resolver returns fraudulent data to other devices; the page's example is a fake bank site. DNSSEC adds digital signatures based on public key cryptography. Read through the opening of the DNSSEC section; the key trust and validation sections are not yet read. Use for: DNS attacks, as the follow-on to the zine's DNS pages.
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228) (`services.nvd.nist.gov`, replace the CVE id to look up another)
  NIST's National Vulnerability Database as data: description, publication date, analysis status, CVSS score and severity, and CISA known-exploited-vulnerability fields. For CVE-2021-44228 (Log4Shell) it returned a CVSS v3.1 score of 10.0, CRITICAL, with CISA dates of 2021-12-10 added and 2021-12-24 action due. The NVD website itself refuses automated requests, but this API works. Use for: reading an advisory and judging severity.
- [CVE Record API (MITRE)](https://cveawg.mitre.org/api/cve/CVE-2021-44228)
  The authoritative CVE record. For CVE-2021-44228 it returned state PUBLISHED, assigned by Apache. Use for: who reported it and the original description, to cross-check NVD.

### Not yet read

- [OSV (Open Source Vulnerabilities)](https://osv.dev/) and [CVE.org](https://www.cve.org/)
  Both reachable (home pages return 200; OSV's API also answered) but not yet read. Use for: finding which vulnerabilities affect specific open-source package versions, which is the practical "does this affect what I run?" question.
- [OWASP Cheat Sheet Series: HTTP Strict Transport Security](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
  Linked from the TLS cheat sheet as the guide to HSTS, one of the controls OWASP lists against man-in-the-middle attacks. Reachable but not read. Use for: the lesson on HTTPS enforcement.
- [Julia Evans: "Bite Size Networking" (paid zine, $10)](https://jvns.ca/blog/2019/03/15/new-zine--bite-size-networking-/)
  A separate, paid zine from 2019 on practical tools (tcpdump, DNS queries, inspecting SSL certificates, checking firewalls). Only the announcement post has been read. Use for: hands-on command-line troubleshooting, if you decide to buy it.
- Cloudflare Learning Center articles on DNS and TLS handshakes (cloudflare.com/learning). The site serves a bot check to automated requests, so I can't read it. The learner is reading these themselves.

## Wisdom (Communities)

Where to test skills with other practitioners. The learner asked for suggestions. None of these communities' own rules or moderation could be read from this environment (Reddit and the Stack Exchange sites are not reachable here), so descriptions come from third-party lists and an official AWS announcement; check each community's sidebar or rules before posting.

- [AWS re:Post](https://repost.aws/)
  Official community Q&A service launched by AWS in December 2021 (replacing the old AWS forums), where customers, partners and AWS staff answer questions on designing, building and operating workloads on AWS; members earn reputation for accepted answers. Source: [AWS announcement](https://aws.amazon.com/about-aws/whats-new/2021/12/aws-repost-community-question-answer-service). Use for: AWS questions once lessons reach VPCs and IAM.
- [r/homelab](https://www.reddit.com/r/homelab/)
  Reddit community for home lab setups, networking and virtualization projects (third-party lists, 2026, give member counts from about 700K to over 1M). Use for: hands-on practice ideas and "what did I get wrong in my setup" questions.
- [r/networking](https://www.reddit.com/r/networking/)
  Described by a third-party list as a subreddit for network professionals and enthusiasts covering hardware, protocols and troubleshooting. Use for: networking questions after reading the basics. Professional audience; expect to be asked to show your own research first.
- [r/sysadmin](https://www.reddit.com/r/sysadmin/) and [r/linuxadmin](https://www.reddit.com/r/linuxadmin/)
  Described as communities for system administrators and Linux administrators respectively. Use for: operations questions, once lessons reach Linux and monitoring.
- Stack Exchange sites: Server Fault, Information Security, Network Engineering (serverfault.com, security.stackexchange.com, networkengineering.stackexchange.com)
  Not verified from here; suggested from general knowledge of the Stack Exchange network. Use for: precise, well-formed questions with a single right answer. Stack Exchange sites expect you to search first and show your research.
- OWASP local chapters ([owasp.org/chapters](https://owasp.org/chapters/))
  OWASP has local chapters (page confirmed to exist; its list loads dynamically and could not be read). Use for: in-person or local meetups on application security, if one is near the learner. Needs the learner's location to check.

## Gaps

- **Firewalls beyond AWS.** Only AWS security groups and network ACLs are covered; no source read explains host or network firewalls in general.
- **How to read and triage a real advisory.** The data sources (NVD, MITRE, OSV) are now readable, but no guide on triage (is it exploitable here, what to patch first) has been read yet. CISA's known-exploited catalog is a candidate, but `www.cisa.gov` blocks automated reads; the learner can read it directly.
- **Cloudflare's DNS and TLS articles** are still blocked by a bot check; the learner is reading them themselves.
- **Community rules and activity** are unverified for every community above; pick one or two, read the sidebar, and prune the rest.
