---
schema_version: 1
id: j211-spaeter
revision: 1
titel: Erst später
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- zeitgeber
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`setTimeout(() => console.log("Möwe"), 20);`'
tests_sichtbar:
- input: []
  expected: 'Pinguin

    Robbe

    Möwe

    '
starter_code: '// Möwe nach 20 ms


  // Robbe nach 10 ms


  console.log("Pinguin");

  '
---

Ergänze zwei Zeitgeber, sodass die Ausgabe in dieser Reihenfolge erscheint, obwohl die `console.log` für Möwe und Robbe im Code vor dem Pinguin stehen. Die Möwe kommt nach 20, die Robbe nach 10 Millisekunden:

```
Pinguin
Robbe
Möwe
```
