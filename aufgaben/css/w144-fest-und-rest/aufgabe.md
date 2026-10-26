---
schema_version: 1
id: w144-fest-und-rest
revision: 1
titel: Fest und Rest
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- fr
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"zeile\">\n  <div>Bild</div>\n  <div>Beschreibung des Fischs</div>\n  <div>4,50</div>\n</div>\n"
ziel_css: ".zeile {\n  display: grid;\n  grid-template-columns: 80px 1fr 60px;\n}\n\n.zeile div {\n  background-color: teal;\n\
  \  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 60px;\n}\n"
hints:
- kosten: 0
  text: Zwei feste Spalten außen, eine mit dem ganzen Rest in der Mitte.
- kosten: 2
  text: 'grid-template-columns: 80px 1fr 60px;'
starter_code: ".zeile div {\n  background-color: teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 60px;\n}\n"
---

Eine Zeile der Karte: links ein Bild mit fester Breite, rechts der Preis mit fester Breite, dazwischen die Beschreibung mit allem, was übrig bleibt.

## Vorgaben

- Klasse `zeile`: Raster mit den Spalten `80px 1fr 60px`
