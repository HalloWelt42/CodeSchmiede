---
schema_version: 1
id: k177-unbekannte-ware
revision: 1
titel: Unbekannte Ware
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- ausnahme
- woerterbuch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein fehlender Schlüssel löst `KeyError` aus.
tests_sichtbar:
- input:
  - Hering
  - Wal
  - Eis
  - kasse
  expected: 'Unbekannt: Wal

    Summe: 5

    '
tests_versteckt:
- input:
  - kasse
  expected: 'Summe: 0

    '
- input:
  - Lachs
  - Lachs
  - Robbe
  - Hai
  - kasse
  expected: 'Unbekannt: Robbe

    Unbekannt: Hai

    Summe: 12

    '
starter_code: 'preise = {"Hering": 3, "Eis": 2, "Lachs": 6}

  '
---

Lies Waren ein, bis `kasse` kommt. Hole den Preis direkt mit `preise[ware]` und fange den `KeyError` ab: unbekannte Waren werden gemeldet, die anderen summiert. Bei `Hering`, `Wal`, `Eis`, `kasse`:

```
Unbekannt: Wal
Summe: 5
```
