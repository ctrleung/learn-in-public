"""Build an Anki .apkg from a card JSON file, in the learner's concept-card style.

Usage: python3 build.py networking-lesson-1.json   (needs: pip install genanki)

The note type (fields, template, CSS) comes from note-type.json, copied exactly from the
learner's own concept-card deck so cards look the same and Anki recognizes the note type.
"""
import json, sys, zlib, os
import genanki

here = os.path.dirname(os.path.abspath(__file__))
nt = json.load(open(os.path.join(here, "note-type.json")))
model = genanki.Model(
    nt["model_id"], nt["name"],
    fields=[{"name": f} for f in nt["fields"]],
    templates=[{"name": nt["template_name"], "qfmt": nt["qfmt"], "afmt": nt["afmt"]}],
    css=nt["css"])

path = sys.argv[1]
spec = json.load(open(path))
deck = genanki.Deck(1795300000000 + zlib.crc32(spec["deck"].encode()) % 1000000, spec["deck"])
for c in spec["cards"]:
    deck.add_note(genanki.Note(
        model=model, guid=genanki.guid_for(spec["deck"], c["question"]),
        fields=[c["question"], c["answer"], c.get("code", ""), c.get("category", ""), c["topic"]]))
out = os.path.splitext(path)[0] + ".apkg"
genanki.Package(deck).write_to_file(out)
print("wrote", out, "with", len(spec["cards"]), "notes")
