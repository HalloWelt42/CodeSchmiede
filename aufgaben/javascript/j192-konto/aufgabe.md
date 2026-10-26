---
schema_version: 1
id: j192-konto
revision: 1
titel: Das Konto als Klasse
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
tags:
- kurs
- klasse
- this
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In den Methoden immer `this.stand`.
tests_sichtbar:
- input: []
  expected: 'Stand: 15.00

    Abgelehnt: Zu wenig Geld

    Stand: 15.00

    '
starter_code: "class Konto {\n  constructor() {\n    this.stand = 0;\n  }\n}\nconst k = new Konto();\nk.einzahlen(20);\nk.abheben(5);\n\
  console.log(`Stand: ${k.stand.toFixed(2)}`);\ntry {\n  k.abheben(100);\n} catch (fehler) {\n  console.log(`Abgelehnt: ${fehler.message}`);\n\
  }\nconsole.log(`Stand: ${k.stand.toFixed(2)}`);\n"
---

Ergänze die Klasse `Konto` um `einzahlen(betrag)` und `abheben(betrag)`; abheben wirft einen Fehler `Zu wenig Geld`, wenn der Stand nicht reicht:

```
Stand: 15.00
Abgelehnt: Zu wenig Geld
Stand: 15.00
```
