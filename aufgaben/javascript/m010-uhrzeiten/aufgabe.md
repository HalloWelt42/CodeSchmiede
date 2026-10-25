---
schema_version: 1
id: m010-uhrzeiten
revision: 1
titel: Uhrzeiten
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: mittel
schwierigkeit_score: 9
schaetz_minuten: 8
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Stunden bis 19 beginnen mit 0 oder 1, ab 20 mit 2 und dann nur 0 bis 3."}
muster:
  treffer: ["um 09:30 Uhr", "23:59", "Start 00:00", "14:05 bis 15:45"]
  nieten: ["24:00", "9:30", "12:60", "Zeit 1230", "25:10"]
  treffer_versteckt: ["(07:15)", "20:00 Abendessen"]
  nieten_versteckt: ["125:10", "12:345", "29:00"]
  sterne: {zwei: 32, drei: 27}
  spickzettel:
    - ["[01]", "0 oder 1"]
    - ["[0-3]", "0 bis 3"]
    - ["(a|b)", "a oder b als Gruppe"]
    - ["\\b", "Wortgrenze"]
---

# Uhrzeiten

Fang gültige Uhrzeiten im Format **HH:MM** von 00:00 bis 23:59, mit zweistelliger Stunde. Was keine gültige Uhrzeit ist oder Teil einer längeren Zahl, ist eine Niete.
