---
schema_version: 1
id: k207-wettfischen
revision: 1
titel: Das Wettfischen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- klasse
- liste
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`angler.append(Angler(name, int(input())))` baut und sammelt in einem Schritt.'
- kosten: 2
  text: Den Sieger als ganzes Objekt merken.
tests_sichtbar:
- input:
  - Pia
  - '5'
  - Pit
  - '8'
  - Paul
  - '2'
  - ende
  expected: 'Sieger: Pit mit 8

    Durchschnitt: 5.0

    '
tests_versteckt:
- input:
  - Polly
  - '3'
  - ende
  expected: 'Sieger: Polly mit 3

    Durchschnitt: 3.0

    '
starter_code: ''
---

Schreibe eine Klasse `Angler` mit Name und Fang. Lies Paare aus Name und Fang ein, bis als Name `ende` kommt, und sammle die Angler in einer Liste. Gib den Sieger und den durchschnittlichen Fang aus. Bei `Pia`, `5`, `Pit`, `8`, `Paul`, `2`, `ende`:

```
Sieger: Pit mit 8
Durchschnitt: 5.0
```
