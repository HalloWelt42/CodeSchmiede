---
schema_version: 1
id: j185-beliebig-viele
revision: 1
titel: Beliebig viele
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- spread
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`...preise` als letzter Parameter sammelt alle übrigen Argumente.'
- kosten: 2
  text: Beim Aufruf verteilt `...idasPreise` das Array.
tests_sichtbar:
- input: []
  expected: 'Pia: 3 Posten, 8.75 Euro

    Ole: 0 Posten, 0.00 Euro

    Ida: 4 Posten, 13.50 Euro

    '
starter_code: 'const idasPreise = [2.5, 4.5, 1.75, 4.75];

  '
---

Schreib `bon(kunde, ...preise)`, die alle übergebenen Preise zusammenzählt, und ruf sie mit unterschiedlich vielen Preisen auf, beim letzten Mal aus einem Array verteilt:

```
Pia: 3 Posten, 8.75 Euro
Ole: 0 Posten, 0.00 Euro
Ida: 4 Posten, 13.50 Euro
```
