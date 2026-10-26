---
schema_version: 1
id: j136-schon-gesehen
revision: 1
titel: Schon gesehen?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- set
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein leeres Set vor der Schleife; `has` fragt, `add` merkt.
tests_sichtbar:
- input:
  - Hering
  - Aal
  - Hering
  expected: 'Fisch? Neu!

    Fisch? Neu!

    Fisch? Kenne ich schon

    Fisch? Verschiedene: 2

    '
tests_versteckt:
- input: []
  expected: 'Fisch? Verschiedene: 0

    '
- input:
  - a
  - a
  - a
  - ''
  expected: 'Fisch? Neu!

    Fisch? Kenne ich schon

    Fisch? Kenne ich schon

    Fisch? Verschiedene: 1

    '
starter_code: ''
---

Lies Fische, bis eine leere Antwort oder keine mehr kommt. Zu jedem sagst du `Neu!` oder `Kenne ich schon`, am Ende die Zahl der verschiedenen. Bei den Eingaben `Hering`, `Aal` und `Hering`:

```
Fisch? Neu!
Fisch? Neu!
Fisch? Kenne ich schon
Fisch? Verschiedene: 2
```
