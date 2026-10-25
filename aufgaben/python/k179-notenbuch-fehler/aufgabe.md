---
schema_version: 1
id: k179-notenbuch-fehler
revision: 1
titel: 'Notenbuch: falsche Eingaben'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- projekt
- ausnahme
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'In `lies_note`: erst `int(text)` im try, bei ValueError selbst einen neuen mit eigener Meldung auslösen.'
- kosten: 2
  text: 'Danach prüfen: `if note < 1 or note > 6: raise ValueError(f"{note} ist keine Note")`.'
- kosten: 4
  text: 'Beim Einlesen: `eintragen(fach, lies_note(input()))` in ein try mit `except ValueError as fehler`.'
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Musik
  - sehr gut
  - Kunst
  - '9'
  - Deutsch
  - '1'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Übersprungen: sehr gut ist keine Zahl

    Übersprungen: 9 ist keine Note

    Einträge: 2

    Mathe: 2 (gut)

    Deutsch: 1 (sehr gut)

    Verschiedene Noten: [1, 2]

    Durchschnitt: 1.5

    Urteil: sehr gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - Sport
  - '0'
  - Sport
  - '6'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Übersprungen: 0 ist keine Note

    Einträge: 1

    Sport: 6 (nicht bestanden)

    Verschiedene Noten: [6]

    Durchschnitt: 6.0

    Urteil: nicht bestanden

    Sterne: *

    '
starter_code: "def urteil(note):\n    if note <= 1.5:\n        return \"sehr gut\"\n    elif note <= 2.5:\n        return\
  \ \"gut\"\n    elif note <= 3.5:\n        return \"befriedigend\"\n    elif note <= 4:\n        return \"ausreichend\"\n\
  \    else:\n        return \"nicht bestanden\"\n\n\ndef sterne(note):\n    return \"*\" * (7 - round(note))\n\n\neintraege\
  \ = 0\n\n\ndef eintragen(fach, note):\n    global eintraege\n    eintraege += 1\n    if fach in noten:\n        print(f\"\
  {fach} überschrieben\")\n    noten[fach] = note\n\n\ntitel = \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten\
  \ = {}\nwhile True:\n    fach = input()\n    if fach == \"ende\":\n        break\n    eintragen(fach, int(input()))\nprint(\"\
  Einträge:\", eintraege)\nfor fach, note in noten.items():\n    print(f\"{fach}: {note} ({urteil(note)})\")\nprint(\"Verschiedene\
  \ Noten:\", sorted(set(noten.values())))\nschnitt = sum(noten.values()) / len(noten)\nprint(\"Durchschnitt:\", schnitt)\n\
  print(\"Urteil:\", urteil(schnitt))\nprint(\"Sterne:\", sterne(schnitt))\n"
---

**Kapitelprojekt Notenbuch, Stück 17.** Dein Code aus Stück 16 steht schon da. Falsche Eingaben bringen das Notenbuch nicht mehr zum Absturz: eine Funktion `lies_note(text)` wandelt um und löst einen `ValueError` aus, mit `<text> ist keine Zahl` oder `<note> ist keine Note` (gültig sind 1 bis 6). Beim Einlesen wird der Fehler gefangen und mit `Übersprungen: ` gemeldet; ein übersprungener Eintrag zählt nicht. Bei `Mathe`, `2`, `Musik`, `sehr gut`, `Kunst`, `9`, `Deutsch`, `1`, `ende`:

```
=== MEIN NOTENBUCH ===
Übersprungen: sehr gut ist keine Zahl
Übersprungen: 9 ist keine Note
Einträge: 2
Mathe: 2 (gut)
Deutsch: 1 (sehr gut)
Verschiedene Noten: [1, 2]
Durchschnitt: 1.5
Urteil: sehr gut
Sterne: *****
```
