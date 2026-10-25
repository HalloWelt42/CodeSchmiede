---
schema_version: 1
id: k182-abrunden
revision: 1
titel: Abrunden
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- modul
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hinter import steht der Name des Werkzeugs.
tests_sichtbar:
- input: []
  expected: '3

    '
starter_code: 'from math import ___


  print(floor(3.7))

  '
---

Ergänze die Lücke `___`, damit `floor` ohne Modulnamen benutzt werden kann:

```
3
```
