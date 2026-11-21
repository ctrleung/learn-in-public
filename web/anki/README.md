# Anki cards

Decks built as topics are learned, as importable `.apkg` files, in the learner's own card styles, taken from their existing decks. Card data lives in one JSON file per topic; `build.py` turns the cards you haven't exported yet into a package.

## Concept cards (the default for web and systems)

- **Note type:** `React Concept (Option B)`, copied exactly from the learner's own deck into `note-type.json`, so the cards look identical and Anki recognizes the note type.
- **One card per note:** Question to Answer.
- **Fields:** Question, Answer, Code (optional), Category (optional pill, such as Scenario, Mnemonic or Compare), Topic (small gray line).
- **Front:** a small uppercase "Question" label and the question in bold, centered.
- **Back:** the same, a divider, the answer, an optional code block, the Category pill and the Topic.
- **Short:** questions about 8 words (up to about 15); answers about 17 words (up to about 40), in plain sentences. One idea per card.
- **Kinds of cards:** "What is X?", "When do you use X?", "What is the difference between X and Y?", scenario questions ("You need X. What do you use?"), contrast cards ("Does X do Y? No. ..."), best-practice lists and mnemonics.
- **Organized by Topic, not tags, and never by lesson.** One deck per topic, with the path `Subject::Topic`, for example `Web::Networking`.
- Light and dark mode are handled by the CSS.

## Vocabulary cards (language decks, built when asked)

From the learner's vocabulary deck: two cards per note (term to meaning, and meaning to term), a big centered term with audio, a very short meaning with a clarifier in brackets, and a small gray type line. One deck per topic, with no lesson numbers in the cards or deck names. `build.py` doesn't build these yet.

## When to make and change cards

- **Make cards when a topic has been learned,** after I've been tested on it, in small batches (about 5 to 15 cards). I add them to the topic's JSON file. Don't make cards from material that hasn't been learned. Cards never mention lessons.
- **Control the pace in Anki,** with its new-cards-per-day setting, not by delaying the file.
- **Change a card** when it's ambiguous, wrong, or a leech (missed again and again). Rewrite it so it asks one clear thing. Review leeches and wording at each block review.
- **Retire a card** (suspend or delete) when the topic is obsolete, not because it's hard.
- **Mistakes in gaps.md** that keep coming back are good candidates for a new card.

## Adding to a deck you've already imported

- **Each build contains only cards you haven't exported yet.** `exported.json` records which cards have gone into an import file, so a new file has cards Anki has never seen, and nothing existing can be affected. Files are named by topic and date, for example `networking-2026-11-21.apkg`.
- **They go into your existing deck** if the deck name matches (for example `Web::Networking`). If you rename the deck in Anki, tell me the new name.
- **Don't reimport a file you've already studied from.** Every card has a stable `id`, so a reimport matches existing notes instead of duplicating them, but I haven't tested what Anki does to their review history and scheduling, and I'm not certain it's kept.
- **Fix an existing card by editing it in Anki,** which leaves your progress untouched, then tell me so I mirror it in the JSON.
- **Marked as exported means built, not imported.** If you didn't import a file, tell me and I'll rebuild those cards with `--all`.
- **Anki is the source of truth for what you study** once you've imported; the JSON is a record. If they drift apart, say so.
- **Before the first import,** export your collection as a backup, and try a small file first.

## Files

- `note-type.json`: the concept-card note type (fields, template, styling)
- `networking.json`: the networking cards (15 terms and 4 "Compare" cards), with each card's source; the source of truth
- `exported.json`: which cards have already gone into an import file
- `networking-2026-11-21.apkg`: the first import file (19 cards)
- `build.py`: `pip install genanki`, then `python3 build.py networking.json`

The note type has no Source field, so each card's source is kept in the JSON only. Rewrite a card in your own words if that helps, then update the JSON.

## Importing

Open the `.apkg` file with Anki, or use File, then Import on a computer. The note type matches the learner's existing one, so Anki should reuse it. I haven't checked the steps for the Anki mobile apps; if it's awkward on your phone, import on a computer and sync.
