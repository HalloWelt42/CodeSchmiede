---
schema_version: 1
id: k034-gerecht-teilen
revision: 1
titel: Gerecht teilen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ganzzahlig teilen mit `//`, den Rest mit `%`.
tests_sichtbar:
- input: []
  expected: 'Jeder: 5

    Rest: 3

    '
starter_code: 'fische = 23

  pinguine = 4

  '
---

23 Fische sollen gerecht an 4 Pinguine gehen. Gib aus, wie viele jeder bekommt und wie viele übrig bleiben:

```
Jeder: 5
Rest: 3
```
