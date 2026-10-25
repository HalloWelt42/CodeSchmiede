---
schema_version: 1
id: k042-fstring-luecke
revision: 1
titel: Der Wert muss rein
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- text
- fstring
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In die geschweiften Klammern gehört der Name, dessen Wert eingesetzt werden soll.
tests_sichtbar:
- input: []
  expected: 'Pit hat 4 Fische.

    '
starter_code: 'name = "Pit"

  fische = 4

  print(f"{name} hat {___} Fische.")

  '
---

Ergänze den f-String so, dass `Pit hat 4 Fische.` herauskommt.
