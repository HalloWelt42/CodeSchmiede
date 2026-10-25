---
schema_version: 1
id: k199-notenbuch-speichern
revision: 1
titel: 'Notenbuch: speichern und laden'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- projekt
- datei
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`speichern` öffnet mit `"w"` und schreibt `f"{fach};{note}\n"`.'
- kosten: 2
  text: '`laden` zerlegt jede Zeile mit `split(";")` und trägt `int(note)` ein.'
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Einträge: 2

    Mathe: 2 (gut)

    Deutsch: 1 (sehr gut)

    Verschiedene Noten: [1, 2]

    Durchschnitt: 1.5

    Median: 1.5

    Urteil: sehr gut

    Sterne: *****

    Geladen: {''Mathe'': 2, ''Deutsch'': 1}

    '
tests_versteckt:
- input:
  - Sport
  - '3'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Einträge: 1

    Sport: 3 (befriedigend)

    Verschiedene Noten: [3]

    Durchschnitt: 3.0

    Median: 3

    Urteil: befriedigend

    Sterne: ****

    Geladen: {''Sport'': 3}

    '
starter_code: "from statistics import median\n\n\ndef urteil(note):\n    if note <= 1.5:\n        return \"sehr gut\"\n  \
  \  elif note <= 2.5:\n        return \"gut\"\n    elif note <= 3.5:\n        return \"befriedigend\"\n    elif note <= 4:\n\
  \        return \"ausreichend\"\n    else:\n        return \"nicht bestanden\"\n\n\ndef sterne(note):\n    return \"*\"\
  \ * (7 - round(note))\n\n\neintraege = 0\n\n\ndef eintragen(fach, note):\n    global eintraege\n    eintraege += 1\n   \
  \ if fach in noten:\n        print(f\"{fach} überschrieben\")\n    noten[fach] = note\n\n\ndef lies_note(text):\n    try:\n\
  \        note = int(text)\n    except ValueError:\n        raise ValueError(f\"{text} ist keine Zahl\")\n    if note < 1\
  \ or note > 6:\n        raise ValueError(f\"{note} ist keine Note\")\n    return note\n\n\ntitel = \"Mein Notenbuch\"\n\
  print(f\"=== {titel.upper()} ===\")\nnoten = {}\nwhile True:\n    fach = input()\n    if fach == \"ende\":\n        break\n\
  \    try:\n        eintragen(fach, lies_note(input()))\n    except ValueError as fehler:\n        print(\"Übersprungen:\"\
  , fehler)\nprint(\"Einträge:\", eintraege)\nfor fach, note in noten.items():\n    print(f\"{fach}: {note} ({urteil(note)})\"\
  )\nprint(\"Verschiedene Noten:\", sorted(set(noten.values())))\nschnitt = sum(noten.values()) / len(noten)\nprint(\"Durchschnitt:\"\
  , schnitt)\nprint(\"Median:\", median(noten.values()))\nprint(\"Urteil:\", urteil(schnitt))\nprint(\"Sterne:\", sterne(schnitt))\n"
---

**Kapitelprojekt Notenbuch, Stück 19.** Dein Code aus Stück 18 steht schon da. Das Notenbuch merkt sich die Noten jetzt in einer Datei: `speichern(noten, dateiname)` schreibt je Fach eine Zeile `Fach;Note`, `laden(dateiname)` liest sie wieder als Wörterbuch. Ganz am Ende wird in `notenbuch.txt` gespeichert, wieder geladen und das Geladene ausgegeben. Bei `Mathe`, `2`, `Deutsch`, `1`, `ende`:

```
=== MEIN NOTENBUCH ===
Einträge: 2
Mathe: 2 (gut)
Deutsch: 1 (sehr gut)
Verschiedene Noten: [1, 2]
Durchschnitt: 1.5
Median: 1.5
Urteil: sehr gut
Sterne: *****
Geladen: {'Mathe': 2, 'Deutsch': 1}
```
