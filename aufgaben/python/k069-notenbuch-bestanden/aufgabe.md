---
schema_version: 1
id: k069-notenbuch-bestanden
revision: 1
titel: 'Notenbuch: bestanden?'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- projekt
- vergleich
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst `schnitt = ...`, dann zweimal ausgeben.
- kosten: 2
  text: '`print("Bestanden:", schnitt <= 4)`'
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    Bestanden: True

    '
tests_versteckt:
- input:
  - '5'
  - '5'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 4.333333333333333

    Bestanden: False

    '
- input:
  - '4'
  - '4'
  - '4'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 4.0

    Bestanden: True

    '
starter_code: 'titel = "Mein Notenbuch"

  faecher = "Mathe, Deutsch, Musik"

  print(f"=== {titel.upper()} ===")

  print("Fächer:", faecher)

  mathe = int(input())

  deutsch = int(input())

  musik = int(input())

  print("Durchschnitt:", (mathe + deutsch + musik) / 3)

  '
---

**Kapitelprojekt Notenbuch, Stück 6.** Dein Code aus Stück 5 steht schon da. Rechne den Durchschnitt in einen Namen `schnitt` und gib als vierte Zeile aus, ob er höchstens 4 ist. Bei `2`, `1`, `3`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Durchschnitt: 2.0
Bestanden: True
```
