# Mission: Understand how web systems scale and connect, and be able to do system design

## Why
I build web applications and want to understand how they scale and how the pieces connect (networking, load balancing, caching, CDNs, then containers and Kubernetes), and to be able to talk through a system design, including in a system design interview, instead of only handling application code. This runs as one short session a week alongside the web and Japanese plans.

## Success looks like
- Explain how a request moves through a scaled system (DNS, CDN, load balancer, reverse proxy, application servers, cache, database) and what each part is for
- Explain performance vs scalability, latency vs throughput, and availability vs consistency in my own words, with an example of each
- Talk through a design for a simple system (a URL shortener is a good first one) in four steps: use cases, constraints and assumptions; a high-level design; the core components; then scaling it, including a back-of-the-envelope estimate
- Explain what containers are and what Kubernetes does, and run a container locally
- Do timed practice designs where I attempt first and get feedback afterwards, for system design interview practice

## Constraints
- One short session of about 10 minutes a week, on a weekend; the first thing to skip when I'm tired, with web and Japanese protected
- Sources: my system design interview book, the System Design Primer, MDN's HTTP reference and caching pages, AWS Well-Architected; Docker and Kubernetes docs once their domains are allowed
- Quiz first, then explain; I produce answers and designs myself, and feedback comes after an attempt
- Mostly learning for myself, with notes public in this repo. Interview dates and other personal timing are not recorded here

## Out of scope
- AWS service-specific depth, Linux, DevOps, security beyond the browser and backend or database deep dives (parked in `PARKING-LOT.md`)
- Certifications
- Distributed systems theory beyond what the primer covers
