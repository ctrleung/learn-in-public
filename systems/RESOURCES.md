# Systems Resources

> Sources marked **read** were fetched and read for the cited section. Everything else is a candidate: read the page before a lesson cites it. The parked resources from before 21 Nov 2026 are kept below.

## Active sources

- [The System Design Primer (GitHub, donnemartin/system-design-primer)](https://github.com/donnemartin/system-design-primer)
  A long community guide to designing large-scale systems, aimed at system design interviews. **Only its table of contents has been read.** Its sections include performance vs scalability, latency vs throughput, availability vs consistency (CAP), consistency and availability patterns, DNS, CDNs (push and pull), load balancers (layer 4 and 7, horizontal scaling), reverse proxies, the application layer (microservices, service discovery), a four-step approach to a design question, back-of-the-envelope calculations, and worked questions (Pastebin or bit.ly first). It also links Anki flashcards. Read the raw file at `raw.githubusercontent.com/donnemartin/system-design-primer/master/README.md`, since github.com blocks automated reads. A popular community resource, not an authority. Use for: the main sequence for the scaling and design sessions.
- **System Design Interview, by Alex Xu: Volume 1 (the learner says edition 2) and Volume 2, both the learner's own.**
  Start with Volume 1, which search results describe as the fundamentals, then Volume 2 (a sequel with more specialized designs and trade-offs) later, in the interview-practice phase. The learner read chapter 1 of Volume 1 a few months ago and is rereading it. Not read by Claude, and Claude can't see its content, so lessons follow the chapters the learner says they're on and cross-check ideas against the primer. Use for: the learner's main interview-practice text alongside the primer. Quiz on the concepts and run designs in chat, with the learner attempting first.
- [MDN: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) and [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
  Reachable, not read. Use for: caching, one of the overlaps with the web plan.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
  Reachable, not read. Use for: a vendor's view of reliability, performance and cost at scale, cross-checked against the primer.
- **Docker docs** (`docs.docker.com`) and **Kubernetes docs** (`kubernetes.io`)
  Blocked by the network settings. Add both domains before the container and Kubernetes sessions.

## Gaps

- The primer's sections are unread beyond headings; each session reads its section first.
- Docker and Kubernetes docs are blocked.
- The learner has read chapter 1 of Volume 1 and is rereading it; later chapters and Volume 2 are unread. Claude can't read it, so lessons rely on what the learner shares.

## Parked resources (kept, not in the current plan)


### AWS and vulnerabilities

- [AWS: What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  Defines a VPC as a logically isolated virtual network, a subnet as a range of IP addresses in a VPC (within a single Availability Zone), route tables as deciding where traffic goes, and internet gateways as connecting the VPC to the internet. Use for: subnets and routing before going deeper into AWS.

- [AWS: Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
  A security group acts as a virtual firewall with inbound and outbound rules (source or destination, port range, protocol); only traffic allowed by the rules reaches the instance; security groups are stateful. Only the opening and basics sections have been read. Use for: firewalls as AWS applies them.

- [AWS: Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
  A network ACL allows or denies specific inbound or outbound traffic at the subnet level, as an extra layer on top of security groups. Only the opening and basics read. Use for: subnet-level filtering and how it differs from security groups (the comparison page it links to is not yet read).

- [AWS: Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
  A route table is the traffic controller for a VPC; each route has a destination (CIDR block) and a target (such as an internet gateway, NAT gateway, peering connection or VPN connection); traffic is routed by destination IP address. Only the opening read. Use for: public vs private subnets, once the zine's routing and CIDR pages are done.

- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228) (`services.nvd.nist.gov`, replace the CVE id to look up another)
  NIST's National Vulnerability Database as data: description, publication date, analysis status, CVSS score and severity, and CISA known-exploited-vulnerability fields. For CVE-2021-44228 (Log4Shell) it returned a CVSS v3.1 score of 10.0, CRITICAL, with CISA dates of 2021-12-10 added and 2021-12-24 action due. The NVD website itself refuses automated requests, but this API works. Use for: reading an advisory and judging severity.

- [CVE Record API (MITRE)](https://cveawg.mitre.org/api/cve/CVE-2021-44228)
  The authoritative CVE record. For CVE-2021-44228 it returned state PUBLISHED, assigned by Apache. Use for: who reported it and the original description, to cross-check NVD.

- [OSV (Open Source Vulnerabilities)](https://osv.dev/) and [CVE.org](https://www.cve.org/)
  Both reachable (home pages return 200; OSV's API also answered) but not yet read. Use for: finding which vulnerabilities affect specific open-source package versions, which is the practical "does this affect what I run?" question.

- [Julia Evans: "Bite Size Networking" (paid zine, $10)](https://jvns.ca/blog/2019/03/15/new-zine--bite-size-networking-/)
  A separate, paid zine from 2019 on practical tools (tcpdump, DNS queries, inspecting SSL certificates, checking firewalls). Only the announcement post has been read. Use for: hands-on command-line troubleshooting, if you decide to buy it.

### Communities

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

## Parked gaps

- **Firewalls beyond AWS.** Only AWS security groups and network ACLs were read; no source read explains host or network firewalls in general.
- **How to read and triage a real advisory.** NVD, MITRE and OSV are readable, but no triage guide has been read. CISA's known-exploited catalog is a candidate; `www.cisa.gov` blocks automated reads.
- **Community rules and activity** are unverified for every community above.
