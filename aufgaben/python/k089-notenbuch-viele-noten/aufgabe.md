---
schema_version: 1
id: k089-notenbuch-viele-noten
revision: 1
titel: 'Notenbuch: beliebig viele Noten'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- projekt
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Summe und Anzahl vor der Schleife bei 0; while True mit break bei 0.
- kosten: 2
  text: Danach `schnitt = summe / anzahl`.
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

    '
tests_versteckt:
- input:
  - '1'
  - '2'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: 2

    Durchschnitt: 1.5

    Urteil: sehr gut

    '
- input:
  - '5'
  - '6'
  - '4'
  - '5'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: 4

    Durchschnitt: 5.0

    Urteil: nicht bestanden

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nmathe = int(input())\ndeutsch = int(input())\nmusik = int(input())\nschnitt = (mathe + deutsch + musik)\
  \ / 3\nprint(\"Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n  \
  \  print(\"Urteil: gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil:\
  \ ausreichend\")\nelse:\n    print(\"Urteil: nicht bestanden\")\n"
---

**Kapitelprojekt Notenbuch, Stück 8.** Dein Code aus Stück 7 steht schon da. Statt genau drei Noten liest das Notenbuch jetzt Noten ein, bis eine `0` kommt, und gibt zusätzlich ihre Anzahl aus. Bei `2`, `1`, `3`, `0`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Noten: 3
Durchschnitt: 2.0
Urteil: gut
```
