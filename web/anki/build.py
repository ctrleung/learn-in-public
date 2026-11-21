"""Build an Anki .apkg from a card JSON file, in the learner's card style.

Usage: python3 build.py networking-terms.json   (needs: pip install genanki)
"""
import json, sys, zlib, os
import genanki

MODEL_ID = 1795300000001          # fixed so every deck shares one note type
model = genanki.Model(
    MODEL_ID, "Tech Terms+",
    fields=[{"name": "Term"}, {"name": "Meaning"}, {"name": "Type"}, {"name": "Lesson"}, {"name": "Source"}],
    templates=[
        {"name": "Term -> Meaning",
         "qfmt": '<div style="font-size: 40px; text-align: center;">{{Term}}</div>',
         "afmt": '{{FrontSide}}<hr id="answer"><div style="font-size: 28px; text-align: center;">{{Meaning}}</div>'
                 '<div style="text-align: center; color: #888; font-size: 14px;">{{Type}} &middot; Lesson {{Lesson}}</div>'},
        {"name": "Meaning -> Term",
         "qfmt": '<div style="font-size: 28px; text-align: center;">{{Meaning}}</div>',
         "afmt": '{{FrontSide}}<hr id="answer"><div style="font-size: 40px; text-align: center;">{{Term}}</div>'
                 '<div style="text-align: center; color: #888; font-size: 14px;">{{Type}} &middot; Lesson {{Lesson}}</div>'},
    ])

path = sys.argv[1]
spec = json.load(open(path))
deck = genanki.Deck(1795300000000 + zlib.crc32(spec["deck"].encode()) % 1000000, spec["deck"])
tags = ["lesson" + spec["lesson"], spec["type"].lower()]
for c in spec["cards"]:
    deck.add_note(genanki.Note(model=model, guid=genanki.guid_for(spec["deck"], c["term"]),
                               fields=[c["term"], c["meaning"], spec["type"], spec["lesson"], c["source"]], tags=tags))
out = os.path.splitext(path)[0] + ".apkg"
genanki.Package(deck).write_to_file(out)
print("wrote", out, "with", len(spec["cards"]), "notes")
