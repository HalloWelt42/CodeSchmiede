---
schema_version: 1
id: j195-static
revision: 1
titel: Zählen über alle
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- klasse
- getter
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im constructor `Fisch.anzahl++`, nicht `this.anzahl`.
tests_sichtbar:
- input: []
  expected: 'Gebaut: 3 Fische

    '
starter_code: "class Fisch {\n  constructor(art) {\n    this.art = art;\n  }\n}\nnew Fisch(\"Hering\");\nnew Fisch(\"Aal\"\
  );\nnew Fisch(\"Butt\");\nconsole.log(Fisch.bericht());\n"
---

Die Klasse `Fisch` soll mitzählen, wie viele Fische insgesamt gebaut wurden. Leg dafür eine statische Eigenschaft `static anzahl = 0;` an, zähl sie im constructor hoch und gib sie über `Fisch.anzahl` aus. Dazu eine statische Methode `Fisch.bericht()`:

```
Gebaut: 3 Fische
```
