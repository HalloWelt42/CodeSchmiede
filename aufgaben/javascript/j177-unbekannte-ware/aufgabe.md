---
schema_version: 1
id: j177-unbekannte-ware
revision: 1
titel: Unbekannte Ware
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- throw
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im try erst den Preis holen, dann zur Summe; scheitert preis, wird auch nichts addiert.
tests_sichtbar:
- input:
  - Hering
  - Lachs
  - Suppe
  expected: 'Ware? Hering: 2.50

    Ware? Lachs: Ware gibt es nicht

    Ware? Suppe: 4.50

    Ware? Summe: 7.00

    '
tests_versteckt:
- input: []
  expected: 'Ware? Summe: 0.00

    '
- input:
  - Aal
  - ''
  expected: 'Ware? Aal: Ware gibt es nicht

    Ware? Summe: 0.00

    '
starter_code: ''
---

Lies Waren, bis eine leere Antwort oder keine mehr kommt. Eine Funktion `preis(ware)` schlägt in einer Map nach und wirft bei unbekannten Waren `Error("Ware gibt es nicht")`. Gib je Ware den Preis oder `Name: Ware gibt es nicht` aus und am Ende die Summe der gefundenen. Bei den Eingaben `Hering`, `Lachs` und `Suppe`:

```
Ware? Hering: 2.50
Ware? Lachs: Ware gibt es nicht
Ware? Suppe: 4.50
Ware? Summe: 7.00
```
