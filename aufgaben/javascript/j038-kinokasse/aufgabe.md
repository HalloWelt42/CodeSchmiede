---
schema_version: 1
id: j038-kinokasse
revision: 1
titel: Die Kinokasse am Eisberg
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- rechnen
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst die beiden Beträge mit `*`, dann zur Summe dazu.
- kosten: 2
  text: '`Math.round(39.5)` rundet kaufmännisch auf 40.'
tests_sichtbar:
- input: []
  expected: 'Erwachsene: 22.5

    Kinder: 17

    Karten: 7

    Summe: 39.5

    Gerundet: 40

    '
starter_code: ''
---

Im Pinguinkino kosten Karten für Erwachsene `7.5`, für Kinder `4.25`. Heute kommen 3 Erwachsene und 4 Kinder. Rechne die beiden Beträge aus, sammle die Summe in `let summe` mit `+=` und zähle die Karten mit `+=` in `karten`. Zum Schluss den auf ganze Euro gerundeten Betrag:

```
Erwachsene: 22.5
Kinder: 17
Karten: 7
Summe: 39.5
Gerundet: 40
```
