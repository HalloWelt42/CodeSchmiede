---
schema_version: 1
id: j183-objekt-auspacken
revision: 1
titel: Das Gericht auspacken
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
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
  text: '`function zeile({ name, preis, scharf = false })`'
tests_sichtbar:
- input: []
  expected: 'Fischsuppe: 4.50 Euro (scharf)

    Heringsbrötchen: 2.50 Euro

    '
starter_code: 'const suppe = { name: "Fischsuppe", preis: 4.5, scharf: true };

  const broetchen = { name: "Heringsbrötchen", preis: 2.5 };

  '
---

Schreib `zeile(gericht)`, die ihren Parameter gleich auspackt: `name`, `preis` und `scharf` mit Standardwert false. Sie liefert `Name: Preis Euro`, bei scharfen Gerichten mit ` (scharf)`. Für die beiden Gerichte im Startcode:

```
Fischsuppe: 4.50 Euro (scharf)
Heringsbrötchen: 2.50 Euro
```
