---
schema_version: 1
id: k198-rekordliste
revision: 1
titel: Die Rekordliste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- datei
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Beim Eintragen: `if punkte > rekorde.get(name, 0):`.'
- kosten: 3
  text: Beim Laden jede Zeile mit `split(";")` zerlegen und die Punkte mit int umwandeln.
tests_sichtbar:
- input:
  - Pia
  - '30'
  - Pit
  - '17'
  - Pia
  - '42'
  - ende
  expected: 'Pia: 42

    Pit: 17

    Bester: Pia

    '
tests_versteckt:
- input:
  - Paul
  - '5'
  - ende
  expected: 'Paul: 5

    Bester: Paul

    '
- input:
  - A
  - '9'
  - B
  - '10'
  - A
  - '3'
  - ende
  expected: 'A: 9

    B: 10

    Bester: B

    '
starter_code: ''
---

Schreibe zwei Funktionen: `speichern(rekorde, dateiname)` schreibt ein Wörterbuch Name zu Punkte als Zeilen `Name;Punkte`, `laden(dateiname)` liest es wieder als Wörterbuch mit Zahlen. Lies Paare aus Name und Punkten ein, bis als Name `ende` kommt; bei doppelten Namen gilt die höhere Punktzahl. Speichere in `rekorde.txt`, lade wieder und gib alle Einträge der geladenen Liste und den Besten aus. Bei `Pia`, `30`, `Pit`, `17`, `Pia`, `42`, `ende`:

```
Pia: 42
Pit: 17
Bester: Pia
```
