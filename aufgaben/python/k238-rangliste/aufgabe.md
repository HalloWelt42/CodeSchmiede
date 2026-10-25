---
schema_version: 1
id: k238-rangliste
revision: 1
titel: Die Rangliste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 7
tags:
- kurs
- algorithmus
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Paare als Tupel `(name, punkte)` sammeln; verglichen wird `liste[j][1]`.
- kosten: 3
  text: 'Absteigend: das Größte nach vorn, also `>` statt `<`.'
- kosten: 5
  text: Fehlt der Name, meldet das Programm `<Name> ist nicht dabei`.
tests_sichtbar:
- input:
  - Pit
  - '17'
  - Pia
  - '42'
  - Paul
  - '8'
  - ende
  - Pit
  expected: '1. Pia 42

    2. Pit 17

    3. Paul 8

    Pit ist auf Platz 2

    '
tests_versteckt:
- input:
  - A
  - '1'
  - ende
  - B
  expected: '1. A 1

    B ist nicht dabei

    '
- input:
  - A
  - '1'
  - B
  - '2'
  - C
  - '3'
  - ende
  - A
  expected: '1. C 3

    2. B 2

    3. A 1

    A ist auf Platz 3

    '
starter_code: ''
---

Lies Paare aus Name und Punkten ein, bis als Name `ende` kommt, und dann noch einen gesuchten Namen. Sortiere die Paare ohne `sorted` und `sort` absteigend nach Punkten (mit Auswahlsortieren, bei Gleichstand ist die Reihenfolge egal), gib die Rangliste aus und dann den Platz des gesuchten Namens mit linearer Suche. Bei `Pit`, `17`, `Pia`, `42`, `Paul`, `8`, `ende`, `Pit`:

```
1. Pia 42
2. Pit 17
3. Paul 8
Pit ist auf Platz 2
```
