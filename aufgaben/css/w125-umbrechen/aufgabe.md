---
schema_version: 1
id: w125-umbrechen
revision: 1
titel: Umbrechen erlaubt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- flex-wrap
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kacheln\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n  <div>Lachs</div>\n\
  \  <div>Scholle</div>\n</div>\n"
ziel_css: ".kacheln {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 10px;\n}\n\n.kacheln div {\n  width: 160px;\n  height:\
  \ 60px;\n  background-color: teal;\n  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: Die Kacheln werden gestaucht. Lass sie in die nächste Reihe umbrechen.
- kosten: 2
  text: 'flex-wrap: wrap;'
starter_code: ".kacheln {\n  display: flex;\n  gap: 10px;\n}\n\n.kacheln div {\n  width: 160px;\n  height: 60px;\n  background-color:\
  \ teal;\n  padding: 10px;\n}\n"
---

Fünf Kacheln passen nicht in eine Reihe und werden zusammengedrückt. Sie sollen ihre Breite behalten und umbrechen.

## Vorgaben

- Klasse `kacheln`: Umbrechen erlaubt
