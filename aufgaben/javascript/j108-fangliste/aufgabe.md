---
schema_version: 1
id: j108-fangliste
revision: 1
titel: Die Fangliste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 7
tags:
- kurs
- array
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ohne Umwandeln würden die Texte bei += zusammengeklebt.
- kosten: 2
  text: Eine Zählschleife reicht für Summe und besten Tag zugleich.
tests_sichtbar:
- input:
  - 4,9,2,7
  expected: 'Fänge? Tage: 4

    Summe: 22

    Bester Tag: 2 mit 9

    Schnitt: 5.5

    '
tests_versteckt:
- input:
  - '5'
  expected: 'Fänge? Tage: 1

    Summe: 5

    Bester Tag: 1 mit 5

    Schnitt: 5.0

    '
- input:
  - 1,2,3,10,4,10
  expected: 'Fänge? Tage: 6

    Summe: 30

    Bester Tag: 4 mit 10

    Schnitt: 5.0

    '
starter_code: ''
---

Die Fänge kommen als eine Zeile mit Kommas, etwa `4,9,2,7`. Zerlege sie, wandle jeden Wert in eine Zahl und sammle die Zahlen mit push in einem neuen Array. Gib dann die Zahl der Tage, die Summe, den besten Tag (Tag 1 ist der erste) und den Schnitt mit einer Stelle aus. Bei der Eingabe `4,9,2,7`:

```
Fänge? Tage: 4
Summe: 22
Bester Tag: 2 mit 9
Schnitt: 5.5
```
