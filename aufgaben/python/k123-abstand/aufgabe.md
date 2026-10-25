---
schema_version: 1
id: k123-abstand
revision: 1
titel: Der Abstand
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- tupel
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst `ax, ay = a`, dann dasselbe für b.
tests_sichtbar:
- input: []
  expected: '5 -2

    '
starter_code: 'a = (1, 6)

  b = (6, 4)

  '
---

Zwei Eisschollen liegen an den Punkten `a` und `b`. Packe beide Tupel aus und gib den Abstand in x- und y-Richtung aus (immer größer minus kleiner ist nicht nötig, einfach b minus a):

```
5 -2
```
