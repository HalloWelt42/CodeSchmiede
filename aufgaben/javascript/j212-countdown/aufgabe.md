---
schema_version: 1
id: j212-countdown
revision: 1
titel: Countdown mit Takt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
tags:
- kurs
- zeitgeber
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: setInterval liefert eine Nummer, die clearInterval zum Stoppen braucht.
- kosten: 2
  text: Ohne clearInterval läuft es ewig.
tests_sichtbar:
- input:
  - '3'
  expected: 'Ab? 3

    2

    1

    Start!

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Ab? Start!

    '
- input:
  - '5'
  expected: 'Ab? 5

    4

    3

    2

    1

    Start!

    '
starter_code: ''
---

Lies eine Startzahl und zähle mit `setInterval` alle 10 Millisekunden herunter; bei 0 kommt `Start!` und das Intervall wird mit `clearInterval` gestoppt. Bei der Eingabe `3`:

```
Ab? 3
2
1
Start!
```
