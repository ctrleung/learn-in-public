# DNS answers and caching

Notes from the 23 Nov 2026 session. Study from this, then close it and test yourself.

## URL vs hostname
`https://www.example.com/blog/post?id=3`
- `https` is the scheme (which protocol to speak).
- `www.example.com` is the hostname. Only this goes to DNS. `www` is a subdomain and part of the hostname.
- `/blog/post` is the path and `?id=3` the query. They go to the server in the HTTP request, never to DNS.

## What a DNS answer looks like
```
www.example.com.   300   IN   A      93.184.216.34
www.example.com.   300   IN   AAAA   2606:2800:220:1:248:1893:25c8:1946
```
Name, TTL (seconds the answer may be cached), class, record type, value. `A` is IPv4, `AAAA` is IPv6, `CNAME` is an alias for another name. A failed lookup returns a status such as `NXDOMAIN` (no such domain).

## TTL trade-off
- Long TTL: fewer lookups and less load, but a changed IP reaches users slowly.
- Short TTL: changes and failover arrive fast, but more lookups.
- Before a planned IP change, lower the TTL first, then raise it again afterwards.

## Cache chain
1. Browser cache.
2. OS cache (and the `hosts` file).
3. Recursive resolver, shared by many users (see below for where it lives).
4. Only if all miss: the resolver walks root, then `.com`, then the site's authoritative server, caches the answer and returns it.

Your machine asks the resolver once; the resolver does the legwork. Each cache keeps the answer only for the TTL, counted from when it last fetched it, so after an IP change the old IP can linger for up to about the TTL (not a guarantee).

## How the browser reaches the OS cache
The browser never reads the OS cache directly. It makes a function call to the operating system's resolver API, such as `getaddrinfo("www.example.com")` on Linux and macOS or `GetAddrInfo` on Windows. The same call is used by `curl`, `ping` and almost every other program. The OS then checks, in order: the `hosts` file, its own DNS cache (if it has one), and then it sends a DNS query to the configured recursive resolver. The answer comes back to the browser as a list of IPs, and the browser doesn't know which step answered. At each level the first cache with a fresh entry (in the table and within its TTL) answers, and later ones aren't asked.

Exception: some browsers skip the OS. Chrome can use its own built-in DNS client, and "secure DNS" (DNS over HTTPS) sends the query straight to a chosen resolver over HTTPS. Then the OS cache and `hosts` file may not be involved. The chain above is the classic picture, not the only one.

## What the browser's DNS cache stores
An in-memory table of hostname, IP address(es) and an **expiry time**, not a countdown. When an answer arrives the cache stores `expires_at = now + TTL` (for example 12:00:00 + 300 s = 12:05:00). On each lookup it checks `now < expires_at`: if yes, use the cached IP; if not, do a fresh lookup. An "expires in 240 s" display is just `expires_at - now`, worked out when you look. Nothing updates every second, and expired rows are often only removed when next used or in occasional sweeps. The same deadline-and-compare trick is used for session and token expiry.

## How to look at the browser's DNS cache
- Chrome: `chrome://net-internals/#dns` shows the host cache and has a "Clear host cache" button. Chrome has moved this page between versions, so it may be missing or different in yours.
- Firefox: `about:networking#dns` lists cached hostnames, addresses and remaining time.
- Safari: no page of its own; it relies on the OS cache.

## The OS DNS cache
The same idea as the browser's table (hostname, record type, IP, expiry), but a system service holds it and every app on the machine shares it. Each browser's own cache is separate from it. Before asking DNS at all, the OS checks the `hosts` file (`IP hostname` per line), which is how a developer points `myapp.local` at their own machine.
- Windows (DNS Client service): `ipconfig /displaydns` lists entries (record name, type, time to live, value); `ipconfig /flushdns` clears it.
- macOS (`mDNSResponder`): no simple way to list it. Flush with `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`.
- Linux: often no system-wide cache by default. With `systemd-resolved`, `resolvectl statistics` shows cache hits and `resolvectl flush-caches` clears it; otherwise a local service such as `dnsmasq` or `nscd` may do it.

A Windows entry looks roughly like this (Time To Live is the remaining time, worked out from a stored expiry):
```
Record Name . . . : www.example.com
Record Type . . . : 1          (1 = A)
Time To Live  . . : 240
A (Host) Record . : 93.184.216.34
```

## Where the recursive resolver lives
It is just a server that does lookups on your behalf. Which one you use depends on how your device is configured:
- Your ISP's resolver: the default on most home and mobile networks (the router passes its address to your devices).
- A public resolver you chose: 1.1.1.1 (Cloudflare), 8.8.8.8 (Google), 9.9.9.9 (Quad9).
- Your router: many home routers run a small forwarding cache that forwards to the ISP or a public resolver.
- A company or school resolver: also resolves internal names such as `intranet.corp`.
- Your own machine: a local resolver such as `systemd-resolved`, `dnsmasq` or `unbound`.

The role is the same everywhere: a shared cache that walks the DNS hierarchy on a miss.

### How to see which resolver you use
- Windows: `ipconfig /all`, look for "DNS Servers".
- macOS: `scutil --dns`, or System Settings, Network, your connection, Details, DNS.
- Linux: `resolvectl status`, or `cat /etc/resolv.conf` (it may show a local address such as 127.0.0.53, meaning a local resolver that forwards on; `resolvectl status` shows the real upstream servers).
- Any system: `dig example.com` prints `SERVER:` near the bottom, the resolver that answered.

## One site, many IPs
One server's IP, a load balancer's IP, several IPs rotated round-robin, different IPs by location (CDNs), or both IPv4 and IPv6.
