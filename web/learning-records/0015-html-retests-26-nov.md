# HTML re-tests on 26 Nov: nesting, the body and void elements held, the doctype's history needed a new explanation

Later on 26 Nov, after the warm-up, the learner continued with the three HTML items from the Basic HTML syntax reading, in new forms.

## Evidence
- **The doctype's original purpose:** missed for the second day. Said it was originally made to turn on standards mode, and that it is a historical artifact because browsers are mostly in standards mode already. Corrected with a different explanation (a timeline, then two examples): the doctype first named the rules for an HTML version, which a validator used to check the page (an HTML 4.01 Strict page with a `<font>` element fails; the Transitional doctype allows it); browsers then used it to choose standards or quirks mode; HTML5 shortened it to `<!DOCTYPE html>`. After that: a missing doctype means quirks mode, and it was originally for checking the HTML against the rules it names. Asked good follow-ups (how a validator uses it; what "modern rules and old behaviour" mean, with the box-model sizing example). Held at 1 day.
- **Correct nesting:** fixed `<ul><li>Item <em>one</li></em></ul>` and stated the rule: a child closes before its parent. First said the browser takes the first closing tag; corrected: it repairs the markup by guessing, with no error. Correct, moved to 3 days.
- **The `body` and void elements:** correct. `br`, `img`, `hr` and `input` are void: no content, no closing tag, and their attributes supply the data. `<title>` and `<meta charset>` go in the head, the `<h1>` and text in the body. Moved to 3 days.

## Decision
Correct the doctype's history again tomorrow, in a new form, and note what worked: a timeline plus a concrete example. The other two held. No explain-back this session.

Re-test: on or after 2026-11-27 for the doctype's original purpose. On or after 2026-11-29 for nesting and the `body` and void elements.
