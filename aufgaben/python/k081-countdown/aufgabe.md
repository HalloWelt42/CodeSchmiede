---
schema_version: 1
id: k081-countdown
revision: 1
titel: Der Countdown
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '3

    2

    1

    Start!

    '
starter_code: "zahl = 3\nwhile zahl > 0:\n    print(zahl)\n    zahl -= 1\nprint(\"Start!\")\n"
---

Der Code steht schon da: die Schleife zählt rückwärts. Prüfe ihn und spiel den Ablauf im Kopf durch.
