---
schema_version: 1
id: k111-anhaengen
revision: 1
titel: Hinten anstellen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- listenmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '[''Pit'', ''Pia'', ''Paul'']

    '
starter_code: 'schlange = ["Pit", "Pia"]

  schlange.append("Paul")

  print(schlange)

  '
---

Der Code steht schon da: Paul stellt sich hinten an. Prüfe ihn.
