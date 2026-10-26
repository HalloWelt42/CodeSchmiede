---
schema_version: 1
id: j146-groessere
revision: 1
titel: Die größere Zahl
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- funktion
- return
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Den größeren von a und b nochmal mit c vergleichen: Aufrufe ineinander.'
tests_sichtbar:
- input:
  - '4'
  - '9'
  - '7'
  expected: 'Pia? Paul? Pit? Größter Fang: 9

    '
tests_versteckt:
- input:
  - '8'
  - '2'
  - '5'
  expected: 'Pia? Paul? Pit? Größter Fang: 8

    '
- input:
  - '1'
  - '3'
  - '6'
  expected: 'Pia? Paul? Pit? Größter Fang: 6

    '
starter_code: ''
---

Schreib `groessere(a, b)` mit zwei return: ist a größer, endet sie gleich mit a, sonst liefert sie b. Benutze sie, um den größten von drei eingelesenen Fängen zu finden. Bei den Eingaben `4`, `9` und `7`:

```
Pia? Paul? Pit? Größter Fang: 9
```
