---
schema_version: 1
id: k071-erster-if
revision: 1
titel: Die erste Weiche
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'Satt!

    Fertig.

    '
starter_code: "fische = 5\nif fische > 3:\n    print(\"Satt!\")\nprint(\"Fertig.\")\n"
---

Der Code steht schon da: das `if` lässt den eingerückten Block nur laufen, wenn die Bedingung wahr ist. Prüfe ihn.
