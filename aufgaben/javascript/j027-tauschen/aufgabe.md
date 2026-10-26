---
schema_version: 1
id: j027-tauschen
revision: 1
titel: Plätze tauschen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- variablen
- zuweisung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Merk dir zuerst, wer vorne steht, bevor du vorne überschreibst.
- kosten: 2
  text: 'Drei Zeilen: `const merker = vorne;`, dann `vorne = hinten;`, dann `hinten = merker;`'
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

Vorne steht Pia, hinten Paul. Tausche die beiden mit einer Hilfsvariable, **ohne** die Namen Pia und Paul noch einmal zu schreiben. Die beiden `console.log` am Ende bleiben, wie sie sind:

```
Vorne: Paul
Hinten: Pia
```
