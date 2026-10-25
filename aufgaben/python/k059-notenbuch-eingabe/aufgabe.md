---
schema_version: 1
id: k059-notenbuch-eingabe
revision: 1
titel: 'Notenbuch: Noten eingeben'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ersetze die drei festen Noten durch `int(input())`.
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  - '4'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    '
- input:
  - '3'
  - '3'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 3.0

    '
starter_code: 'titel = "Mein Notenbuch"

  faecher = "Mathe, Deutsch, Musik"

  print(f"=== {titel.upper()} ===")

  print("Fächer:", faecher)

  mathe = 2

  deutsch = 1

  musik = 3

  print("Durchschnitt:", (mathe + deutsch + musik) / 3)

  '
---

**Kapitelprojekt Notenbuch, Stück 5.** Dein Code aus Stück 4 steht schon da. Die drei Noten sollen jetzt eingelesen werden, in der Reihenfolge Mathe, Deutsch, Musik, mit `int(input())` ohne Fragetext. Bei `2`, `1`, `3`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Durchschnitt: 2.0
```
