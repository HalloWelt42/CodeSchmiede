---
schema_version: 1
id: j028-steckbrief-namen
revision: 1
titel: Steckbrief mit Namen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- variablen
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst ausgeben, dann ändern, dann wieder ausgeben.
- kosten: 2
  text: 'Das Komma gehört in den Text: `console.log("Alles Gute zum Geburtstag,", name);`'
tests_sichtbar:
- input: []
  expected: 'Name: Pit

    Alter: 4

    Alles Gute zum Geburtstag, Pit

    Alter: 5

    '
starter_code: ''
---

Pit ist ein Jahr älter geworden. Lege `name` als `const` mit `"Pit"` an und `alter` als `let` mit `4`. Gib den Steckbrief aus, setze `alter` dann auf `5` und gib die letzte Zeile noch einmal aus:

```
Name: Pit
Alter: 4
Alles Gute zum Geburtstag, Pit
Alter: 5
```
