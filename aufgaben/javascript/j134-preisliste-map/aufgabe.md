---
schema_version: 1
id: j134-preisliste-map
revision: 1
titel: Preisliste aus der Map
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for (const fisch of preise.keys())`'
tests_sichtbar:
- input: []
  expected: 'Hering: 2.50

    Aal: 5.00

    Makrele: 3.20

    Alles einmal: 10.70

    '
starter_code: 'const preise = new Map();

  preise.set("Hering", 2.5);

  preise.set("Aal", 5);

  preise.set("Makrele", 3.2);

  '
---

Gib alle Preise der Map in ihrer Reihenfolge aus und darunter die Summe aller Preise:

```
Hering: 2.50
Aal: 5.00
Makrele: 3.20
Alles einmal: 10.70
```
