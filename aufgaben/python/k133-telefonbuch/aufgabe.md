---
schema_version: 1
id: k133-telefonbuch
revision: 1
titel: Das Telefonbuch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- woerterbuch
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`get(name, "unbekannt")` liefert den Ersatz, wenn es den Namen nicht gibt.'
tests_sichtbar:
- input:
  - Pia
  expected: '5512

    '
tests_versteckt:
- input:
  - Bodo
  expected: 'unbekannt

    '
- input:
  - Paul
  expected: '0815

    '
starter_code: 'nummern = {"Pit": "4711", "Pia": "5512", "Paul": "0815"}

  '
---

Lies einen Namen ein und gib die Nummer aus dem Telefonbuch aus, oder `unbekannt`, wenn es den Namen nicht gibt. Benutze `get`. Bei `Pia`:

```
5512
```
