---
schema_version: 1
id: j158-fangbuch
revision: 1
titel: Das Fangbuch
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- rueckrufmethoden
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Jeder Eintrag wird ein Objekt: `{ name: teile[0], anzahl: Number(teile[1]) }`.'
- kosten: 2
  text: Bei Gleichstand behält sort die ursprüngliche Reihenfolge, das passt hier.
tests_sichtbar:
- input:
  - Pia 7
  - Ole 12
  - Ida 0
  - Bo 10
  expected: 'Fang? Fang? Fang? Fang? Fang? Gesamt: 29

    Große Fänge: Ole 12, Bo 10

    Rangliste: Ole, Bo, Pia, Ida

    Jemand ohne Fang: ja

    '
tests_versteckt:
- input:
  - A 3
  expected: 'Fang? Fang? Gesamt: 3

    Große Fänge: keine

    Rangliste: A

    Jemand ohne Fang: nein

    '
- input:
  - A 10
  - B 20
  - C 15
  - ''
  expected: 'Fang? Fang? Fang? Fang? Gesamt: 45

    Große Fänge: A 10, B 20, C 15

    Rangliste: B, C, A

    Jemand ohne Fang: nein

    '
starter_code: ''
---

Lies Einträge wie `Pia 7`, bis eine leere Antwort oder keine mehr kommt, als Objekte mit `name` und `anzahl` in ein Array. Dann, jeweils mit den Methoden aus diesem Kapitel: die Summe mit reduce, die großen Fänge (ab 10) mit filter und map (sonst `keine`), die Namen absteigend nach Fang mit sort und map, und ob jemand gar nichts gefangen hat mit some. Bei den Eingaben `Pia 7`, `Ole 12`, `Ida 0` und `Bo 10`:

```
Fang? Fang? Fang? Fang? Fang? Gesamt: 29
Große Fänge: Ole 12, Bo 10
Rangliste: Ole, Bo, Pia, Ida
Jemand ohne Fang: ja
```
