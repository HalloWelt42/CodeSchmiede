---
schema_version: 1
id: k112-vordraengeln
revision: 1
titel: Vordrängeln
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
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
  text: Einschieben an einer Stelle heißt auf Englisch insert.
tests_sichtbar:
- input: []
  expected: '[''Polly'', ''Pit'', ''Pia'']

    '
starter_code: 'schlange = ["Pit", "Pia"]

  schlange.___(0, "Polly")

  print(schlange)

  '
---

Polly drängelt sich ganz nach vorn. Ergänze die Methode anstelle von `___`.
