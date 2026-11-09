# Exercises

Hands-on things to try later. Tick them off as you go. Each one runs on **your own computer** and is based on a source you've already read. Only capture or probe your own devices and networks.

Source key: [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) · [Zine](https://wizardzines.com/zines/networking/) (free, "Networking! ACK!") · [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

## Lesson 1: the request journey

- [ ] **See a status code.** Run `curl -sI https://developer.mozilla.org/en-US/` then `curl -sI https://developer.mozilla.org/en-US/no-such-page-xyz`.
  Notice: `HTTP/2 200` for the first and `404` for the second. Which step of the journey does the code come from? *(MDN)*
- [ ] **Make an HTTP request by hand.** Run `printf "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc example.com 80` (all on one line).
  Notice: the response is plain text, with a status line, headers, then the page. *(Zine, HTTP page)*
- [ ] **Look up a DNS name.** Run `dig jvns.ca`, then `dig @8.8.8.8 jvns.ca`, then `dig +trace jvns.ca`.
  Notice: the number after the name is the TTL (how long the answer may be cached); `+trace` shows the root, `.ca` and site name servers answering in turn. *(Zine, DNS pages)*
- [ ] **Trace the route.** Run `traceroute google.com`.
  Notice: each line is a router your packets pass through on the way. *(Zine, routing page)*
- [ ] **See who's on your local network.** Run `arp -na`.
  Notice: the table maps IP addresses on your network to hardware (MAC) addresses. *(Zine, local networking page)*

## Packets and TLS

- [ ] **Capture your own traffic, plain HTTP.** Run `sudo tcpdump port 80 -w http.pcap`, load an `http://` site in your browser, press Ctrl+C, then open `http.pcap` in Wireshark.
  Notice: the SYN / SYN-ACK / ACK handshake, the `GET` request and its headers, readable. Try the filter `frame contains "GET"`. Many sites now redirect to `https`; if you see no readable requests, that's why. *(Zine, Wireshark page)*
- [ ] **Capture your own traffic, HTTPS.** Same as above but with `port 443`, visiting an `https://` site.
  Notice: you still see addresses, ports and the handshake, but the contents are scrambled. Compare with the plain HTTP capture. *(Zine, TLS page; HPBN, "a third-party observer can only infer...")*
- [ ] **Read a certificate.** Run `openssl s_client -connect jvns.ca:443 -servername jvns.ca`.
  Notice: the server's certificate details, and which TLS version was negotiated. *(Zine, TLS page)*

## Vulnerabilities

- [ ] **Read a real advisory.** Run `curl "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"` (Log4Shell). Find the description, the severity score, and the CISA dates.
  Notice: how a single record tells you whether something is serious and being exploited. Then look at the same CVE at `cveawg.mitre.org`. *(NVD and MITRE APIs)*

## Later: needs a container or VM

- [ ] **Harden a TLS setup.** Run nginx in a container with a self-signed certificate, check which TLS versions it accepts, then change the config to allow only TLS 1.2 and 1.3 and check again. Look up the right directive name in nginx's documentation; OWASP says to default to TLS 1.3, allow 1.2 for compatibility, and disable 1.0, 1.1 and SSLv2/3. *(OWASP TLS)*
- [ ] **Generate a config.** Use Mozilla's SSL configuration generator (named in OWASP's cheat sheet) to produce an nginx config, and read what each setting does.
