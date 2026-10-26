---
schema_version: 1
id: j061-groesser
revision: 1
titel: Wer hat mehr?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- wahrheit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`pia > paul` ist schon die Antwort, true oder false.'
tests_sichtbar:
- input:
  - '7'
  - '4'
  expected: 'Pia? Paul? Pia hat mehr: true

    '
tests_versteckt:
- input:
  - '3'
  - '9'
  expected: 'Pia? Paul? Pia hat mehr: false

    '
- input:
  - '5'
  - '5'
  expected: 'Pia? Paul? Pia hat mehr: false

    '
starter_code: 'const pia = Number(prompt("Pia? "));

  const paul = Number(prompt("Paul? "));

  '
---

Lies zwei Fänge ein und gib aus, ob der erste größer ist. Bei den Eingaben `7` und `4`:

```
Pia? Paul? Pia hat mehr: true
```
