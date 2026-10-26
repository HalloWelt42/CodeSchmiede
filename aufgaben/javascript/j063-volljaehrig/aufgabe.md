---
schema_version: 1
id: j063-volljaehrig
revision: 1
titel: Ab 18
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- wahrheit
- vergleich
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Mit 18 ist man schon volljährig: größer oder gleich.'
tests_sichtbar:
- input:
  - '18'
  expected: 'Alter? Volljährig: true

    '
tests_versteckt:
- input:
  - '17'
  expected: 'Alter? Volljährig: false

    '
- input:
  - '42'
  expected: 'Alter? Volljährig: true

    '
starter_code: ''
---

Lies das Alter ein und gib aus, ob jemand volljährig ist, also 18 oder älter. Bei der Eingabe `18`:

```
Alter? Volljährig: true
```
