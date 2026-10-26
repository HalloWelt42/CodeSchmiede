---
schema_version: 1
id: j166-gedaechtnis
revision: 1
titel: Ein Gedächtnis für Rechnungen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- sichtbarkeit
- closure
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Map steht in mitGedaechtnis und überlebt dort zwischen den Aufrufen.
- kosten: 2
  text: Am Ende steht die letzte Frage noch in einer eigenen Zeile, weil danach nichts mehr kommt.
tests_sichtbar:
- input:
  - '3'
  - '4'
  - '3'
  expected: "Zahl? 9\nZahl? 16\nZahl? 9 (gemerkt)\nZahl? \n"
tests_versteckt:
- input:
  - '5'
  - '5'
  - '5'
  expected: "Zahl? 25\nZahl? 25 (gemerkt)\nZahl? 25 (gemerkt)\nZahl? \n"
starter_code: "function teuer(n) {\n  return n * n;\n}\n"
---

`teuer(n)` rechnet lange. Schreib `mitGedaechtnis(f)`, die eine Funktion liefert, die sich Ergebnisse in einer Map merkt und bei schon bekannten Werten `(gemerkt)` anhängt. Lies Zahlen, bis keine mehr kommt. Bei den Eingaben `3`, `4` und `3`:

```
Zahl? 9
Zahl? 16
Zahl? 9 (gemerkt)
Zahl? 
```
