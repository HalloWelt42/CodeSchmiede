---
schema_version: 1
id: j062-passwort
revision: 1
titel: Das Passwort
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- wahrheit
- vergleich
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Vorher alles klein machen, dann mit `===` vergleichen.
- kosten: 2
  text: '`eingabe.toLowerCase() === "sprotte"`'
tests_sichtbar:
- input:
  - SPROTTE
  expected: 'Passwort? Richtig: true

    '
tests_versteckt:
- input:
  - sprotte
  expected: 'Passwort? Richtig: true

    '
- input:
  - Sprotten
  expected: 'Passwort? Richtig: false

    '
starter_code: ''
---

Am Hintereingang des Fischwagens gilt das Passwort `Sprotte`, egal ob groß oder klein geschrieben. Bei der Eingabe `SPROTTE`:

```
Passwort? Richtig: true
```
