---
schema_version: 1
id: j066-wochenende
revision: 1
titel: Ruhetag
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- wahrheit
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Jeder Tag braucht seinen eigenen Vergleich, verbunden mit `||`.
- kosten: 2
  text: 'Geöffnet ist das Gegenteil: `!ruhetag`.'
tests_sichtbar:
- input:
  - Montag
  expected: 'Tag? Ruhetag: true

    Geöffnet: false

    '
tests_versteckt:
- input:
  - Dienstag
  expected: 'Tag? Ruhetag: true

    Geöffnet: false

    '
- input:
  - Freitag
  expected: 'Tag? Ruhetag: false

    Geöffnet: true

    '
starter_code: ''
---

Der Fischwagen hat am Montag und am Dienstag Ruhetag. Lies den Wochentag ein und gib aus, ob Ruhetag ist und ob geöffnet ist. Bei der Eingabe `Montag`:

```
Tag? Ruhetag: true
Geöffnet: false
```
