#!/usr/bin/env python3
"""Build the data file for the Mastery Map artifact.

Reads web/TOPICS.md (HTML topics), web/reviews.md and web/gaps.md, groups the
review items by topic, and writes topics.json: one row per topic with a status.

Usage:  python3 -I scripts/mastery_map.py [output.json]     (default: topics.json)

Status of a topic = its weakest review item:
  none      no review items yet
  work      a gap with no correct answer yet
  learning  weakest item at 1 or 3 days
  solid     weakest item at 7 or 14 days
  master    every item at 30 days or more

Then upload topics.json to the Mastery Map artifact and point its `topics`
dataset at the new file (see CLAUDE.md, "Run the session", step 5).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = sys.argv[1] if len(sys.argv) > 1 else "topics.json"

STAGES = ("1", "3", "7", "14", "30", "M")
STAGE_NAME = {"1": "1 day", "3": "3 days", "7": "7 days", "14": "14 days", "30": "30 days", "M": "Mastered"}
STATUS_LABEL = {"none": "Not started", "work": "Needs work", "learning": "Learning",
                "solid": "Getting solid", "master": "Mastered"}


def table_rows(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        if line.startswith("|") and not line.startswith(("|---", "| Item", "| Date", "| #")):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


# Subjects and their topics. HTML comes from web/TOPICS.md; the rest are first
# guesses from web/PLAN.md until their lists are polished.
def topics_from_md(path):
    """Topics per subject from web/TOPICS.md: a '## Subject' heading, then a table with a numbered first column."""
    found, subject = {}, None
    for line in Path(path).read_text().splitlines():
        if line.startswith("## "):
            subject = re.sub(r"\s*\(.*\)\s*$", "", line[3:]).strip()
        elif line.startswith("|") and subject:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) > 1 and cells[0].isdigit():
                found.setdefault(subject, []).append(cells[1])
    return found


FROM_MD = topics_from_md(ROOT / "web/TOPICS.md")
SUBJECTS = {
    "HTML": FROM_MD.get("HTML", []),
    "CSS": FROM_MD.get("CSS", ["Selectors", "Cascade and specificity", "Inheritance", "Box model",
                               "Sizing and overflow", "Flexbox", "Grid", "Positioning",
                               "Responsive design and media queries", "Values and units", "Typography"]),
    "JavaScript": FROM_MD.get("JavaScript", ["Fundamentals", "The DOM", "Events and bubbling", "Promises",
                                             "fetch and JSON", "Error handling", "Browser storage"]),
    "React": FROM_MD.get("React", ["Getting started", "Components", "State", "Events",
                                   "Conditional rendering and filtering", "React accessibility"]),
    "Networking and HTTP": ["The request journey", "DNS", "TLS", "Status codes", "Headers and caching",
                            "Cookies", "CORS", "HTTP/2, HTTPS and HSTS"],
}

# (keyword in the review item, subject, start of the topic name). First match wins.
# An item that matches nothing is left out; add a rule when you add a new kind of item.
RULES = [
    ("steps of a request", "Networking and HTTP", "The request journey"),
    ("roles of", "Networking and HTTP", "The request journey"),
    ("503", "Networking and HTTP", "Status codes"),
    ("301", "Networking and HTTP", "Status codes"),
    ("tls", "Networking and HTTP", "TLS"),
    ("integrity", "Networking and HTTP", "TLS"),
    ("dns", "Networking and HTTP", "DNS"),
    ("address lookup", "Networking and HTTP", "DNS"),
    ("hostname", "Networking and HTTP", "DNS"),
    ("cache", "Networking and HTTP", "DNS"),
    ("ip change", "Networking and HTTP", "DNS"),
    ("element vs tag", "HTML", "Element anatomy"),
    ("doctype", "HTML", "Document structure"),
    ("`<html>`", "HTML", "Document structure"),
    ("heading", "HTML", "Headings and paragraphs"),
]

# (keyword in the review item, text that appears in the matching gaps.md row)
GAP_LINKS = [
    ("503", "503"), ("dns terms", "domain name service"), ("integrity", "integrity"),
    ("element vs tag", "element vs tag"), ("doctype", "doctype"),
    ("`<html>`", "lang"), ("heading levels", "heading level"),
]


def stage_key(text):
    m = re.match(r"(\d+)\s*day", text)
    if "mastered" in text.lower() and not m:
        return "M"
    return m.group(1) if m and m.group(1) in STAGES else "1"


gap_rows = [r for r in table_rows(ROOT / "web/gaps.md") if len(r) > 3 and r[3].lower().startswith("open")]
open_gaps = " ".join(r[2].lower() + " " + r[3].lower() for r in gap_rows)
fresh_gaps = " ".join(r[2].lower() + " " + r[3].lower() for r in gap_rows if "correct" not in r[3].lower())

bucket = {}
for r in table_rows(ROOT / "web/reviews.md"):
    name, _src, stage, last = (r + [""] * 4)[:4]
    low = name.lower()
    hit = next(((s, t) for k, s, t in RULES if k in low), None)
    if not hit:
        continue
    subject, start = hit
    topic = next((t for t in SUBJECTS[subject] if t.startswith(start)), None)
    if not topic:
        continue
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", last)
    bucket.setdefault((subject, topic), []).append({
        "stage": stage_key(stage),
        "gap": any(k in low and g in open_gaps for k, g in GAP_LINKS),
        "fresh": any(k in low and g in fresh_gaps for k, g in GAP_LINKS),
        "last": max(dates) if dates else "",
    })


def status(items):
    if not items:
        return "none"
    if any(i["fresh"] for i in items):
        return "work"
    low = min(STAGES.index(i["stage"]) for i in items)
    return "learning" if low <= 1 else "solid" if low <= 3 else "master"


rows = []
for subject, topics in SUBJECTS.items():
    for topic in topics:
        items = bucket.get((subject, topic), [])
        st = status(items)
        weakest = STAGE_NAME[STAGES[min(STAGES.index(i["stage"]) for i in items)]] if items else ""
        rows.append({
            "subject": subject, "topic": topic, "status": st, "status_label": STATUS_LABEL[st],
            "items": len(items), "open_gaps": sum(1 for i in items if i["gap"]),
            "weakest_item_stage": weakest,
            "last_tested": max([i["last"] for i in items if i["last"]] or [""]),
        })

Path(OUT).write_text(json.dumps(rows, indent=1))
print(f"{len(rows)} topics written to {OUT}")
