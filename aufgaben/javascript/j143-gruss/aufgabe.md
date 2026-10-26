---
schema_version: 1
id: j143-gruss
revision: 1
titel: Grüßen mit Standardwert
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- funktion
- standardwert
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`function gruss(name = "Gast")` setzt den Standardwert.'
- kosten: 2
  text: Mit `? :` entscheiden, ob mit oder ohne Wert aufgerufen wird.
tests_sichtbar:
- input:
  - Pia
  expected: 'Name? Moin, Pia!

    '
tests_versteckt:
- input:
  - ''
  expected: 'Name? Moin, Gast!

    '
- input: []
  expected: 'Name? Moin, Gast!

    '
starter_code: ''
---

Schreib eine Funktion `gruss(name)`, die `Moin, Name!` zurückgibt; ohne Namen heißt es `Moin, Gast!`. Lies einen Namen ein; ist die Antwort leer oder fehlt, ruf `gruss()` ohne Wert auf. Bei der Eingabe `Pia`:

```
Name? Moin, Pia!
```
