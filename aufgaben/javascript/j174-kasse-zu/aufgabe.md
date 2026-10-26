---
schema_version: 1
id: j174-kasse-zu
revision: 1
titel: Die Kasse geht immer zu
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Durchgänge, je ein try ... catch ... finally.
tests_sichtbar:
- input:
  - '3'
  - '50'
  expected: 'Anzahl? 3 verkauft

    Kasse zu

    Anzahl? Abgelehnt: zu viele

    Kasse zu

    '
tests_versteckt:
- input:
  - '11'
  - '10'
  expected: 'Anzahl? Abgelehnt: zu viele

    Kasse zu

    Anzahl? 10 verkauft

    Kasse zu

    '
starter_code: "function verkaufen(anzahl) {\n  if (anzahl > 10) {\n    throw new Error(\"zu viele\");\n  }\n  console.log(`${anzahl}\
  \ verkauft`);\n}\n"
---

`verkaufen(anzahl)` soll bei mehr als 10 Brötchen einen Fehler werfen. Egal was passiert, danach muss `Kasse zu` erscheinen. Bei den Eingaben `3` und dann `50`:

```
Anzahl? 3 verkauft
Kasse zu
Anzahl? Abgelehnt: zu viele
Kasse zu
```
