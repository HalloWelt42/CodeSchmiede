---
schema_version: 1
id: k091-buchstabieren
revision: 1
titel: Buchstabieren
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'R

    o

    b

    b

    e

    '
starter_code: "for b in \"Robbe\":\n    print(b)\n"
---

Der Code steht schon da: for geht das Wort Zeichen für Zeichen durch. Prüfe ihn.
