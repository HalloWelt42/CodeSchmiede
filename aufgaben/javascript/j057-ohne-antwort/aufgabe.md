---
schema_version: 1
id: j057-ohne-antwort
revision: 1
titel: Keine Antwort
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- eingabe
- nichts
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'In der Vorlage: `${antwort}` und `(${typeof antwort})`.'
- kosten: 2
  text: typeof null sagt object, ein alter Fehler von JavaScript.
tests_sichtbar:
- input:
  - '3'
  expected: 'Brötchen? Antwort: 3 (string)

    Als Zahl: 3

    '
tests_versteckt:
- input: []
  expected: 'Brötchen? Antwort: null (object)

    Als Zahl: 0

    '
starter_code: ''
---

Der Kunde soll eine Zahl Brötchen sagen. Gib aus, was angekommen ist, mit Typ, und was Number daraus macht. Bei der Eingabe `3`:

```
Brötchen? Antwort: 3 (string)
Als Zahl: 3
```

Ein versteckter Fall schickt gar keine Antwort. Dann liefert prompt `null`, und `Number(null)` ist übrigens 0.
