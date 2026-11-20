# Exercises

Hands-on things to try later. Tick them off as you go. Each one runs on **your own computer** and is based on a source you've already read. Only capture or probe your own devices and networks. These are the networking exercises that support the browser and HTTP part of the plan. Hand-coded web exercises for the 12-week plan go in [`../practice/`](../practice/) (no AI). Parked exercises are in [PARKING-LOT.md](PARKING-LOT.md).

Source key: [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) · [Zine](https://wizardzines.com/zines/networking/) (free, "Networking! ACK!") · [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

## The request journey

- [ ] **See a status code.** Run `curl -sI https://developer.mozilla.org/en-US/` then `curl -sI https://developer.mozilla.org/en-US/no-such-page-xyz`.
  Notice: `HTTP/2 200` for the first and `404` for the second. Which step of the journey does the code come from? *(MDN)*
- [ ] **Make an HTTP request by hand.** Run `printf "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc example.com 80` (all on one line).
  Notice: the response is plain text, with a status line, headers, then the page. *(Zine, HTTP page)*
- [ ] **Look up a DNS name.** Run `dig jvns.ca`, then `dig @8.8.8.8 jvns.ca`, then `dig +trace jvns.ca`.
  Notice: the number after the name is the TTL (how long the answer may be cached); `+trace` shows the root, `.ca` and site name servers answering in turn. *(Zine, DNS pages)*

## Packets and TLS

- [ ] **Capture your own traffic, plain HTTP.** Run `sudo tcpdump port 80 -w http.pcap`, load an `http://` site in your browser, press Ctrl+C, then open `http.pcap` in Wireshark.
  Notice: the SYN / SYN-ACK / ACK handshake, the `GET` request and its headers, readable. Try the filter `frame contains "GET"`. Many sites now redirect to `https`; if you see no readable requests, that's why. *(Zine, Wireshark page)*
- [ ] **Capture your own traffic, HTTPS.** Same as above but with `port 443`, visiting an `https://` site.
  Notice: you still see addresses, ports and the handshake, but the contents are scrambled. Compare with the plain HTTP capture. *(Zine, TLS page; HPBN, "a third-party observer can only infer...")*
- [ ] **Read a certificate.** Run `openssl s_client -connect jvns.ca:443 -servername jvns.ca`.
  Notice: the server's certificate details, and which TLS version was negotiated. *(Zine, TLS page)*
