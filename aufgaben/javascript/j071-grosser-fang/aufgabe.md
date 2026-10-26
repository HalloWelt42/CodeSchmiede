---
schema_version: 1
id: j071-grosser-fang
revision: 1
titel: Großer Fang
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mehr als 10 heißt größer als 10.
tests_sichtbar:
- input:
  - '12'
  expected: 'Fische? Großer Fang!

    Feierabend

    '
tests_versteckt:
- input:
  - '10'
  expected: 'Fische? Feierabend

    '
- input:
  - '3'
  expected: 'Fische? Feierabend

    '
- input:
  - '11'
  expected: 'Fische? Großer Fang!

    Feierabend

    '
starter_code: "const fische = Number(prompt(\"Fische? \"));\nif (___) {\n  console.log(\"Großer Fang!\");\n}\nconsole.log(\"\
  Feierabend\");\n"
---

Ergänze die Bedingung: Bei mehr als 10 Fischen soll `Großer Fang!` erscheinen, sonst nichts. `Feierabend` kommt immer. Bei der Eingabe `12`:

```
Fische? Großer Fang!
Feierabend
```
