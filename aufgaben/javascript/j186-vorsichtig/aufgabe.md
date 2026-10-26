---
schema_version: 1
id: j186-vorsichtig
revision: 1
titel: Vorsichtig nachsehen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- optional
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`karte?.stempel` liefert bei fehlender Karte undefined.'
- kosten: 2
  text: Mit `||` würde Ida auch keine Karte bekommen; `??` lässt die 0 stehen.
tests_sichtbar:
- input: []
  expected: 'Pia: 3

    Ole: keine Karte

    Ida: 0

    '
starter_code: "const kunden = [\n  { name: \"Pia\", karte: { stempel: 3 } },\n  { name: \"Ole\" },\n  { name: \"Ida\", karte:\
  \ { stempel: 0 } },\n];\n"
---

Nicht jeder Kunde hat eine Karte, und manche Karten haben 0 Stempel. Gib für jeden den Stand aus, mit `?.` und `??`, sodass fehlende Karten `keine Karte` ergeben, 0 Stempel aber 0 bleiben:

```
Pia: 3
Ole: keine Karte
Ida: 0
```
