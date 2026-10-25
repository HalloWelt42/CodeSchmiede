---
schema_version: 1
id: k153-begruessen
revision: 1
titel: Persönlich begrüßen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- funktion
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`def begruessen(name):` und darunter eingerückt das print.'
tests_sichtbar:
- input:
  - Pia
  - Pit
  expected: 'Hallo, Pia!

    Hallo, Pit!

    '
tests_versteckt:
- input:
  - A
  - B
  expected: 'Hallo, A!

    Hallo, B!

    '
starter_code: ''
---

Schreibe eine Funktion `begruessen(name)`, die `Hallo, <name>!` ausgibt. Lies zwei Namen ein und begrüße beide. Bei `Pia` und `Pit`:

```
Hallo, Pia!
Hallo, Pit!
```
