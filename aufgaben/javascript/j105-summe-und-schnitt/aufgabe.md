---
schema_version: 1
id: j105-summe-und-schnitt
revision: 1
titel: Fangstatistik
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- array
- for_of
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Sammler vor der Schleife.
- kosten: 2
  text: Der Schnitt ist Summe durch `faenge.length`, dann `toFixed(1)`.
tests_sichtbar:
- input: []
  expected: 'Summe: 41

    Schnitt: 5.9

    '
starter_code: 'const faenge = [4, 9, 2, 7, 5, 8, 6];

  '
---

Rechne aus den Fängen der Woche die Summe und den Durchschnitt mit einer Nachkommastelle aus:

```
Summe: 41
Schnitt: 5.9
```
