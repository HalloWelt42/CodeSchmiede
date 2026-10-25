---
schema_version: 1
id: k186-wuerfelbecher
revision: 1
titel: Der Würfelbecher
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- modul
- menge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine leere Menge, in der Schleife `add`, zum Schluss `sorted`.
tests_sichtbar:
- input: []
  expected: '[1, 2, 3, 4, 5, 6]

    '
starter_code: ''
---

Würfle 600-mal mit `random.randint(1, 6)` und sammle die Augenzahlen in einer Menge. Gib die Menge sortiert aus. Bei so vielen Würfen kommt jede Zahl vor:

```
[1, 2, 3, 4, 5, 6]
```
