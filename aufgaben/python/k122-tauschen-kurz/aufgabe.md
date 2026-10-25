---
schema_version: 1
id: k122-tauschen-kurz
revision: 1
titel: Tauschen in einer Zeile
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- tupel
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`links, rechts = rechts, links`'
tests_sichtbar:
- input: []
  expected: 'Pia Paul

    '
starter_code: 'links = "Paul"

  rechts = "Pia"

  ___

  print(links, rechts)

  '
---

Tausche links und rechts in einer einzigen Zeile anstelle von `___`.
