---
schema_version: 1
id: k216-in-hundert-tagen
revision: 1
titel: In hundert Tagen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
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
  text: Einlesen mit `datetime.strptime(text, "%d.%m.%Y").date()`.
- kosten: 2
  text: Dazu `timedelta(days=tage)`.
tests_sichtbar:
- input:
  - 25.10.2026
  - '100'
  expected: '02.02.2027

    '
tests_versteckt:
- input:
  - 28.02.2028
  - '1'
  expected: '29.02.2028

    '
- input:
  - 01.01.2026
  - '-1'
  expected: '31.12.2025

    '
starter_code: ''
---

Lies ein Datum in deutscher Schreibweise ein (`25.10.2026`) und eine Zahl von Tagen. Gib das Datum danach wieder deutsch aus. Bei `25.10.2026` und `100`:

```
02.02.2027
```
