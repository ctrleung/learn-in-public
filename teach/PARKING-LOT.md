# Parking lot

Parked, **not dropped**. These topics matter and I'll come back to them, but I'm not working on them during the 12-week web fundamentals plan (23 Nov 2026 to 14 Feb 2027) unless I ask for a lesson on one. When I do ask, it runs as a normal lesson, gets logged, and I note whether it pushes the schedule.

## Parked topics

- **AWS:** VPCs, subnets, routing, security groups, network ACLs, IAM
- **Containers:** Docker, images, scanning
- **Linux and operating systems**
- **Web servers and runtimes:** nginx, Apache, reverse proxies, language runtimes
- **Backend and databases**
- **DevOps:** CI/CD, infrastructure as code; scripting and automation
- **Operations and monitoring; system design**
- **Security beyond the browser:** identity, authentication and secrets; cryptography beyond TLS basics; vulnerability management (CVEs, advisories, triage)
- **Networking beyond the supporting slice:** TCP internals, UDP and DTLS, routing, subnets, firewalls, packet captures

## Parked resources

### AWS and vulnerabilities (moved from RESOURCES.md, unchanged)

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

### Communities (moved from RESOURCES.md, unchanged)

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

## Parked exercises (moved from exercises.md, unchanged)

- [ ] **Trace the route.** Run `traceroute google.com`.
  Notice: each line is a router your packets pass through on the way. *(Zine, routing page)*

- [ ] **See who's on your local network.** Run `arp -na`.
  Notice: the table maps IP addresses on your network to hardware (MAC) addresses. *(Zine, local networking page)*

- [ ] **Read a real advisory.** Run `curl "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"` (Log4Shell). Find the description, the severity score, and the CISA dates.
  Notice: how a single record tells you whether something is serious and being exploited. Then look at the same CVE at `cveawg.mitre.org`. *(NVD and MITRE APIs)*

- [ ] **Harden a TLS setup.** Run nginx in a container with a self-signed certificate, check which TLS versions it accepts, then change the config to allow only TLS 1.2 and 1.3 and check again. Look up the right directive name in nginx's documentation; OWASP says to default to TLS 1.3, allow 1.2 for compatibility, and disable 1.0, 1.1 and SSLv2/3. *(OWASP TLS)*

- [ ] **Generate a config.** Use Mozilla's SSL configuration generator (named in OWASP's cheat sheet) to produce an nginx config, and read what each setting does.

## Parked gaps

- **Firewalls beyond AWS.** Only AWS security groups and network ACLs were read; no source read explains host or network firewalls in general.
- **How to read and triage a real advisory.** NVD, MITRE and OSV are readable, but no triage guide has been read. CISA's known-exploited catalog is a candidate; `www.cisa.gov` blocks automated reads.
- **Community rules and activity** are unverified for every community above.

## Previous mission (before 20 Nov 2026)

## Mission: Systems & security foundations for an application developer

### Why
I build applications, but I'm less familiar with the systems underneath, such as networks, servers, containers and cloud, and I may have some knowledge gaps there. With cybersecurity vulnerabilities being found more often (including with AI), I want enough breadth to understand and mitigate them, and to grow at work, rather than only handle application code.

### Success looks like
- Read a vulnerability advisory (CVE) and decide whether it affects what I run, and what to do about it
- Trace a request from browser to server (DNS, TCP, TLS, HTTP, proxies) and explain where it can fail or be attacked
- Find my way around a Linux server, and understand containers and images well enough to scan and harden them
- Understand how a service is deployed, monitored and kept healthy, including on AWS
- Hold a confident conversation with ops and security colleagues, with a more than good enough foundation across the topics in the README

### Constraints
- Full-time job; energy is uneven, so lessons must be short and sessions flexible
- Can practice on anything: local machine, containers, an AWS account
- Mostly learning for myself, with notes public in this repo

### Out of scope
- Offensive security and penetration testing as a career path
- Certifications
- Deep dives into any single frontend framework
- Kernel internals and low-level OS development

