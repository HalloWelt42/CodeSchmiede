---
schema_version: 1
id: m001-ziffern
revision: 1
titel: Zeilen mit Zahlen
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["Raum 12", "3 Äpfel", "Bus 7 kommt", "2026"]
  nieten: ["zwölf", "drei Äpfel", "Bus kommt gleich", "ohne Zahl"]
  treffer_versteckt: ["Zimmer 9", "x1"]
  nieten_versteckt: ["neun Leben", "Text"]
  sterne: {zwei: 5, drei: 2}
  spickzettel:
    - ["\\d", "eine Ziffer, 0 bis 9"]
    - ["[0-9]", "dasselbe als Zeichenklasse"]
---

# Zeilen mit Zahlen

Fang jede Zeile, in der mindestens eine Ziffer steht. Zahlwörter zählen nicht.
