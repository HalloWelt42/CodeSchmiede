---
schema_version: 1
id: k115-rangliste
revision: 1
titel: Die Rangliste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- auswerten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`sort(reverse=True)` sortiert absteigend.'
tests_sichtbar:
- input: []
  expected: '[42, 17, 8, 3]

    42

    '
starter_code: 'punkte = [8, 42, 3, 17]

  '
---

Sortiere die Punkte absteigend und gib die Liste und den Spitzenwert aus:

```
[42, 17, 8, 3]
42
```
