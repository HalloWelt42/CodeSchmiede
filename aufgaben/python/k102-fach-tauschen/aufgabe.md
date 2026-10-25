---
schema_version: 1
id: k102-fach-tauschen
revision: 1
titel: Ein Fach neu belegen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- liste
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Gezählt wird ab 0.
tests_sichtbar:
- input: []
  expected: '[''Pit'', ''Polly'', ''Paul'']

    '
starter_code: 'kolonie = ["Pit", "Pia", "Paul"]

  kolonie[___] = "Polly"

  print(kolonie)

  '
---

Im mittleren Fach soll statt `Pia` jetzt `Polly` sitzen. Ersetze `___` durch den richtigen Index.
