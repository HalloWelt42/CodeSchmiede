---
schema_version: 1
id: k101-erste-liste
revision: 1
titel: Die erste Liste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
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
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '[''Hering'', ''Sprotte'', ''Lachs'']

    3

    '
starter_code: 'sorten = ["Hering", "Sprotte", "Lachs"]

  print(sorten)

  print(len(sorten))

  '
---

Der Code steht schon da: eine Liste mit drei Fischsorten, dann ihre Länge. Prüfe ihn.
