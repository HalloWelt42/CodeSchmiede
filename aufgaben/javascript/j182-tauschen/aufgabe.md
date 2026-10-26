---
schema_version: 1
id: j182-tauschen
revision: 1
titel: Tausch ohne Merker
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- destrukturierung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`[vorne, hinten] = [hinten, vorne];`'
tests_sichtbar:
- input: []
  expected: 'Vorne: Paul

    Hinten: Pia

    '
starter_code: 'let vorne = "Pia";

  let hinten = "Paul";

  // hier tauschen


  console.log("Vorne:", vorne);

  console.log("Hinten:", hinten);

  '
---

Tausche `vorne` und `hinten` in einer Zeile, ohne Hilfsvariable:

```
Vorne: Paul
Hinten: Pia
```
