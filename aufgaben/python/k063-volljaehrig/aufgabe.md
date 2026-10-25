---
schema_version: 1
id: k063-volljaehrig
revision: 1
titel: Alt genug?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- vergleich
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Mindestens heißt größer oder gleich: `>=`.'
tests_sichtbar:
- input:
  - '21'
  expected: 'True

    '
tests_versteckt:
- input:
  - '17'
  expected: 'False

    '
- input:
  - '18'
  expected: 'True

    '
starter_code: ''
---

Lies ein Alter ein (ohne Fragetext) und gib aus, ob es mindestens 18 ist. Bei `21`:

```
True
```
