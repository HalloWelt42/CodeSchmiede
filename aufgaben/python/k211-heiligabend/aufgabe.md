---
schema_version: 1
id: k211-heiligabend
revision: 1
titel: Heiligabend
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- datum
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '2026-12-24

    '
starter_code: 'from datetime import date


  heiligabend = date(2026, 12, 24)

  print(heiligabend)

  '
---

Der Code steht schon da: ein Datum wird angelegt und ausgegeben. Prüfe ihn.
