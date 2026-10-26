---
schema_version: 1
id: j044-erster-letzter
revision: 1
titel: Erster und letzter
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- text
- index
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der erste hat Index 0.
- kosten: 2
  text: Der letzte hat Index `fisch.length - 1`.
tests_sichtbar:
- input: []
  expected: 'Erster: M

    Letzter: e

    '
starter_code: 'const fisch = "Makrele";

  '
---

Gib den ersten und den letzten Buchstaben von `fisch` aus. Dein Code soll auch für jedes andere Wort stimmen, schreib also keine feste Zahl für das Ende:

```
Erster: M
Letzter: e
```
