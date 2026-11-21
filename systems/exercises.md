# Exercises

Hands-on exercises for the systems thread. These are the ones parked from the web fundamentals plan; new exercises are added as sessions reach them (for example running a container locally, once Docker docs are reachable). Each one runs on your own computer; only probe your own devices and networks.

- [ ] **Trace the route.** Run `traceroute google.com`.
  Notice: each line is a router your packets pass through on the way. *(Zine, routing page)*

- [ ] **See who's on your local network.** Run `arp -na`.
  Notice: the table maps IP addresses on your network to hardware (MAC) addresses. *(Zine, local networking page)*

- [ ] **Read a real advisory.** Run `curl "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"` (Log4Shell). Find the description, the severity score, and the CISA dates.
  Notice: how a single record tells you whether something is serious and being exploited. Then look at the same CVE at `cveawg.mitre.org`. *(NVD and MITRE APIs)*

- [ ] **Harden a TLS setup.** Run nginx in a container with a self-signed certificate, check which TLS versions it accepts, then change the config to allow only TLS 1.2 and 1.3 and check again. Look up the right directive name in nginx's documentation; OWASP says to default to TLS 1.3, allow 1.2 for compatibility, and disable 1.0, 1.1 and SSLv2/3. *(OWASP TLS)*

- [ ] **Generate a config.** Use Mozilla's SSL configuration generator (named in OWASP's cheat sheet) to produce an nginx config, and read what each setting does.
