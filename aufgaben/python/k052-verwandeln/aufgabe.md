---
schema_version: 1
id: k052-verwandeln
revision: 1
titel: Verwandeln
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- umwandeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Aus Text wird mit `int(...)` eine ganze Zahl.
tests_sichtbar:
- input: []
  expected: '24

    '
starter_code: 'zahl = ___("12")

  print(zahl * 2)

  '
---

Ergänze die Verwandlung, damit `24` herauskommt und nicht `1212`.
