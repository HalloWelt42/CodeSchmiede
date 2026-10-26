---
schema_version: 1
id: j032-broetchenpreis
revision: 1
titel: Was kosten vier Brötchen?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mal ist `*`.
- kosten: 2
  text: '`console.log(anzahl, "Brötchen kosten", preis * anzahl);`'
tests_sichtbar:
- input: []
  expected: '4 Brötchen kosten 10

    '
starter_code: ''
---

Ein Heringsbrötchen kostet `2.5`, Paul nimmt `4`. Lege `preis` und `anzahl` als Konstanten an, rechne den Gesamtpreis aus und gib aus:

```
4 Brötchen kosten 10
```
