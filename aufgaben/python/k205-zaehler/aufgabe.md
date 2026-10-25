---
schema_version: 1
id: k205-zaehler
revision: 1
titel: Der Zähler
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
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
  text: '`__init__` braucht hier außer self keinen Parameter.'
tests_sichtbar:
- input:
  - klick
  - klick
  - 'null'
  - klick
  - ende
  expected: 'Stand: 1

    '
tests_versteckt:
- input:
  - ende
  expected: 'Stand: 0

    '
- input:
  - klick
  - klick
  - klick
  - ende
  expected: 'Stand: 3

    '
starter_code: ''
---

Schreibe eine Klasse `Zaehler` mit der Eigenschaft `stand` (zu Beginn 0) und den Methoden `klick()` und `zuruecksetzen()`. Lies Befehle ein (`klick` oder `null`), bis `ende` kommt, und gib dann den Stand aus. Bei `klick`, `klick`, `null`, `klick`, `ende`:

```
Stand: 1
```
