---
schema_version: 1
id: k064-gerade
revision: 1
titel: Gerade Zahl?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- vergleich
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Gerade heißt: beim Teilen durch 2 bleibt kein Rest.'
- kosten: 2
  text: '`zahl % 2 == 0`'
tests_sichtbar:
- input:
  - '6'
  expected: 'True

    '
tests_versteckt:
- input:
  - '7'
  expected: 'False

    '
- input:
  - '0'
  expected: 'True

    '
starter_code: ''
---

Lies eine ganze Zahl ein und gib aus, ob sie gerade ist. Bei `6`:

```
True
```
