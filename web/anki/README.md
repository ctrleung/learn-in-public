# Anki cards

Decks built after lessons as importable `.apkg` files, in the learner's own card styles, taken from their existing decks. Card data lives in a JSON file next to each deck; `build.py` turns it into the package.

## Concept cards (the default for web and systems)

- **Note type:** `React Concept (Option B)`, copied exactly from the learner's own deck into `note-type.json`, so the cards look identical and Anki recognizes the note type.
- **One card per note:** Question to Answer.
- **Fields:** Question, Answer, Code (optional), Category (optional pill, such as Scenario, Mnemonic or Compare), Topic (small gray line).
- **Front:** a small uppercase "Question" label and the question in bold, centered.
- **Back:** the same, a divider, the answer, an optional code block, the Category pill and the Topic.
- **Short:** questions about 8 words (up to about 15); answers about 17 words (up to about 40), in plain sentences. One idea per card.
- **Kinds of cards:** "What is X?", "When do you use X?", "What is the difference between X and Y?", scenario questions ("You need X. What do you use?"), contrast cards ("Does X do Y? No. ..."), best-practice lists and mnemonics.
- **Organized by Topic, not tags.** Deck path: `Subject::Topic`, for example `Web::Networking`.
- Light and dark mode are handled by the CSS.

## Vocabulary cards (language decks, built when asked)

From the learner's vocabulary deck: two cards per note (term to meaning, and meaning to term), a big centered term with audio, a very short meaning with a clarifier in brackets, and a small gray "Type · Lesson N" line. Lowercase tags (`lesson1`, `vocabulary`), and a deck path like `Subject::Course unit::Lesson N`. `build.py` doesn't build these yet.

## When to make and change cards

- **Make cards after a lesson,** once I've been tested on it, in small batches (about 5 to 15 per lesson). I build them at wrap-up as `networking-lesson-N.json` (or the topic's name) and a matching `.apkg`. Don't make cards from material that hasn't been learned.
- **Control the pace in Anki,** with its new-cards-per-day setting, not by delaying the file.
- **Change a card** when it's ambiguous, wrong, or a leech (missed again and again). Rewrite it so it asks one clear thing. Review leeches and wording at each block review.
- **Retire a card** (suspend or delete) when the topic is obsolete, not because it's hard.
- **Mistakes in gaps.md** that keep coming back are good candidates for a new card.

## Adding to a deck you've already imported

- **New cards:** each lesson's file has only that lesson's new cards, with the same deck name (for example `Web::Networking`) and the same note type, so they land in the existing deck and your current cards are left alone.
- **Only import files of brand-new cards.** Each lesson's file has cards Anki has never seen, so nothing existing can be affected. This is the safe pattern.
- **Don't reimport a file you've already studied from.** Every card has a stable `id`, so a reimport matches the existing notes instead of duplicating them, but I haven't tested what Anki does to their review history and scheduling, and I'm not certain it's kept. If the import dialog offers a choice about updating existing notes, pick the one that doesn't.
- **Fix an existing card by editing it in Anki,** which leaves your progress untouched, then tell me so I mirror it in the JSON.
- **Anki is the source of truth for what you study** once you've imported; the JSON is a record. If they drift apart, say so at wrap-up.
- **Before the first import,** export your collection as a backup, and try a small file first.

## Files

- `note-type.json`: the concept-card note type (fields, template, styling)
- `networking-lesson-1.json`: 19 cards from lesson 1 (15 terms and 4 "Compare" cards); the source of truth, with each card's source
- `networking-lesson-1.apkg`: the importable deck
- `build.py`: `pip install genanki`, then `python3 build.py networking-lesson-1.json`

The note type has no Source field, so each card's source is kept in the JSON only. Rewrite a card in your own words if that helps, then update the JSON so the deck and the repo stay in step.

## Importing

Open the `.apkg` file with Anki, or use File, then Import on a computer. The note type matches the learner's existing one, so Anki should reuse it. I haven't checked the steps for the Anki mobile apps; if it's awkward on your phone, import on a computer and sync.
