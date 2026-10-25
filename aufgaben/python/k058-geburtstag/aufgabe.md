---
schema_version: 1
id: k058-geburtstag
revision: 1
titel: Der Geburtstagsrechner
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- eingabe
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Das Alter umwandeln, bevor du rechnest; die Rechnung darf in die geschweiften Klammern.
tests_sichtbar:
- input:
  - Pit
  - '4'
  expected: 'Pit wird nächstes Jahr 5.

    '
tests_versteckt:
- input:
  - Mia
  - '9'
  expected: 'Mia wird nächstes Jahr 10.

    '
starter_code: ''
---

Lies einen Namen und ein Alter ein (ohne Fragetexte) und gib mit einem f-String aus, wie alt die Person nächstes Jahr wird. Bei `Pit` und `4`:

```
Pit wird nächstes Jahr 5.
```
