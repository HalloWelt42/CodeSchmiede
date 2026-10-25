---
schema_version: 1
id: k129-notenbuch-nummern
revision: 1
titel: 'Notenbuch: nummerierte Noten'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- aufzaehlen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for nr, note in enumerate(noten, 1):`'
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Note 1: 2

    Note 2: 1

    Note 3: 3

    Beste: 1 Schlechteste: 3

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - '5'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Note 1: 5

    Beste: 5 Schlechteste: 5

    Durchschnitt: 5.0

    Urteil: nicht bestanden

    Sterne: **

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nnoten = []\nwhile True:\n    note = int(input())\n    if note == 0:\n        break\n    noten.append(note)\n\
  schnitt = sum(noten) / len(noten)\nprint(\"Noten:\", sorted(noten))\nprint(\"Beste:\", min(noten), \"Schlechteste:\", max(noten))\n\
  print(\"Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"\
  Urteil: gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\"\
  )\nelse:\n    print(\"Urteil: nicht bestanden\")\nprint(\"Sterne: \", end=\"\")\nfor i in range(7 - round(schnitt)):\n \
  \   print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 12.** Dein Code aus Stück 11 steht schon da. Statt der Notenliste erscheint jede Note in einer eigenen, nummerierten Zeile (in der eingegebenen Reihenfolge). Bei `2`, `1`, `3`, `0`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Note 1: 2
Note 2: 1
Note 3: 3
Beste: 1 Schlechteste: 3
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
