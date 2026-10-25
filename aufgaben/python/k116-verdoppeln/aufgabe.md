---
schema_version: 1
id: k116-verdoppeln
revision: 1
titel: Alles doppelt
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- abstraktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`[z * 2 for z in zahlen]`'
tests_sichtbar:
- input: []
  expected: '[2, 8, 10, 14]

    '
starter_code: 'zahlen = [1, 4, 5, 7]

  '
---

Baue mit einer Listenabstraktion eine neue Liste, in der jede Zahl verdoppelt ist, und gib sie aus:

```
[2, 8, 10, 14]
```
