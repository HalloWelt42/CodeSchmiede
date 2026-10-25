---
schema_version: 1
id: k231-lineare-suche
revision: 1
titel: Der Reihe nach
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- algorithmus
- suchen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '2

    '
starter_code: "def suche(liste, ziel):\n    for i in range(len(liste)):\n        if liste[i] == ziel:\n            return\
  \ i\n    return -1\n\n\nprint(suche([4, 9, 2, 7], 2))\n"
---

Der Code steht schon da: eine lineare Suche und ein Aufruf. Prüfe ihn und verfolge im Ablauf, wie die Schleife beim Treffer endet.
