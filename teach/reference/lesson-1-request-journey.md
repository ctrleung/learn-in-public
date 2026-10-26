# The request journey

Quick-reference notes from networking lesson 1. Every claim comes from [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) or [HPBN](https://hpbn.co/transport-layer-security-tls/). See also the [glossary](glossary.html) and the [lesson](../lessons/0001-follow-a-request.html).

## The four steps

1. **Address lookup.** The browser asks DNS for the IP address of the server the site lives on. It needs this *before* it can retrieve the site.
2. **Request.** The browser sends an HTTP request asking for a copy of the site. All data between client and server travels over TCP/IP.
3. **Response.** If the server approves, it replies `200 OK` and sends the site's files as small chunks called *packets*.
4. **Assembly.** The browser puts the chunks together into the page.

## Where each step fails

| Symptom | Step |
|---|---|
| Can't find the site at all | 1. Address lookup (DNS) |
| Data lost or corrupted on the way | 2-3. TCP/IP transport (the client re-requests the missing packets) |
| Error code (403, 404, 503...) | 3. Response (the server answered, but not with the page) |

## Status codes

| Code | Means |
|---|---|
| `200` | Success |
| `301` | Permanently moved; the new location is in the response |
| `400` | Server can't process the request (malformed or has errors) |
| `403` | Server won't give access: it knows who you are, but you lack permission |
| `404` | Can't find the resource (wrong URL, or deleted without a redirect) |
| `503` | Server can't handle the request right now, usually temporary (e.g. maintenance) |

> **Mix-ups to watch:** 301 is not "unauthorized" and 503 is not "internal server error". Those are different codes (401 and 500), which the MDN page names but doesn't define. Look them up in MDN's HTTP status reference.

## Packets

Data is sent in small chunks. Each packet has:

- a **header**: client and server IP addresses, packet number, total packets, protocol details
- a **payload**: the actual data

**Why chunks:**

1. Dropped or corrupted packets can be re-requested on their own instead of the whole file.
2. Packets can take different routes and arrive out of order. The header numbers let the client reassemble them.

## Parts of a URL

```text
https://developer.mozilla.org/en-US/
 |        |         |           |
 |        |         |           path: where the resource is on the server
 |        |         domain name (mozilla.org)
 |        subdomain (developer)
 protocol
```

## TCP/IP vs HTTP

- **TCP/IP** defines how data travels across the internet (the road and the vehicle).
- **HTTP** is the application protocol: the language client and server use to talk (the order you place at the shop).
- **DNS** is the address book that turns a domain name into an IP address.

## TLS: three services, three attacks

| Service | What it does | Attack it answers |
|---|---|---|
| Encryption | Obfuscates what is sent between hosts | Reading the traffic |
| Authentication | Lets the browser verify the server is who it claims to be | Impersonating a site (spoofing its name or IP address) |
| Integrity | Detects tampering and forgery, using a message authentication code on each message | Changing the traffic |

MDN: HTTPS is a secure version of HTTP that stops bad people from reading your data while it is being transported.

## Try it

```sh
curl -sI https://developer.mozilla.org/en-US/
curl -sI https://developer.mozilla.org/en-US/no-such-page-xyz
```

`-I` asks for headers only. Expect `HTTP/2 200` for the first and `404` for the second.

## Sources

- [MDN, How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
- [HPBN, Transport Layer Security (TLS)](https://hpbn.co/transport-layer-security-tls/)
