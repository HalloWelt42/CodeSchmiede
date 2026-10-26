---
schema_version: 1
id: j117-mitte
revision: 1
titel: In die Mitte
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Mitte ist `Math.floor(karte.length / 2)`.
- kosten: 2
  text: Mit Anzahl 0 fügt splice nur ein.
tests_sichtbar:
- input: []
  expected: 'Hering, Aal, Fischsuppe, Makrele, Dorsch

    '
starter_code: 'const karte = ["Hering", "Aal", "Makrele", "Dorsch"];

  '
---

Pit möchte die Fischsuppe genau in die Mitte der Karte schieben (bei 4 Gerichten also an Index 2). Füge sie mit `splice` ein, ohne etwas zu streichen, und rechne die Mitte aus der Länge aus:

```
Hering, Aal, Fischsuppe, Makrele, Dorsch
```
