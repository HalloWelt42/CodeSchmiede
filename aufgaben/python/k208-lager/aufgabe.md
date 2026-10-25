---
schema_version: 1
id: k208-lager
revision: 1
titel: Das Fischlager
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 7
tags:
- kurs
- klasse
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`art, ware, anzahl = befehl.split()` zerlegt den Befehl.'
- kosten: 3
  text: 'In `entnehmen`: `if self.bestand.get(ware, 0) < anzahl: raise ValueError(...)`.'
tests_sichtbar:
- input:
  - rein Hering 5
  - raus Hering 2
  - raus Lachs 1
  - ende
  expected: 'Zu wenig Lachs

    Hering: 3

    '
tests_versteckt:
- input:
  - ende
  expected: ''
- input:
  - rein Eis 2
  - rein Wels 1
  - rein Eis 3
  - raus Eis 6
  - raus Wels 1
  - ende
  expected: 'Zu wenig Eis

    Eis: 5

    Wels: 0

    '
starter_code: ''
---

Schreibe eine Klasse `Lager` mit einem Wörterbuch `bestand` und zwei Methoden: `einlagern(ware, anzahl)` zählt dazu, `entnehmen(ware, anzahl)` zieht ab und löst einen `ValueError` mit `Zu wenig <ware>` aus, wenn nicht genug da ist. Lies Befehle wie `rein Hering 5` oder `raus Hering 2` ein (mit `split()` zerlegen), bis `ende` kommt; gefangene Fehler werden ausgegeben. Zum Schluss steht der Bestand je Ware. Bei `rein Hering 5`, `raus Hering 2`, `raus Lachs 1`, `ende`:

```
Zu wenig Lachs
Hering: 3
```
