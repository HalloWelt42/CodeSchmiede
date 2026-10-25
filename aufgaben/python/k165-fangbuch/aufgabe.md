---
schema_version: 1
id: k165-fangbuch
revision: 1
titel: Das Fangbuch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
- liste
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: append verändert die Liste, dafür braucht es kein global.
tests_sichtbar:
- input:
  - Hering
  - Lachs
  - ende
  expected: '[''Hering'', ''Lachs'']

    2 Fische

    '
tests_versteckt:
- input:
  - ende
  expected: '[]

    0 Fische

    '
starter_code: 'fang = []

  '
---

Schreibe eine Funktion `notieren(fisch)`, die den Fisch an die Liste `fang` draußen anhängt. Lies Fische ein, bis `ende` kommt, und gib dann die Liste und ihre Länge aus. Bei `Hering`, `Lachs`, `ende`:

```
['Hering', 'Lachs']
2 Fische
```
