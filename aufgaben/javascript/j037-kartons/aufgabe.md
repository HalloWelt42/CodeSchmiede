---
schema_version: 1
id: j037-kartons
revision: 1
titel: Brötchen in Kartons
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- rechnen
- math
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ein angefangener Karton zählt mit: aufrunden mit `Math.ceil`.'
- kosten: 2
  text: Die Brötchen im letzten Karton sind der Rest.
tests_sichtbar:
- input: []
  expected: 'Kartons: 5

    Im letzten: 2

    '
starter_code: 'const broetchen = 50;

  const proKarton = 12;

  '
---

50 Brötchen kommen in Kartons zu je 12 Stück. Wie viele Kartons braucht es, wenn der letzte nicht ganz voll sein muss, und wie viele Brötchen liegen im letzten?

```
Kartons: 5
Im letzten: 2
```
