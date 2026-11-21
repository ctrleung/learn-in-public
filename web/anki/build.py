"""Build an Anki .apkg of the cards that haven't been exported yet, in the learner's concept-card style.

Usage:  python3 build.py networking.json          new cards only (the safe pattern for importing)
        python3 build.py networking.json --all    every card in the file (a fresh deck)
Needs:  pip install genanki

- Cards live in one JSON file per topic. Each card has a stable "id" that sets its Anki identity,
  so rewording a card doesn't duplicate it.
- exported.json records which ids have already gone into an import file, so each build contains
  only cards Anki hasn't seen. Nothing here refers to lessons.
- The note type (fields, template, CSS) comes from note-type.json, copied exactly from the learner's
  own concept-card deck.
"""
import json, sys, zlib, os, datetime
import genanki

here = os.path.dirname(os.path.abspath(__file__))
nt = json.load(open(os.path.join(here, "note-type.json")))
model = genanki.Model(
    nt["model_id"], nt["name"],
    fields=[{"name": f} for f in nt["fields"]],
    templates=[{"name": nt["template_name"], "qfmt": nt["qfmt"], "afmt": nt["afmt"]}],
    css=nt["css"])

path = sys.argv[1]
build_all = "--all" in sys.argv
spec = json.load(open(path))
manifest_path = os.path.join(here, "exported.json")
manifest = json.load(open(manifest_path)) if os.path.exists(manifest_path) else {}
done = set(manifest.get(spec["deck"], []))
cards = [c for c in spec["cards"] if build_all or c.get("id", c["question"]) not in done]
if not cards:
    print("no new cards for", spec["deck"]); sys.exit(0)

deck = genanki.Deck(1795300000000 + zlib.crc32(spec["deck"].encode()) % 1000000, spec["deck"])
for c in cards:
    deck.add_note(genanki.Note(
        model=model, guid=genanki.guid_for(spec["deck"], c.get("id", c["question"])),
        fields=[c["question"], c["answer"], c.get("code", ""), c.get("category", ""), c["topic"]]))
stem = os.path.splitext(os.path.basename(path))[0]
base = os.path.join(here, f"{stem}-{datetime.date.today().isoformat()}")
out, n = base + ".apkg", 1
while os.path.exists(out):          # never overwrite an earlier file from the same day
    n += 1; out = f"{base}-{n}.apkg"
genanki.Package(deck).write_to_file(out)
if not build_all:
    manifest[spec["deck"]] = sorted(done | {c.get("id", c["question"]) for c in cards})
    json.dump(manifest, open(manifest_path, "w"), indent=1, ensure_ascii=False); open(manifest_path, "a").write("\n")
print("wrote", out, "with", len(cards), "notes")
