#!/usr/bin/env python3
"""Build the data file for the Mastery Map artifact.

Reads the topic lists (web/TOPICS.md and networking/TOPICS.md), the review queue
(web/reviews.md) and the gaps list (web/gaps.md), and writes topics.json: one row
per topic with a status.

Every row in reviews.md and gaps.md has a Topic column, written "Subject: Topic"
exactly as in the topic lists, for example "Networking: DNS and name resolution".
A row with a missing or unknown topic is reported as a warning and left out.

Usage:  python3 -I scripts/mastery_map.py [output.json]     (default: topics.json)

Status of a topic = its weakest review item:
  none      no review items yet
  work      an open gap with no correct answer yet
  learning  weakest item at 1 or 3 days
  solid     weakest item at 7 or 14 days
  master    every item at 30 days or more

Sections whose heading says "optional" are not tracked.

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
SUBJECT_ORDER = ["HTML", "CSS", "JavaScript", "React", "HTTP and the web", "Networking"]
warnings = []


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def read_table(path):
    """Rows of the first markdown table in a file, as dicts keyed by the header cells."""
    lines = Path(path).read_text().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].startswith("|---"):
            header = cells(line)
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                c = cells(row)
                rows.append(dict(zip(header, c + [""] * (len(header) - len(c)))))
            return rows
    return []


def topics_from_md(path):
    """Topics per subject: a '## Subject' heading, then a table with a numbered first column.
    Sections marked optional are not tracked."""
    found, subject = {}, None
    for line in Path(path).read_text().splitlines():
        if line.startswith("## "):
            subject = None if "optional" in line else re.sub(r"\s*\(.*\)\s*$", "", line[3:]).strip()
        elif line.startswith("|") and subject:
            c = cells(line)
            if len(c) > 1 and c[0].isdigit():
                found.setdefault(subject, []).append(c[1])
    return found


FROM_MD = {**topics_from_md(ROOT / "web/TOPICS.md"), **topics_from_md(ROOT / "networking/TOPICS.md")}
SUBJECTS = {s: FROM_MD.get(s, []) for s in SUBJECT_ORDER}


def resolve(topic_cell, where):
    """'Subject: Topic' -> (subject, topic), or None with a warning."""
    if ": " not in topic_cell:
        warnings.append(f"{where}: missing Topic (write 'Subject: Topic')")
        return None
    subject, topic = topic_cell.split(": ", 1)
    if subject not in SUBJECTS or topic not in SUBJECTS[subject]:
        warnings.append(f"{where}: unknown topic '{topic_cell}'")
        return None
    return subject, topic


def stage_key(text):
    m = re.match(r"(\d+)\s*day", text)
    if "mastered" in text.lower() and not m:
        return "M"
    return m.group(1) if m and m.group(1) in STAGES else "1"


items = {}   # (subject, topic) -> list of {stage, last}
for r in read_table(ROOT / "web/reviews.md"):
    key = resolve(r.get("Topic", ""), "reviews.md: " + r.get("Item", "")[:40])
    if not key:
        continue
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", r.get("Last result", ""))
    items.setdefault(key, []).append({"stage": stage_key(r.get("Stage", "")), "last": max(dates) if dates else ""})

gaps = {}    # (subject, topic) -> {"open": n, "fresh": n}
for r in read_table(ROOT / "web/gaps.md"):
    status_text = r.get("Status", "").lower()
    if not status_text.startswith("open"):
        continue
    key = resolve(r.get("Topic", ""), "gaps.md: " + r.get("What I missed", "")[:40])
    if not key:
        continue
    g = gaps.setdefault(key, {"open": 0, "fresh": 0})
    g["open"] += 1
    if "correct" not in status_text:
        g["fresh"] += 1


def status(key):
    its = items.get(key, [])
    if gaps.get(key, {}).get("fresh"):
        return "work"
    if not its:
        return "none"
    low = min(STAGES.index(i["stage"]) for i in its)
    return "learning" if low <= 1 else "solid" if low <= 3 else "master"


rows = []
for subject, topics in SUBJECTS.items():
    for topic in topics:
        key = (subject, topic)
        its = items.get(key, [])
        st = status(key)
        weakest = STAGE_NAME[STAGES[min(STAGES.index(i["stage"]) for i in its)]] if its else ""
        rows.append({
            "subject": subject, "topic": topic, "status": st, "status_label": STATUS_LABEL[st],
            "items": len(its), "open_gaps": gaps.get(key, {}).get("open", 0),
            "weakest_item_stage": weakest,
            "last_tested": max([i["last"] for i in its if i["last"]] or [""]),
        })

Path(OUT).write_text(json.dumps(rows, indent=1))
print(f"{len(rows)} topics written to {OUT}")
for w in warnings:
    print("WARNING:", w)
if warnings:
    print(f"{len(warnings)} warning(s): fix the Topic column, then run again.")
