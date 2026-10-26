---
schema_version: 1
id: j104-gaeste-sammeln
revision: 1
titel: Gäste einsammeln
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- array
- anhaengen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein leeres Array `[]` vor der Schleife, darin `gaeste.push(name);`.
- kosten: 2
  text: '`!name` ist wahr bei leerem Text und bei null.'
tests_sichtbar:
- input:
  - Pia
  - Ole
  - ''
  expected: 'Gast? Gast? Gast? 2 Gäste: Pia, Ole

    '
tests_versteckt:
- input:
  - Ida
  expected: 'Gast? Gast? 1 Gäste: Ida

    '
- input:
  - A
  - B
  - C
  - D
  - ''
  expected: 'Gast? Gast? Gast? Gast? Gast? 4 Gäste: A, B, C, D

    '
starter_code: ''
---

Lies Namen ein, bis eine leere Antwort kommt oder gar keine mehr, sammle sie mit `push` und gib sie am Ende mit `join` aus. Bei den Eingaben `Pia`, `Ole` und einer leeren Antwort:

```
Gast? Gast? Gast? 2 Gäste: Pia, Ole
```
