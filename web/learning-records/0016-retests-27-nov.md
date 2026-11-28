# Re-tests on 27 Nov: 503, the doctype and element vs tag held; www and the styled heading need another pass

Five items and one gap, in new forms. The warm-up questions were done in the morning and the last item that evening.

## Evidence
- **500 vs 503:** correct. 500 is a generic server error, 503 means unavailable and to try again later, with a `Retry-After` header. The 503 gap is fixed (correct on 24 and 27 Nov). Moved to 7 days.
- **DNS terms (URL, hostname, domain name):** gave Domain Name System correctly this time and the whole URL and the domain name `example.com` correctly. Said `www` is the hostname (it is the subdomain; the hostname is `www.example.com`) and assumed `example.com` and `www.example.com` return the same address; corrected: they are different names with their own records, and a missing `www` record means the lookup fails (step 1). Held at 1 day.
- **The doctype (a page with no doctype looks different in two browsers):** correct with no help: quirks mode, browsers differ, CSS looks off, the fix is `<!DOCTYPE html>`, and it was originally for checking the HTML against rules. The doctype item moved to 7 days and the original-purpose item to 3 days.
- **A styled `div` that looks like a heading:** found the fix (make it a real heading) but gave "put it under a heading" as an alternative, and did not state the reason: a styled `div` is not a heading element, so screen readers leave it out of the headings list. A fair point that it is reachable under another heading, but only as a workaround. Held at 1 day.
- **Element vs tag and void elements (explained to a junior):** correct and clear. The `br` is void, `p` has content and a closing tag, an element is the tags, attributes and content, and the tags give the kind and the start and end. The element-vs-tag gap is fixed. Moved to 7 days.

## Decision
Move on for 503, the doctype and element vs tag. Another pass on `www` vs the hostname and on the styled-heading reason. No explain-back this session.

Re-test: on or after 2026-11-28 for DNS terms and the styled heading. On or after 2026-11-30 for the doctype's original purpose. On or after 2026-12-04 for 503, the doctype and element vs tag.
