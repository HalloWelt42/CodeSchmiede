---
schema_version: 1
id: k213-wochentag
revision: 1
titel: Welcher Wochentag?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- datum
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`date.fromisoformat(input())` liest das Datum, `weekday()` ist der Index in der Liste.'
tests_sichtbar:
- input:
  - '2026-10-25'
  expected: 'Sonntag

    '
tests_versteckt:
- input:
  - '2027-01-01'
  expected: 'Freitag

    '
- input:
  - '2026-11-02'
  expected: 'Montag

    '
starter_code: 'from datetime import date


  WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

  '
---

Lies ein Datum in der Form `2026-10-25` ein und gib den Wochentag auf Deutsch aus. Die Liste der Namen steht schon da. Bei `2026-10-25`:

```
Sonntag
```
