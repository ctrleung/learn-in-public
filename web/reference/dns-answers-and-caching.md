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
3. Recursive resolver (ISP or 1.1.1.1, 8.8.8.8), shared by many users.
4. Only if all miss: the resolver walks root, then `.com`, then the site's authoritative server, caches the answer and returns it.

Your machine asks the resolver once; the resolver does the legwork. Each cache keeps the answer only for the TTL, counted from when it last fetched it, so after an IP change the old IP can linger for up to about the TTL (not a guarantee).

## What the browser's DNS cache stores
An in-memory table of hostname, IP address(es) and an **expiry time**, not a countdown. When an answer arrives the cache stores `expires_at = now + TTL` (for example 12:00:00 + 300 s = 12:05:00). On each lookup it checks `now < expires_at`: if yes, use the cached IP; if not, do a fresh lookup. An "expires in 240 s" display is just `expires_at - now`, worked out when you look. Nothing updates every second, and expired rows are often only removed when next used or in occasional sweeps. The same deadline-and-compare trick is used for session and token expiry.

## One site, many IPs
One server's IP, a load balancer's IP, several IPs rotated round-robin, different IPs by location (CDNs), or both IPv4 and IPv6.
