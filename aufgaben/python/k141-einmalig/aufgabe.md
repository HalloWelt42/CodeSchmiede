---
schema_version: 1
id: k141-einmalig
revision: 1
titel: Jeder nur einmal
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- menge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '2

    '
starter_code: 'faenge = [2, 5, 2, 2, 5]

  print(len(set(faenge)))

  '
---

Der Code steht schon da: aus einer Liste mit Doppelten wird eine Menge, dann wird gezählt. Prüfe ihn.
