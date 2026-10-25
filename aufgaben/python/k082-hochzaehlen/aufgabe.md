---
schema_version: 1
id: k082-hochzaehlen
revision: 1
titel: Hochzählen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
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
  text: Ohne Änderung an i läuft die Schleife ewig.
- kosten: 2
  text: '`i += 1`'
tests_sichtbar:
- input: []
  expected: '1

    2

    3

    4

    5

    '
starter_code: "i = 1\nwhile i <= 5:\n    print(i)\n    ___\n"
---

Die Schleife soll von 1 bis 5 zählen, aber eine Zeile fehlt noch. Ergänze sie anstelle von `___`.
