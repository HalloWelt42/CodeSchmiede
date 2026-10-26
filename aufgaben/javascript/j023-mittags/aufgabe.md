---
schema_version: 1
id: j023-mittags
revision: 1
titel: Mittags wird gewischt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
  text: Den Namen gibt es schon; für einen neuen Wert brauchst du kein `let`.
tests_sichtbar:
- input: []
  expected: 'Heute: Hering

    Heute: Makrele

    '
starter_code: 'let angebot = "Hering";

  console.log("Heute:", angebot);


  console.log("Heute:", angebot);

  '
---

Mittags gibt es Makrele statt Hering. Ergänze **eine** Zeile zwischen den beiden Ausgaben, damit herauskommt:

```
Heute: Hering
Heute: Makrele
```
