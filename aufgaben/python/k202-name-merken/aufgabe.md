---
schema_version: 1
id: k202-name-merken
revision: 1
titel: Den Namen merken
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Rechts steht der Parameter, der beim Bauen hereinkommt.
tests_sichtbar:
- input: []
  expected: 'Hering

    Lachs

    '
starter_code: "class Fisch:\n    def __init__(self, art):\n        self.art = ___\n\n\nprint(Fisch(\"Hering\").art)\nprint(Fisch(\"\
  Lachs\").art)\n"
---

Ergänze die Lücke `___`, damit jeder Fisch seine Art als Eigenschaft bekommt:

```
Hering
Lachs
```
