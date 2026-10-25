---
schema_version: 1
id: m007-ganze-zeile
revision: 1
titel: Nur eine Zahl
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: mittel
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
muster:
  treffer: ["42", "0", "2026", "1234567"]
  nieten: ["42 Äpfel", "Nr. 7", "3.14", "-5", " 12"]
  treffer_versteckt: ["99", "000"]
  nieten_versteckt: ["12a", "1 2"]
  sterne: {zwei: 9, drei: 5}
  spickzettel:
    - ["^ $", "Anfang und Ende der Zeile"]
    - ["+", "einmal oder öfter"]
---

# Nur eine Zahl

Fang die Zeilen, die aus nichts als einer Zahl bestehen: nur Ziffern, mindestens eine, sonst nichts, auch kein Leerzeichen.
