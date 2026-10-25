---
schema_version: 1
id: k189-notenbuch-median
revision: 1
titel: 'Notenbuch: der Median'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- projekt
- modul
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ganz oben: `from statistics import median`.'
- kosten: 2
  text: '`median(noten.values())` nimmt die Noten aus dem Wörterbuch.'
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - Musik
  - '4'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Einträge: 3

    Mathe: 2 (gut)

    Deutsch: 1 (sehr gut)

    Musik: 4 (ausreichend)

    Verschiedene Noten: [1, 2, 4]

    Durchschnitt: 2.3333333333333335

    Median: 2

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - Sport
  - '1'
  - Kunst
  - '2'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Einträge: 2

    Sport: 1 (sehr gut)

    Kunst: 2 (gut)

    Verschiedene Noten: [1, 2]

    Durchschnitt: 1.5

    Median: 1.5

    Urteil: sehr gut

    Sterne: *****

    '
starter_code: "def urteil(note):\n    if note <= 1.5:\n        return \"sehr gut\"\n    elif note <= 2.5:\n        return\
  \ \"gut\"\n    elif note <= 3.5:\n        return \"befriedigend\"\n    elif note <= 4:\n        return \"ausreichend\"\n\
  \    else:\n        return \"nicht bestanden\"\n\n\ndef sterne(note):\n    return \"*\" * (7 - round(note))\n\n\neintraege\
  \ = 0\n\n\ndef eintragen(fach, note):\n    global eintraege\n    eintraege += 1\n    if fach in noten:\n        print(f\"\
  {fach} überschrieben\")\n    noten[fach] = note\n\n\ndef lies_note(text):\n    try:\n        note = int(text)\n    except\
  \ ValueError:\n        raise ValueError(f\"{text} ist keine Zahl\")\n    if note < 1 or note > 6:\n        raise ValueError(f\"\
  {note} ist keine Note\")\n    return note\n\n\ntitel = \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten =\
  \ {}\nwhile True:\n    fach = input()\n    if fach == \"ende\":\n        break\n    try:\n        eintragen(fach, lies_note(input()))\n\
  \    except ValueError as fehler:\n        print(\"Übersprungen:\", fehler)\nprint(\"Einträge:\", eintraege)\nfor fach,\
  \ note in noten.items():\n    print(f\"{fach}: {note} ({urteil(note)})\")\nprint(\"Verschiedene Noten:\", sorted(set(noten.values())))\n\
  schnitt = sum(noten.values()) / len(noten)\nprint(\"Durchschnitt:\", schnitt)\nprint(\"Urteil:\", urteil(schnitt))\nprint(\"\
  Sterne:\", sterne(schnitt))\n"
---

**Kapitelprojekt Notenbuch, Stück 18.** Dein Code aus Stück 17 steht schon da. Unter dem Durchschnitt steht jetzt auch der Median der Noten, mit `median` aus dem Modul statistics. Bei `Mathe`, `2`, `Deutsch`, `1`, `Musik`, `4`, `ende`:

```
=== MEIN NOTENBUCH ===
Einträge: 3
Mathe: 2 (gut)
Deutsch: 1 (sehr gut)
Musik: 4 (ausreichend)
Verschiedene Noten: [1, 2, 4]
Durchschnitt: 2.3333333333333335
Median: 2
Urteil: gut
Sterne: *****
```
