---
schema_version: 1
id: k053-begruessung
revision: 1
titel: Die Begrüßung
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Frage mit Leerzeichen am Ende genau so in input schreiben.
- kosten: 2
  text: Danach `print(f"Hallo {name}!")`.
tests_sichtbar:
- input:
  - Pia
  expected: 'Wie heißt du? Hallo Pia!

    '
tests_versteckt:
- input:
  - Bodo
  expected: 'Wie heißt du? Hallo Bodo!

    '
starter_code: ''
---

Frage mit `input("Wie heißt du? ")` nach dem Namen und begrüße dann. Bei der Eingabe `Pia` sieht die Ausgabe so aus (die Antwort selbst erscheint nicht, die tippt man ja):

```
Wie heißt du? Hallo Pia!
```
