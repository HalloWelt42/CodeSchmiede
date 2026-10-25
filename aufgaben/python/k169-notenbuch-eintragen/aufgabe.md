---
schema_version: 1
id: k169-notenbuch-eintragen
revision: 1
titel: 'Notenbuch: Einträge zählen'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- sichtbarkeit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`eintraege` braucht global, das Wörterbuch noten nicht.'
- kosten: 2
  text: Erst mit `fach in noten` nachschauen, dann eintragen.
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - Mathe
  - '3'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Mathe überschrieben

    Einträge: 3

    Mathe: 3 (befriedigend)

    Deutsch: 1 (sehr gut)

    Verschiedene Noten: [1, 3]

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

    Einträge: 1

    Sport: 1 (sehr gut)

    Verschiedene Noten: [1]

    Durchschnitt: 1.0

    Urteil: sehr gut

    Sterne: ******

    '
starter_code: "def urteil(note):\n    if note <= 1.5:\n        return \"sehr gut\"\n    elif note <= 2.5:\n        return\
  \ \"gut\"\n    elif note <= 3.5:\n        return \"befriedigend\"\n    elif note <= 4:\n        return \"ausreichend\"\n\
  \    else:\n        return \"nicht bestanden\"\n\n\ndef sterne(note):\n    return \"*\" * (7 - round(note))\n\n\ntitel =\
  \ \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten = {}\nwhile True:\n    fach = input()\n    if fach == \"\
  ende\":\n        break\n    noten[fach] = int(input())\nfor fach, note in noten.items():\n    print(f\"{fach}: {note} ({urteil(note)})\"\
  )\nprint(\"Verschiedene Noten:\", sorted(set(noten.values())))\nschnitt = sum(noten.values()) / len(noten)\nprint(\"Durchschnitt:\"\
  , schnitt)\nprint(\"Urteil:\", urteil(schnitt))\nprint(\"Sterne:\", sterne(schnitt))\n"
---

**Kapitelprojekt Notenbuch, Stück 16.** Dein Code aus Stück 15 steht schon da. Das Eintragen übernimmt jetzt eine Funktion `eintragen(fach, note)`: sie zählt im Namen `eintraege` draußen mit, meldet `<Fach> überschrieben`, wenn es das Fach schon gibt, und legt die Note ins Wörterbuch. Nach dem Einlesen erscheint die Zahl der Einträge. Bei `Mathe`, `2`, `Deutsch`, `1`, `Mathe`, `3`, `ende`:

```
=== MEIN NOTENBUCH ===
Mathe überschrieben
Einträge: 3
Mathe: 3 (befriedigend)
Deutsch: 1 (sehr gut)
Verschiedene Noten: [1, 3]
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
