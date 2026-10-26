---
schema_version: 1
id: j074-ampel
revision: 1
titel: Die Ampel
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- verzweigung
- else
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit `else if` hängst du weitere Fälle an, `else` fängt den Rest.
tests_sichtbar:
- input:
  - gelb
  expected: 'Farbe? Warten

    '
tests_versteckt:
- input:
  - rot
  expected: 'Farbe? Stehen

    '
- input:
  - grün
  expected: 'Farbe? Gehen

    '
- input:
  - lila
  expected: 'Farbe? Ampel kaputt

    '
starter_code: ''
---

Lies die Farbe der Ampel ein: `rot` heißt `Stehen`, `gelb` heißt `Warten`, `grün` heißt `Gehen`, alles andere `Ampel kaputt`. Bei der Eingabe `gelb`:

```
Farbe? Warten
```
