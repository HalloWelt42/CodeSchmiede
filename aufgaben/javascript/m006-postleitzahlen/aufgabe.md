---
schema_version: 1
id: m006-postleitzahlen
revision: 1
titel: Postleitzahlen
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: mittel
schwierigkeit_score: 7
schaetz_minuten: 5
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["70173 Stuttgart", "PLZ: 10115", "D-80331 München", "01067"]
  nieten: ["Tel. 0711123456", "1234 Leute", "Nr. 123456", "70 173"]
  treffer_versteckt: ["(20095)", "Postfach 99999"]
  nieten_versteckt: ["2026-01-15", "12.345"]
  sterne: {zwei: 13, drei: 9}
  spickzettel:
    - ["{5}", "genau fünfmal"]
    - ["\\b", "Wortgrenze: Übergang zwischen Ziffer oder Buchstabe und etwas anderem"]
---

# Postleitzahlen

Fang deutsche Postleitzahlen: genau fünf Ziffern am Stück, nicht Teil einer längeren Zahl.
