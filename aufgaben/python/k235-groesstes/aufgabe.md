---
schema_version: 1
id: k235-groesstes
revision: 1
titel: Das Größte selbst finden
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- algorithmus
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Merke dir die Stelle der bisher größten, nicht nur den Wert.
- kosten: 2
  text: Nur bei echt größer wechseln, dann bleibt der erste Treffer.
tests_sichtbar:
- input:
  - '4'
  - '9'
  - '2'
  - '9'
  - ende
  expected: 'Größte: 9 an Stelle 1

    '
tests_versteckt:
- input:
  - '-5'
  - '-2'
  - ende
  expected: 'Größte: -2 an Stelle 1

    '
- input:
  - '7'
  - ende
  expected: 'Größte: 7 an Stelle 0

    '
starter_code: ''
---

Lies Zahlen ein, bis `ende` kommt. Finde ohne `max` die größte und ihre Stelle (ab 0). Bei `4`, `9`, `2`, `9`, `ende`:

```
Größte: 9 an Stelle 1
```
