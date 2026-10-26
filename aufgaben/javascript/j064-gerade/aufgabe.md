---
schema_version: 1
id: j064-gerade
revision: 1
titel: Gerade oder nicht?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- wahrheit
- rest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Bei einer geraden Zahl bleibt beim Teilen durch 2 kein Rest.
- kosten: 2
  text: '`anzahl % 2 === 0`'
tests_sichtbar:
- input:
  - '6'
  expected: 'Pinguine? Gerade: true

    '
tests_versteckt:
- input:
  - '7'
  expected: 'Pinguine? Gerade: false

    '
- input:
  - '0'
  expected: 'Pinguine? Gerade: true

    '
starter_code: ''
---

Pinguine gehen immer zu zweit schwimmen. Lies die Zahl der Pinguine ein und gib aus, ob sie gerade ist. Bei der Eingabe `6`:

```
Pinguine? Gerade: true
```
