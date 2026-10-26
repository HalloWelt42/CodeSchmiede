---
schema_version: 1
id: j156-finden
revision: 1
titel: Gesucht und gefunden
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- rueckrufmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: find liefert das ganze Objekt; den Namen holt `.name`.
tests_sichtbar:
- input: []
  expected: 'Erstes unter 3 Euro: Heringsbrötchen

    Etwas über 8 Euro: false

    Alles unter 10 Euro: true

    '
starter_code: "const karte = [\n  { name: \"Fischsuppe\", preis: 4.5 },\n  { name: \"Heringsbrötchen\", preis: 2.5 },\n  {\
  \ name: \"Limonade\", preis: 1.75 },\n];\n"
---

Beantworte mit `find`, `some` und `every` drei Fragen zur Speisekarte:

```
Erstes unter 3 Euro: Heringsbrötchen
Etwas über 8 Euro: false
Alles unter 10 Euro: true
```
