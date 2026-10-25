---
schema_version: 1
id: k136-umdrehen
revision: 1
titel: Andersherum
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- woerterbuch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein leeres Wörterbuch und in der Schleife umgekehrt eintragen.
tests_sichtbar:
- input: []
  expected: '{''Hering'': ''Pit'', ''Lachs'': ''Pia''}

    '
starter_code: 'lieblingsfisch = {"Pit": "Hering", "Pia": "Lachs"}

  '
---

Baue aus dem Wörterbuch ein neues, in dem Schlüssel und Werte vertauscht sind:

```
{'Hering': 'Pit', 'Lachs': 'Pia'}
```
