---
schema_version: 1
id: k099-notenbuch-sterne
revision: 1
titel: 'Notenbuch: Sterne'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Erst `print("Sterne: ", end="")`, dann je Stern `print("*", end="")`, zum Schluss `print()`.'
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: 3

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: 2

    Durchschnitt: 1.0

    Urteil: sehr gut

    Sterne: ******

    '
- input:
  - '5'
  - '6'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: 2

    Durchschnitt: 5.5

    Urteil: nicht bestanden

    Sterne: *

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nsumme = 0\nanzahl = 0\nwhile True:\n    note = int(input())\n    if note == 0:\n        break\n   \
  \ summe += note\n    anzahl += 1\nschnitt = summe / anzahl\nprint(\"Noten:\", anzahl)\nprint(\"Durchschnitt:\", schnitt)\n\
  if schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"Urteil: gut\")\nelif schnitt <= 3.5:\n\
  \    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\")\nelse:\n    print(\"Urteil:\
  \ nicht bestanden\")\n"
---

**Kapitelprojekt Notenbuch, Stück 9.** Dein Code aus Stück 8 steht schon da. Gib als letzte Zeile Sterne aus: 7 minus der gerundete Durchschnitt (`round(schnitt)`), alle in einer Zeile hinter `Sterne: `. Mit `print(..., end="")` bleibt print in derselben Zeile. Bei `2`, `1`, `3`, `0`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Noten: 3
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
