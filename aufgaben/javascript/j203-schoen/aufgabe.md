---
schema_version: 1
id: j203-schoen
revision: 1
titel: Schön eingerückt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- json
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`JSON.stringify(daten, null, 2)`'
tests_sichtbar:
- input: []
  expected: "{\n  \"wagen\": \"Fischwagen\",\n  \"karte\": [\n    \"Hering\",\n    \"Suppe\"\n  ]\n}\n"
starter_code: 'const daten = { wagen: "Fischwagen", karte: ["Hering", "Suppe"] };

  '
---

Gib die Speisekarte als eingerückten JSON-Text aus, mit zwei Leerzeichen:

```
{
  "wagen": "Fischwagen",
  "karte": [
    "Hering",
    "Suppe"
  ]
}
```
