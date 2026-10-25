---
schema_version: 1
id: k222-alle-zahlen
revision: 1
titel: Alle Zahlen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- regex
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 22
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Alle Treffer sammelt `findall`.
tests_sichtbar:
- input: []
  expected: '[''3'', ''12'', ''1'']

    '
starter_code: 'import re


  print(re.___(r"\d+", "3 Heringe, 12 Lachse und 1 Wal"))

  '
---

Ergänze die Lücke `___`, damit alle Zahlen des Satzes als Liste erscheinen:

```
['3', '12', '1']
```
