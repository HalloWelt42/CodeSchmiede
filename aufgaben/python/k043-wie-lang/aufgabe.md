---
schema_version: 1
id: k043-wie-lang
revision: 1
titel: Wie lang ist der Name?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`len(name)` darf direkt in die geschweiften Klammern.'
tests_sichtbar:
- input: []
  expected: 'Kaiserpinguin hat 13 Zeichen

    '
starter_code: 'name = "Kaiserpinguin"

  '
---

Gib mit einem f-String aus, wie viele Zeichen der Name hat:

```
Kaiserpinguin hat 13 Zeichen
```
