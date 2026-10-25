---
schema_version: 1
id: k018-steckbrief
revision: 1
titel: Steckbrief
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- ausgabe
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Text und Zahl passen in ein `print`, getrennt durch ein Komma.
- kosten: 2
  text: '`print("Alter:", 4)` setzt das Leerzeichen selbst.'
tests_sichtbar:
- input: []
  expected: 'Steckbrief

    Name: Pit

    Alter: 4

    Lieblingsessen: Hering

    '
starter_code: ''
---

Pit braucht einen Steckbrief für den Schwimmverein. Gib ihn genau so aus; das Alter ist eine **Zahl**:

```
Steckbrief
Name: Pit
Alter: 4
Lieblingsessen: Hering
```
