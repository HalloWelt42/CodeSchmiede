---
schema_version: 1
id: j153-nur-grosse
revision: 1
titel: Nur die großen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- rueckrufmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`map(Number)` macht aus allen Texten Zahlen: Number ist selbst eine Funktion.'
- kosten: 2
  text: '`faenge.filter(f => f >= 5)`'
tests_sichtbar:
- input:
  - 4,9,2,7,5
  expected: 'Fänge? [ 9, 7, 5 ]

    '
tests_versteckt:
- input:
  - 1,2
  expected: 'Fänge? []

    '
- input:
  - 10,3,6
  expected: 'Fänge? [ 10, 6 ]

    '
starter_code: ''
---

Lies Fänge mit Kommas ein und gib mit `filter` nur die aus, die mindestens 5 sind. Bei der Eingabe `4,9,2,7,5`:

```
Fänge? [ 9, 7, 5 ]
```
