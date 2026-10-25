---
schema_version: 1
id: k055-kommapreis
revision: 1
titel: Der Kommapreis
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- eingabe
- umwandeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Für Kommazahlen gibt es `float(...)`.
tests_sichtbar:
- input:
  - '2.5'
  expected: '5.0

    '
tests_versteckt:
- input:
  - '1.25'
  expected: '2.5

    '
- input:
  - '3'
  expected: '6.0

    '
starter_code: ''
---

Ein Fischbrötchen kostet so viel, wie eingegeben wird; Pit kauft zwei. Lies den Preis mit `input()` und gib den Gesamtpreis aus. Bei `2.5`:

```
5.0
```
