---
schema_version: 1
id: k131-nachschlagen
revision: 1
titel: Nachschlagen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- woerterbuch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'Lachs

    '
starter_code: 'lieblingsfisch = {"Pit": "Hering", "Pia": "Lachs"}

  print(lieblingsfisch["Pia"])

  '
---

Der Code steht schon da: ein Wörterbuch mit Lieblingsfischen, dann wird nachgeschlagen. Prüfe ihn.
