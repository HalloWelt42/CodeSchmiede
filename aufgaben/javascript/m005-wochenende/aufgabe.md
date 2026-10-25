---
schema_version: 1
id: m005-wochenende
revision: 1
titel: Wochenende
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["Am Samstag frei", "Sonntag ist Ruhetag", "Samstag und Sonntag", "bis Sonntag"]
  nieten: ["Montag", "Sommertag", "Saal am Freitag", "samstags geschlossen"]
  treffer_versteckt: ["Samstag", "Treffen: Sonntag 10 Uhr"]
  nieten_versteckt: ["Dienstag", "Sonnentag"]
  sterne: {zwei: 16, drei: 14}
  spickzettel:
    - ["a|b", "a oder b"]
    - ["(...)", "Gruppe: die Wahl gilt nur darin"]
---

# Wochenende

Fang die Zeilen, in denen **Samstag** oder **Sonntag** steht, groß geschrieben.
