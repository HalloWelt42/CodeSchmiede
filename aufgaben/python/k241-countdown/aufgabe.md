---
schema_version: 1
id: k241-countdown
revision: 1
titel: Der rekursive Countdown
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- rekursion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
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

    Abtauchen!

    '
starter_code: "def countdown(n):\n    if n == 0:\n        print(\"Abtauchen!\")\n    else:\n        print(n)\n        countdown(n\
  \ - 1)\n\n\ncountdown(3)\n"
---

Der Code steht schon da: ein Countdown, der sich selbst aufruft. Prüfe ihn und schau im Ablauf, wie sich die Rahmen stapeln.
