---
schema_version: 1
id: k218-fuetterplan
revision: 1
titel: Der Fütterplan
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- datum
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In der Schleife ausgeben und danach `tag += timedelta(days=abstand)`.
- kosten: 3
  text: 'Kurzname: `KURZ[tag.weekday()]`.'
tests_sichtbar:
- input:
  - 25.10.2026
  - '10'
  - '3'
  expected: 'So 25.10.2026

    Mi 04.11.2026

    Sa 14.11.2026

    '
tests_versteckt:
- input:
  - 28.02.2028
  - '1'
  - '2'
  expected: 'Mo 28.02.2028

    Di 29.02.2028

    '
- input:
  - 01.01.2027
  - '7'
  - '1'
  expected: 'Fr 01.01.2027

    '
starter_code: 'from datetime import datetime, timedelta


  KURZ = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

  '
---

Im Zoo werden die Pinguine alle paar Tage mit Tintenfisch verwöhnt. Lies den ersten Tag in deutscher Schreibweise, den Abstand in Tagen und die Zahl der Termine ein. Gib jeden Termin mit Kurzname des Wochentags und deutschem Datum aus; die Kurznamen stehen schon da. Bei `25.10.2026`, `10`, `3`:

```
So 25.10.2026
Mi 04.11.2026
Sa 14.11.2026
```
