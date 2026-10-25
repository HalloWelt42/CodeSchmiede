---
schema_version: 1
id: k139-notenbuch-faecher
revision: 1
titel: 'Notenbuch: Noten je Fach'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- projekt
- woerterbuch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`noten = {}` und in der Schleife `noten[fach] = int(input())`.'
- kosten: 2
  text: Durchschnitt aus `sum(noten.values()) / len(noten)`.
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - Musik
  - '3'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Mathe: 2

    Deutsch: 1

    Musik: 3

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - Sport
  - '1'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Sport: 1

    Durchschnitt: 1.0

    Urteil: sehr gut

    Sterne: ******

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nnoten = []\nwhile True:\n    note = int(input())\n    if note == 0:\n        break\n    noten.append(note)\n\
  schnitt = sum(noten) / len(noten)\nfor nr, note in enumerate(noten, 1):\n    print(f\"Note {nr}: {note}\")\nprint(\"Beste:\"\
  , min(noten), \"Schlechteste:\", max(noten))\nprint(\"Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n    print(\"Urteil:\
  \ sehr gut\")\nelif schnitt <= 2.5:\n    print(\"Urteil: gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil: befriedigend\"\
  )\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\")\nelse:\n    print(\"Urteil: nicht bestanden\")\nprint(\"Sterne:\
  \ \", end=\"\")\nfor i in range(7 - round(schnitt)):\n    print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 13.** Dein Code aus Stück 12 steht schon da. Das Notenbuch merkt sich die Noten jetzt je Fach in einem Wörterbuch: abwechselnd Fach und Note, bis als Fach `ende` kommt. Die feste Fächerzeile und Beste/Schlechteste fallen weg. Bei `Mathe`, `2`, `Deutsch`, `1`, `Musik`, `3`, `ende`:

```
=== MEIN NOTENBUCH ===
Mathe: 2
Deutsch: 1
Musik: 3
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
