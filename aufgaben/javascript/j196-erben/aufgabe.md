---
schema_version: 1
id: j196-erben
revision: 1
titel: Die Suppe erbt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- klasse
- extends
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im constructor zuerst `super(name, preis)`.
- kosten: 2
  text: '`super.zeile()` liefert die Zeile des Gerichts.'
tests_sichtbar:
- input: []
  expected: 'Heringsbrötchen: 2.50 Euro

    Fischsuppe: 4.50 Euro (scharf)

    Kartoffelsuppe: 3.90 Euro

    '
starter_code: "class Gericht {\n  constructor(name, preis) {\n    this.name = name;\n    this.preis = preis;\n  }\n  zeile()\
  \ {\n    return `${this.name}: ${this.preis.toFixed(2)} Euro`;\n  }\n}\n"
---

Schreib `class Suppe extends Gericht` mit der zusätzlichen Eigenschaft `scharf` und einer eigenen `zeile()`, die die Zeile des Gerichts nimmt und bei scharfen Suppen `(scharf)` anhängt. Alle Gerichte kommen in ein Array:

```
Heringsbrötchen: 2.50 Euro
Fischsuppe: 4.50 Euro (scharf)
Kartoffelsuppe: 3.90 Euro
```
