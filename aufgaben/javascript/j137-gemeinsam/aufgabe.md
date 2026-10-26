---
schema_version: 1
id: j137-gemeinsam
revision: 1
titel: Gemeinsame Gäste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- set
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Sets, dann je eine Schleife mit `has`.
tests_sichtbar:
- input:
  - Pia,Ole,Ida
  - Ole,Bo,Ida,Kim
  expected: 'Erster Tag? Zweiter Tag? Beide Tage: Ole, Ida

    Nur am zweiten: Bo, Kim

    '
tests_versteckt:
- input:
  - A,B
  - C
  expected: "Erster Tag? Zweiter Tag? Beide Tage: \nNur am zweiten: C\n"
- input:
  - X,Y
  - Y,X
  expected: "Erster Tag? Zweiter Tag? Beide Tage: X, Y\nNur am zweiten: \n"
starter_code: ''
---

Lies die Gäste von zwei Tagen ein, jeweils mit Kommas. Gib aus, wer an beiden Tagen da war (Reihenfolge vom ersten Tag) und wer nur am zweiten Tag kam. Bei den Eingaben `Pia,Ole,Ida` und `Ole,Bo,Ida,Kim`:

```
Erster Tag? Zweiter Tag? Beide Tage: Ole, Ida
Nur am zweiten: Bo, Kim
```
