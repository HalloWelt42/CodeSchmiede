---
schema_version: 1
id: j068-tuersteher
revision: 1
titel: Der Türsteher
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- wahrheit
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`prompt("Einladung? ") === "ja"` macht aus der Antwort true oder false.'
- kosten: 2
  text: Leg die Teilbedingungen in Namen, dann ist das Ergebnis `altGenug && mitbringsel`.
tests_sichtbar:
- input:
  - '4'
  - nein
  - ja
  expected: 'Alter? Einladung? Fisch? Alt genug: true

    Einladung oder Fisch: true

    Darf rein: true

    '
tests_versteckt:
- input:
  - '2'
  - ja
  - ja
  expected: 'Alter? Einladung? Fisch? Alt genug: false

    Einladung oder Fisch: true

    Darf rein: false

    '
- input:
  - '5'
  - nein
  - nein
  expected: 'Alter? Einladung? Fisch? Alt genug: true

    Einladung oder Fisch: false

    Darf rein: false

    '
- input:
  - '3'
  - ja
  - nein
  expected: 'Alter? Einladung? Fisch? Alt genug: true

    Einladung oder Fisch: true

    Darf rein: true

    '
starter_code: ''
---

Zur Pinguinparty darf, wer mindestens 3 Jahre alt ist und entweder eine Einladung hat oder Fisch mitbringt. Lies das Alter und zwei Antworten (`ja` oder `nein`) ein. Gib jede Teilbedingung und das Ergebnis aus. Bei den Eingaben `4`, `nein` und `ja`:

```
Alter? Einladung? Fisch? Alt genug: true
Einladung oder Fisch: true
Darf rein: true
```
