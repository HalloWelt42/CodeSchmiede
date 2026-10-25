---
schema_version: 1
id: k161-drinnen-draussen
revision: 1
titel: Drinnen und draußen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- sichtbarkeit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'drinnen

    draußen

    '
starter_code: "x = \"draußen\"\n\n\ndef zeigen():\n    x = \"drinnen\"\n    print(x)\n\n\nzeigen()\nprint(x)\n"
---

Der Code steht schon da: zwei Namen x, einer in der Funktion, einer draußen. Prüfe ihn und schau im Ablauf, wie die beiden Rahmen entstehen.
