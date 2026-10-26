---
schema_version: 1
id: w148-schachbrett
revision: 1
titel: Das Spielbrett
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"brett\">\n  <div class=\"kopf\">Fisch-Bingo</div>\n  <div class=\"felder\">\n    <div>Hering</div>\n\
  \    <div>Lachs</div>\n    <div>Dorsch</div>\n    <div>Scholle</div>\n    <div>Frei</div>\n    <div>Makrele</div>\n    <div>Sprotte</div>\n\
  \    <div>Aal</div>\n    <div>Barsch</div>\n  </div>\n</div>\n"
ziel_css: ".brett {\n  display: grid;\n  grid-template-rows: 50px 1fr;\n  gap: 8px;\n  width: 360px;\n  height: 340px;\n}\n\
  \n.kopf {\n  background-color: #ffd166;\n  color: #2b3442;\n  padding: 12px;\n}\n\n.felder {\n  display: grid;\n  grid-template-columns:\
  \ repeat(3, 1fr);\n  grid-template-rows: repeat(3, 1fr);\n  gap: 4px;\n}\n\n.felder div {\n  background-color: teal;\n \
  \ border: 1px solid #2b3442;\n  padding: 8px;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Raster: das Brett mit zwei Zeilen, die Felder mit drei mal drei gleichen Fächern.'
- kosten: 3
  text: 'Das Brett: grid-template-rows 50px 1fr. Die Felder: repeat(3, 1fr) für Spalten und Zeilen.'
starter_code: '/* Fisch-Bingo */

  '
---

Alles aus dem Kapitel: ein Spielbrett für Fisch-Bingo.

## Vorgaben

- Klasse `brett`: Raster mit den Zeilen `50px 1fr`, Lücke `8px`, Breite `360px`, Höhe `340px`
- Klasse `kopf`: Hintergrund `#ffd166`, Schrift `#2b3442`, Polster `12px`
- Klasse `felder`: Raster mit drei gleichen Spalten und drei gleichen Zeilen, Lücke `4px`
- Felder (`.felder div`): Hintergrund `teal`, Rand `1px solid #2b3442`, Polster `8px`
