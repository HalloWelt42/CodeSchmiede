---
schema_version: 1
id: j181-auspacken
revision: 1
titel: Zeile auspacken
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- destrukturierung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`const [a, b, c] = text.split(";");`'
tests_sichtbar:
- input:
  - Pia;3;Hering
  expected: 'Zeile? Pia nimmt 3 x Hering

    '
tests_versteckt:
- input:
  - Ole;1;Aal
  expected: 'Zeile? Ole nimmt 1 x Aal

    '
starter_code: ''
---

Lies eine Zeile wie `Pia;3;Hering` und pack sie mit **einer** Zeile in `kunde`, `anzahl` und `fisch` aus. Bei der Eingabe `Pia;3;Hering`:

```
Zeile? Pia nimmt 3 x Hering
```
