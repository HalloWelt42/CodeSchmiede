---
schema_version: 1
id: j128-inventur
revision: 1
titel: Die Inventur
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- objekt
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`eintrag.split(" ")` trennt Ware und Menge; die Menge mit Number umwandeln.'
- kosten: 2
  text: Neue Ware bekommt die Menge, bekannte wird mit += angepasst; danach prüfen, ob sie gestrichen wird.
tests_sichtbar:
- input:
  - Hering 5
  - Aal 2
  - Hering -1
  - Aal -2
  expected: 'Eintrag? Eintrag? Eintrag? Eintrag? Eintrag? Hering: 4

    Sorten: 1

    '
tests_versteckt:
- input: []
  expected: 'Eintrag? Lager leer

    Sorten: 0

    '
- input:
  - Aal 3
  - Aal -5
  - Butt 1
  - Aal 2
  expected: 'Eintrag? Eintrag? Eintrag? Eintrag? Eintrag? Butt: 1

    Aal: 2

    Sorten: 2

    '
starter_code: ''
---

Lies Einträge wie `Hering 5` oder `Hering -2`, bis eine leere Antwort oder keine mehr kommt, und führe ein Lager als Objekt: Zahlen kommen dazu oder gehen ab. Fällt eine Ware auf 0 oder darunter, wird sie mit `delete` gestrichen. Am Ende jede Ware mit Bestand (in der Reihenfolge, in der sie dazukam) und die Zahl der Sorten, bei leerem Lager vorher `Lager leer`. Bei den Eingaben `Hering 5`, `Aal 2`, `Hering -1` und `Aal -2`:

```
Eintrag? Eintrag? Eintrag? Eintrag? Eintrag? Hering: 4
Sorten: 1
```
