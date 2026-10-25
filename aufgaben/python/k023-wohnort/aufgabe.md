---
schema_version: 1
id: k023-wohnort
revision: 1
titel: Wo wohnst du?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- variablen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst `ort = ...`, dann ein print mit Text und Name, durch ein Komma getrennt.
- kosten: 2
  text: '`print("Ich wohne am", ort)` setzt das Leerzeichen selbst.'
tests_sichtbar:
- input: []
  expected: 'Ich wohne am Südpol

    '
starter_code: ''
---

Lege eine Variable `ort` mit dem Wert `Südpol` an und gib damit diesen Satz aus:

```
Ich wohne am Südpol
```
