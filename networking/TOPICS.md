# Topics for networking

The source of truth for the Networking subject on the Mastery Map, in the same format as `web/TOPICS.md` (tag `plan` means it is in a plan or the networking records; `extra` is on top). This subject is for later: web comes first, so nothing here is scheduled yet. The earlier networking lessons and their records are in `web/` (learning records 0001 to 0003 and 0005 to 0006, and the `reference/` notes).

## Networking (later)


| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | The request journey | name the four steps of a request (address lookup, request, response, assembly) and say which step a given failure belongs to | plan |
| 2 | DNS and name resolution | say what DNS maps, read a DNS answer (name, TTL, type, value), trace the browser, OS and resolver caches, and tell recursive from iterative queries | plan |
| 3 | TCP/IP and the layers | say what an IP address, a port and a packet are, compare the OSI model and the TCP/IP model, describe the TCP handshake, and say how TCP, UDP and ICMP differ | plan |
| 4 | IP addressing and subnets | tell IPv4 from IPv6 and public from private addresses, and read a subnet and a CIDR block | extra |
| 5 | Local networks: MAC, ARP, DHCP and NAT | explain MAC addresses, ARP and DHCP, and explain how NAT lets many devices share one public address | extra |
| 6 | TLS and HTTPS | name the three TLS services and the attack each stops, say what a certificate proves, and outline the handshake | plan |
| 7 | Network performance | say what latency, bandwidth and throughput are, why round trips matter, and how caching, compression and a CDN reduce them | extra |
| 8 | Troubleshooting with command-line tools | use `ping`, `traceroute`, `dig` or `nslookup`, `netstat` or `ss` and `curl`, and read what each tells you about where a connection fails | extra |
| 9 | Network attacks and defences | say how DoS and DDoS attacks work and what a firewall does | extra |
| 10 | Hosting, domains and CDNs | say what a domain registrar, a host and a CDN each do, and where a load balancer sits (the depth is in the systems sessions) | extra |

## Network engineering reference (optional, not tracked on the map)

A reference for the rest of the network engineer roadmap, not a list to master. Study a group only when you need it. A group is tracked on the map only if you move it into the Networking list above.

| Group | What it is for |
|---|---|
| Other application protocols | SSH (remote shells), FTP and SFTP (file transfer), SMTP and IMAP (email), NTP (time) |
| Network types | LAN, WAN, WLAN, VPN, client-server and peer-to-peer |
| Network devices | routers, switches, hubs, modems and access points |
| Routing | static and dynamic routing, default gateway, and the protocols BGP, OSPF, RIP and EIGRP |
| Switching | VLANs, VXLAN, spanning tree, link aggregation, MAC address tables |
| Tunnels and VPNs | IPSec and SSL VPN, site-to-site and remote access, GRE tunnels |
| Wireless | Wi-Fi standards, channels and coverage, wireless security, Bluetooth, mobile networks |
| Network security | firewall types, IDS and IPS, ACLs, zero trust |
| Traffic and availability | QoS, traffic shaping, high availability (HSRP, VRRP), load balancing and failover |
| Cloud networking | virtual networks, cloud routing and VPN, security groups on AWS, Azure and GCP |
| Automation and observability | Python for networking, APIs, Ansible, Terraform, Wireshark, Nmap, SNMP, Prometheus and Grafana |
| Certifications | CCNA, CCNP, CompTIA Network+ and Security+ |
