---
schema_version: 1
id: k132-eintragen
revision: 1
titel: Neu eintragen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
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
  text: '`lieblingsfisch["Paul"] = "Sprotte"`'
tests_sichtbar:
- input: []
  expected: '{''Pit'': ''Hering'', ''Pia'': ''Lachs'', ''Paul'': ''Sprotte''}

    '
starter_code: 'lieblingsfisch = {"Pit": "Hering", "Pia": "Lachs"}

  ___

  print(lieblingsfisch)

  '
---

Trage Paul mit seinem Lieblingsfisch `Sprotte` ein. Ersetze `___`.
