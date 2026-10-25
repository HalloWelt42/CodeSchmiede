---
schema_version: 1
id: k168-spielstand
revision: 1
titel: Der Spielstand
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- sichtbarkeit
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Jede Funktion braucht ihr eigenes global.
- kosten: 3
  text: Nach jedem Zug prüfen, ob die Leben aus sind, und dann mit break enden.
tests_sichtbar:
- input:
  - t
  - d
  - t
  - ende
  expected: 'Punkte: 20, Leben: 2

    '
- input:
  - d
  - d
  - d
  expected: 'Spiel vorbei

    Punkte: 0, Leben: 0

    '
tests_versteckt:
- input:
  - ende
  expected: 'Punkte: 0, Leben: 3

    '
- input:
  - t
  - t
  - d
  - t
  - d
  - d
  - t
  expected: 'Spiel vorbei

    Punkte: 30, Leben: 0

    '
starter_code: 'punkte = 0

  leben = 3

  '
---

Ein Spiel beginnt mit 0 Punkten und 3 Leben. Schreibe zwei Funktionen: `treffer()` gibt 10 Punkte, `daneben()` kostet ein Leben. Lies Züge ein (`t` oder `d`), bis `ende` kommt oder keine Leben mehr da sind; dann erscheint `Spiel vorbei`. Zum Schluss steht der Spielstand da. Bei `t`, `d`, `t`, `ende`:

```
Punkte: 20, Leben: 2
```

Bei `d`, `d`, `d`:

```
Spiel vorbei
Punkte: 0, Leben: 0
```
