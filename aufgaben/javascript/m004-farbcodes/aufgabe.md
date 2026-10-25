---
schema_version: 1
id: m004-farbcodes
revision: 1
titel: Farbcodes
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 1, text: "Nach der sechsten Hexziffer darf keine weitere folgen."}
muster:
  treffer: ["Farbe #1a2b3c", "#FFAA00", "#00ff7f ist grün"]
  nieten: ["#12345", "#ggg000", "1a2b3c", "#1234567", "#12 34 56"]
  treffer_versteckt: ["#abcdef;", "Rand: #000000"]
  nieten_versteckt: ["#abcdeg", "#12345z"]
  flags: i
  sterne: {zwei: 18, drei: 13}
  spickzettel:
    - ["[a-f]", "ein Buchstabe von a bis f"]
    - ["[\\da-f]", "Ziffer oder a bis f"]
    - ["{6}", "genau sechsmal"]
    - ["\\b", "Wortgrenze"]
---

# Farbcodes

Fang Farbcodes wie in CSS: ein `#` und genau sechs Hexziffern (0 bis 9 und a bis f). Groß- und Kleinschreibung zählt hier nicht, das Level prüft mit dem Flag `i`.
