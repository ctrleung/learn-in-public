# Anki cards

Importable decks for terms, built after lessons in the learner's card style, as `.apkg` files. Card data lives in a JSON file next to each deck; `build.py` turns it into the package.

## Card style (follow this for every deck)

Modeled on the learner's existing vocabulary deck.

- **Two cards per note:** Term to Meaning (recognition) and Meaning to Term (production).
- **Fields:** Term, Meaning, Type, Lesson, Source. The Source field isn't shown on the card.
- **Front:** one big centered item (40px for the term, 28px for a meaning).
- **Back:** the same front, a divider, then the answer (28px or 40px), and a small gray line reading "Type · Lesson N".
- **Meanings are very short:** a few words, with a clarifier in brackets if needed, like "I, me (formal)". No long definitions.
- **One simple fact per card.**
- **Tags:** lowercase, `lesson1` and `vocabulary`.
- **Deck path:** `Subject::Course or topic::Lesson N`, for example `Web::Networking Vocabulary::Lesson 1`.
- **Note type:** `Tech Terms+`, with a fixed id so every deck shares it.

## Files

- `networking-terms.json`: the 15 networking terms from lesson 1 (source of truth)
- `networking-terms.apkg`: the importable deck (30 cards)
- `build.py`: `pip install genanki`, then `python3 build.py networking-terms.json`

Rewrite a card in your own words if that helps you remember it, then update the JSON so the deck and the repo stay in step.

## Importing

Open the `.apkg` file with Anki, or use File, then Import on a computer. I haven't checked the steps for the Anki mobile apps; if it's awkward on your phone, import on a computer and sync.
