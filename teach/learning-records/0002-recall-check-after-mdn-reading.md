# Recall check after the MDN reading: strong on the model, mixed up some status codes

After reading MDN's "How the web works", the learner answered six written recall questions from memory. They explained DNS, packets (header and payload, re-requesting lost pieces), URL parts and TCP/IP vs HTTP correctly, and gave the journey in order but left out the 200 OK / packets step and the browser assembling the page. They mixed up two status codes: 301 as "unauthorized" (it means permanently moved; unauthorized is a different code, 401) and 503 as "internal server error" (503 means the server can't handle the request right now, usually temporary). They also flagged their own uncertainty on the status codes, which is good calibration.

## Evidence
- Written free recall on six questions, same day as the reading, no looking back.
- Added unprompted that the browser and operating system may cache DNS answers before asking a DNS server. This matches the zine's description of caching by recursive DNS servers, but the browser-then-OS order is not covered by any source read so far; verify before teaching it as fact.

## Implications
- Re-test status codes (301 vs 401, 503 vs 500) after a few days; this is the one misconception to watch.
- Ready for a deeper DNS lesson. DNS caching, TTL and attacks on DNS are a natural next step.
