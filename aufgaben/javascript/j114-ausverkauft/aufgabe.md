---
schema_version: 1
id: j114-ausverkauft
revision: 1
titel: Ausverkauft
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst die Stelle mit indexOf suchen; -1 heißt, er steht nicht drauf.
- kosten: 2
  text: '`karte.splice(stelle, 1);` streicht genau einen.'
tests_sichtbar:
- input:
  - Aal
  expected: 'Ausverkauft? Karte: Hering, Makrele, Dorsch

    '
tests_versteckt:
- input:
  - Dorsch
  expected: 'Ausverkauft? Karte: Hering, Aal, Makrele

    '
- input:
  - Lachs
  expected: 'Ausverkauft? Karte: Hering, Aal, Makrele, Dorsch

    '
starter_code: 'const karte = ["Hering", "Aal", "Makrele", "Dorsch"];

  '
---

Lies einen ausverkauften Fisch ein und streiche ihn mit `splice` von der Karte, falls er draufsteht. Bei der Eingabe `Aal`:

```
Ausverkauft? Karte: Hering, Makrele, Dorsch
```
