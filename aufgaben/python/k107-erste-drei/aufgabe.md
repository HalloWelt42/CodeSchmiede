---
schema_version: 1
id: k107-erste-drei
revision: 1
titel: Die ersten drei
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- liste
- scheiben
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ausschnitte gehen wie bei Text, auch mit negativen Zahlen.
tests_sichtbar:
- input: []
  expected: '[''Pia'', ''Pit'', ''Paul'']

    [''Bodo'', ''Mia'']

    '
starter_code: 'rangliste = ["Pia", "Pit", "Paul", "Polly", "Bodo", "Mia"]

  '
---

Gib die ersten drei und die letzten zwei Plätze der Rangliste als Ausschnitte aus:

```
['Pia', 'Pit', 'Paul']
['Bodo', 'Mia']
```
