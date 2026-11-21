# 12-week plan: web fundamentals (23 Nov 2026 to 14 Feb 2027)

This is a guide, not a contract. It adjusts to how I'm doing: when `gaps.md` shows a topic needs more time, that block grows and a later one shrinks, and the change is recorded in "Schedule changes" at the bottom. Main resource: MDN (section links are in [RESOURCES.md](RESOURCES.md)).

## How each session works

1. **Warm-up:** 3 or 4 typed questions from re-tests that are due and open items in `gaps.md`.
2. **Quiz first:** questions on the new topic come before any explanation. A miss goes into `gaps.md`.
3. **Make me produce it:** hints and narrower questions before answers. I fix gaps in my own words.
4. **Then explain,** from MDN, and go deep on a few things instead of skimming many.
5. **Explain it back,** then the learning record, with a Re-test date.
6. Sessions are 10 to 20 minutes. Hand-coded practice goes in `practice/` (no AI).

The first week of each block is a **diagnostic**: a typed quiz across the block, used to find the real gaps and set the pace.

## Blocks and weeks

| Week | Dates | Block | Focus |
|---|---|---|---|
| 1 | 23 to 29 Nov | HTML and accessibility | Diagnostic. Document structure, headings, text semantics, links, images, metadata |
| 2 | 30 Nov to 6 Dec | HTML and accessibility | Forms and tables, done accessibly; form validation |
| 3 | 7 to 13 Dec | HTML and accessibility | What accessibility is, HTML and accessibility, WAI-ARIA basics, keyboard and focus, tooling; block review |
| 4 | 14 to 20 Dec | CSS | Diagnostic. Selectors, cascade, specificity, inheritance, box model, sizing, overflow |
| 5 | 21 to 27 Dec | CSS | Layout: flexbox, grid, positioning (lighter week, holidays) |
| 6 | 28 Dec to 3 Jan | CSS | Responsive design, media queries, values and units, typography, CSS and accessibility; block review (lighter week) |
| 7 | 4 to 10 Jan | Browser, HTTP, JavaScript | Diagnostic. How browsers load websites; JavaScript fundamentals gaps |
| 8 | 11 to 17 Jan | Browser, HTTP, JavaScript | DOM, events, event bubbling; promises, `fetch`, JSON, error handling |
| 9 | 18 to 24 Jan | Browser, HTTP, JavaScript | HTTP in the browser: headers, caching, cookies, CORS, methods, HTTP/2, HTTPS and HSTS; browser storage; developer tools; block review |
| 10 | 25 to 31 Jan | React | Diagnostic. Getting started, components, main features |
| 11 | 1 to 7 Feb | React | State, events, conditional rendering and filtering |
| 12 | 8 to 14 Feb | React | React accessibility, a small hand-built project, review of the whole plan against `gaps.md` |

## Hand-coded practice (in `practice/`, no AI)

- **After HTML and accessibility:** an accessible page with landmarks, a form with validation and a data table, checked with the keyboard and tooling.
- **After CSS:** the same page rebuilt as a responsive layout with flexbox and grid.
- **After browser, HTTP and JS:** a small page that fetches JSON and renders it with the DOM and events, with loading and error states, watched in the browser's developer tools.
- **After React:** a small filterable list in React, accessible.

## Networking, only as support

DNS, HTTP, TLS basics and how a page loads stay in scope, mainly in weeks 7 and 9. The earlier networking records (0001 to 0003) keep their re-tests in the warm-ups. Security stays as a light browser-side thread (XSS, CORS, CSP, cookies, HSTS): when a topic raises "how is this attacked?", ask it once.

## Systems thread

Scaling, networking, containers and system design have their own short weekend sessions in [`../systems/`](../systems/), starting after week 1. Where a web topic overlaps, ask one "what changes at scale?" question and leave the depth for that session. Examples: how a page loads and DNS in week 7, caching, cookies and sessions in week 9.

## Parked

AWS, Linux, backend and databases, DevOps and operations are parked in [`../systems/PARKING-LOT.md`](../systems/PARKING-LOT.md). I work on them only when I ask.

## Schedule changes

| Date | Change | Reason |
|---|---|---|
