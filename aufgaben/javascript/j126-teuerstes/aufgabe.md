---
schema_version: 1
id: j126-teuerstes
revision: 1
titel: Das teuerste Gericht
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- objekt
- array
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Merk dir das ganze Objekt des bisher teuersten, nicht nur den Preis.
tests_sichtbar:
- input: []
  expected: 'Am teuersten: Fischplatte für 9.90 Euro

    '
starter_code: "const karte = [\n  { name: \"Heringsbrötchen\", preis: 2.5 },\n  { name: \"Fischplatte\", preis: 9.9 },\n \
  \ { name: \"Fischsuppe\", preis: 4.5 },\n];\n"
---

Finde in der Speisekarte (ein Array aus Objekten) das teuerste Gericht:

```
Am teuersten: Fischplatte für 9.90 Euro
```
