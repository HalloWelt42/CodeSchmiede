---
schema_version: 1
id: k166-konto
revision: 1
titel: Das Taschengeldkonto
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- sichtbarkeit
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In der Funktion zuerst `global konto`.
- kosten: 2
  text: 'Genau 100 abheben geht noch: verglichen wird mit `>`.'
tests_sichtbar:
- input:
  - '30'
  - '80'
  - '50'
  - '0'
  expected: 'Zu wenig Geld

    Stand: 20

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Stand: 100

    '
- input:
  - '100'
  - '1'
  - '0'
  expected: 'Zu wenig Geld

    Stand: 0

    '
starter_code: 'konto = 100

  '
---

Auf dem Konto liegen 100. Schreibe eine Funktion `abheben(betrag)`, die das Konto draußen verringert, aber nur, wenn genug da ist; sonst gibt sie `Zu wenig Geld` aus. Lies Beträge ein, bis `0` kommt, und gib am Ende den Stand aus. Bei `30`, `80`, `50`, `0`:

```
Zu wenig Geld
Stand: 20
```
