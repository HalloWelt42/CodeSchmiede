---
schema_version: 1
id: j168-stempelautomat
revision: 1
titel: Der Stempelautomat
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- sichtbarkeit
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Wie beim Konto: Die Map lebt im Automaten, nach außen gehen nur zwei Funktionen.'
- kosten: 2
  text: Nach dem fünften Stempel den Stand auf 0 setzen, die Karte zählt weiter mit.
tests_sichtbar:
- input:
  - Pia
  - Ole
  - Pia
  expected: 'Wer? Pia: 1 von 5

    Wer? Ole: 1 von 5

    Wer? Pia: 2 von 5

    Wer? Karten: 2

    '
tests_versteckt:
- input: []
  expected: 'Wer? Karten: 0

    '
- input:
  - A
  - A
  - A
  - A
  - A
  - A
  - B
  - ''
  expected: 'Wer? A: 1 von 5

    Wer? A: 2 von 5

    Wer? A: 3 von 5

    Wer? A: 4 von 5

    Wer? A: Karte voll, ein Brötchen gratis!

    Wer? A: 1 von 5

    Wer? B: 1 von 5

    Wer? Karten: 2

    '
starter_code: ''
---

Schreib `automatBauen(voll)`, die eine Funktion `stempeln(name)` liefert. Sie merkt sich in einer Map, wie viele Stempel jeder hat, und meldet `Name: n von 5`. Beim fünften Stempel heißt es stattdessen `Name: Karte voll, ein Brötchen gratis!` und die Karte beginnt von vorn. Lies Namen, bis eine leere Antwort oder keine mehr kommt, und gib am Ende aus, wie viele verschiedene Karten es gibt (dafür liefert der Automat eine zweite Funktion `karten()`). Bei den Eingaben `Pia`, `Ole`, `Pia`:

```
Wer? Pia: 1 von 5
Wer? Ole: 1 von 5
Wer? Pia: 2 von 5
Wer? Karten: 2
```
