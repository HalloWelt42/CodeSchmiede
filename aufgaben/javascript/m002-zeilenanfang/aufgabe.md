---
schema_version: 1
id: m002-zeilenanfang
revision: 1
titel: Fehler am Zeilenanfang
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["Fehler: Datei fehlt", "Fehler 404", "Fehlermeldung folgt"]
  nieten: ["Kein Fehler", "Warnung: Fehler möglich", " Fehler nach Leerzeichen", "fehler klein"]
  treffer_versteckt: ["Fehler", "Fehlerfrei? Nein"]
  nieten_versteckt: ["Ein Fehler", "FEHLER"]
  sterne: {zwei: 10, drei: 7}
  spickzettel:
    - ["^", "Anfang der Zeile"]
    - ["$", "Ende der Zeile"]
---

# Fehler am Zeilenanfang

Fang die Zeilen eines Protokolls, die mit dem Wort **Fehler** beginnen. Steht es weiter hinten oder klein geschrieben, ist die Zeile eine Niete.
