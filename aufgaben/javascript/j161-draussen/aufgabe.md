---
schema_version: 1
id: j161-draussen
revision: 1
titel: Draußen unbekannt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im Block nur noch zuweisen, ohne let, sonst gibt es zwei verschiedene preis.
tests_sichtbar:
- input:
  - '3'
  expected: 'Brötchen? Preis: 7.5

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Brötchen? Preis: 0

    '
starter_code: "const anzahl = Number(prompt(\"Brötchen? \"));\nif (anzahl > 0) {\n  let preis = anzahl * 2.5;\n}\nconsole.log(\"\
  Preis:\", preis);\n"
---

Das Programm bricht ab: `ReferenceError: preis is not defined`. Leg `preis` vor dem if an (mit 0), damit der Wert nach dem Block noch da ist. Bei der Eingabe `3`:

```
Brötchen? Preis: 7.5
```
