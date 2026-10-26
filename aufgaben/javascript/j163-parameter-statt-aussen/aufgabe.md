---
schema_version: 1
id: j163-parameter-statt-aussen
revision: 1
titel: Ohne fremde Namen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
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
  text: Die zweite Zeile rechnet mit 7 Prozent.
- kosten: 2
  text: '`function netto(brutto, satz = 19)`, die äußere Konstante kann weg.'
tests_sichtbar:
- input: []
  expected: '100 Euro brutto sind 84.03 Euro netto

    100 Euro brutto sind 93.46 Euro netto

    '
starter_code: "const satz = 19;\nfunction netto(brutto) {\n  return brutto / (1 + satz / 100);\n}\nconsole.log(`100 Euro brutto\
  \ sind ${netto(100).toFixed(2)} Euro netto`);\n"
---

`netto` greift heimlich auf den äußeren Namen `satz` zu. Gib der Funktion den Satz als zweiten Parameter mit Standardwert 19 und ruf sie für beide Fälle auf:

```
100 Euro brutto sind 84.03 Euro netto
100 Euro brutto sind 93.46 Euro netto
```
