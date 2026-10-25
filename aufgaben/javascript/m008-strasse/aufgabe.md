---
schema_version: 1
id: m008-strasse
revision: 1
titel: Straße oder Strasse
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
  notiz: Muster-Jagd, Level 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["Hauptstraße 5", "Bahnhofstrasse 12", "Straße der Einheit", "STRASSE GESPERRT"]
  nieten: ["Strase 3", "Strand", "Strauß", "Strassburg"]
  treffer_versteckt: ["Lange Straße", "Seestrasse"]
  nieten_versteckt: ["Strecke", "Strasburg"]
  flags: i
  sterne: {zwei: 14, drei: 11}
  spickzettel:
    - ["(ß|ss)", "ß oder ss"]
    - ["?", "das Zeichen davor darf fehlen"]
---

# Straße oder Strasse

Fang die Zeilen mit dem Wort Straße, egal ob mit ß oder mit ss geschrieben, auch als Teil eines Namens. Groß- und Kleinschreibung zählt nicht (Flag `i`). Tippfehler und ähnliche Wörter sind Nieten.
