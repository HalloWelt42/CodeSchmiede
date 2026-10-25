---
schema_version: 1
id: k209-notenbuch-klasse
revision: 1
titel: 'Notenbuch: als Klasse'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 8
tags:
- kurs
- projekt
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`self.noten`, `self.eintraege` und `self.titel` entstehen in `__init__`.'
- kosten: 2
  text: '`eintragen` wird zur Methode: aus `global eintraege` wird `self.eintraege`.'
- kosten: 4
  text: '`bestes_fach` sucht in einer Schleife das Fach mit der kleinsten Note.'
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

    Bestes Fach: Deutsch

    Geladen: {''Mathe'': 2, ''Deutsch'': 1}

    '
tests_versteckt:
- input:
  - Sport
  - '3'
  - Kunst
  - x
  - Kunst
  - '2'
  - Sport
  - '1'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Übersprungen: x ist keine Zahl

    Sport überschrieben

    Einträge: 3

    Sport: 1 (sehr gut)

    Kunst: 2 (gut)

    Verschiedene Noten: [1, 2]

    Durchschnitt: 1.5

    Median: 1.5

    Urteil: sehr gut

    Sterne: *****

    Bestes Fach: Sport

    Geladen: {''Sport'': 1, ''Kunst'': 2}

    '
starter_code: "from statistics import median\n\n\ndef urteil(note):\n    if note <= 1.5:\n        return \"sehr gut\"\n  \
  \  elif note <= 2.5:\n        return \"gut\"\n    elif note <= 3.5:\n        return \"befriedigend\"\n    elif note <= 4:\n\
  \        return \"ausreichend\"\n    else:\n        return \"nicht bestanden\"\n\n\ndef sterne(note):\n    return \"*\"\
  \ * (7 - round(note))\n\n\neintraege = 0\n\n\ndef eintragen(fach, note):\n    global eintraege\n    eintraege += 1\n   \
  \ if fach in noten:\n        print(f\"{fach} überschrieben\")\n    noten[fach] = note\n\n\ndef lies_note(text):\n    try:\n\
  \        note = int(text)\n    except ValueError:\n        raise ValueError(f\"{text} ist keine Zahl\")\n    if note < 1\
  \ or note > 6:\n        raise ValueError(f\"{note} ist keine Note\")\n    return note\n\n\ndef speichern(noten, dateiname):\n\
  \    with open(dateiname, \"w\") as datei:\n        for fach, note in noten.items():\n            datei.write(f\"{fach};{note}\\\
  n\")\n\n\ndef laden(dateiname):\n    geladen = {}\n    with open(dateiname) as datei:\n        for zeile in datei:\n   \
  \         fach, note = zeile.strip().split(\";\")\n            geladen[fach] = int(note)\n    return geladen\n\n\ntitel\
  \ = \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten = {}\nwhile True:\n    fach = input()\n    if fach ==\
  \ \"ende\":\n        break\n    try:\n        eintragen(fach, lies_note(input()))\n    except ValueError as fehler:\n  \
  \      print(\"Übersprungen:\", fehler)\nprint(\"Einträge:\", eintraege)\nfor fach, note in noten.items():\n    print(f\"\
  {fach}: {note} ({urteil(note)})\")\nprint(\"Verschiedene Noten:\", sorted(set(noten.values())))\nschnitt = sum(noten.values())\
  \ / len(noten)\nprint(\"Durchschnitt:\", schnitt)\nprint(\"Median:\", median(noten.values()))\nprint(\"Urteil:\", urteil(schnitt))\n\
  print(\"Sterne:\", sterne(schnitt))\nspeichern(noten, \"notenbuch.txt\")\nprint(\"Geladen:\", laden(\"notenbuch.txt\"))\n"
---

**Kapitelprojekt Notenbuch, Stück 20, das letzte.** Dein Code aus Stück 19 steht schon da. Das Notenbuch wird selbst ein Objekt: eine Klasse `Notenbuch` mit `titel`, `noten` und `eintraege` und den Methoden `eintragen(fach, note)`, `schnitt()` und `bestes_fach()`. Die Funktion `eintragen` und der Name `eintraege` draußen fallen weg. Neu ist die Zeile `Bestes Fach:` vor dem Speichern. Bei `Mathe`, `2`, `Deutsch`, `1`, `ende`:

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
Bestes Fach: Deutsch
Geladen: {'Mathe': 2, 'Deutsch': 1}
```
