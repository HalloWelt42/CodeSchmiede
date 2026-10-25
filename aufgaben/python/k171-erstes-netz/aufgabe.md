---
schema_version: 1
id: k171-erstes-netz
revision: 1
titel: Das erste Netz
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- ausnahme
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'Fisch ist keine Zahl

    Fertig

    '
starter_code: "try:\n    print(int(\"Fisch\"))\nexcept ValueError:\n    print(\"Fisch ist keine Zahl\")\nprint(\"Fertig\"\
  )\n"
---

Der Code steht schon da: eine Umwandlung, die scheitert, und ein Netz darunter. Prüfe ihn.
