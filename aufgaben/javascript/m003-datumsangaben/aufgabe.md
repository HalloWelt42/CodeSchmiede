---
schema_version: 1
id: m003-datumsangaben
revision: 1
titel: Datumsangaben
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
  notiz: Muster-Jagd, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 1, text: "Ein Monat beginnt immer mit 0 oder 1."}
muster:
  treffer: ["Termin am 24.10.2026", "01.01.2000", "Geboren 31.12.1999 in Ulm", "bis 07.03.2027", "Am 15.08.2026 und 16.08.2026"]
  nieten: ["2026-10-24", "24/10/2026", "1.1.2000", "Version 12.34.5678.9", "Telefon 0711.12.3456"]
  treffer_versteckt: ["Frist: 30.06.2026.", "(01.09.2025)"]
  nieten_versteckt: ["Zeit 12.30 Uhr", "Kurs 99.25.2026", "2026.10.24"]
  sterne: {zwei: 26, drei: 21}
  spickzettel:
    - ["\\d", "eine Ziffer"]
    - ["{4}", "genau viermal"]
    - ["\\.", "ein echter Punkt"]
    - ["[01]", "eine 0 oder eine 1"]
    - ["\\b", "Wortgrenze: davor keine Ziffer und kein Buchstabe"]
---

# Datumsangaben

Fang alle Datumsangaben in der deutschen Schreibweise **Tag.Monat.Jahr** mit zweistelligem Tag und Monat und vierstelligem Jahr. Daten in anderer Schreibweise und Zahlen, die nur so ähnlich aussehen, sind Nieten.
