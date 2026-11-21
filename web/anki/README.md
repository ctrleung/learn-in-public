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

## Files

- `note-type.json`: the concept-card note type (fields, template, styling)
- `networking-lesson-1.json`: 19 cards from lesson 1 (15 terms and 4 "Compare" cards); the source of truth, with each card's source
- `networking-lesson-1.apkg`: the importable deck
- `build.py`: `pip install genanki`, then `python3 build.py networking-lesson-1.json`

The note type has no Source field, so each card's source is kept in the JSON only. Rewrite a card in your own words if that helps, then update the JSON so the deck and the repo stay in step.

## Importing

Open the `.apkg` file with Anki, or use File, then Import on a computer. The note type matches the learner's existing one, so Anki should reuse it. I haven't checked the steps for the Anki mobile apps; if it's awkward on your phone, import on a computer and sync.
