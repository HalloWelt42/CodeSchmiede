---
schema_version: 1
id: k162-klickzaehler
revision: 1
titel: Der Klickzähler
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
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
  text: Mit `global zaehler` darf die Funktion den äußeren Namen ändern.
tests_sichtbar:
- input: []
  expected: '3

    '
starter_code: "zaehler = 0\n\n\ndef klick():\n    ___ zaehler\n    zaehler += 1\n\n\nklick()\nklick()\nklick()\nprint(zaehler)\n"
---

Ergänze die Lücke `___`, damit jeder Klick den Zähler draußen erhöht:

```
3
```
