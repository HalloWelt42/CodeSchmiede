---
schema_version: 1
id: k092-range-luecke
revision: 1
titel: Bis zehn
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- for
- range
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Das Ende gehört nicht dazu.
tests_sichtbar:
- input: []
  expected: '1

    2

    3

    4

    5

    6

    7

    8

    9

    10

    '
starter_code: "for i in range(1, ___):\n    print(i)\n"
---

Die Schleife soll die Zahlen von 1 bis 10 ausgeben. Ersetze `___` durch die richtige Zahl.
