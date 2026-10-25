---
schema_version: 1
id: k038-stunden-minuten
revision: 1
titel: Stunden und Minuten
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- rechnen
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Eine Stunde hat 60 Minuten: ganzzahlig teilen und Rest.'
- kosten: 2
  text: '`print(minuten // 60, "Stunden", ...)`'
tests_sichtbar:
- input: []
  expected: '2 Stunden 15 Minuten

    '
starter_code: 'minuten = 135

  '
---

Der Pinguinfilm dauert 135 Minuten. Gib aus, wie viele ganze Stunden und restliche Minuten das sind:

```
2 Stunden 15 Minuten
```
