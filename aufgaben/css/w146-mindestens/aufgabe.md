---
schema_version: 1
id: w146-mindestens
revision: 1
titel: Mindestens so breit
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- minmax
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"spalten\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ".spalten {\n  display: grid;\n  grid-template-columns: minmax(250px, 1fr) 1fr 1fr;\n  gap: 6px;\n}\n\n.spalten\
  \ div {\n  background-color: teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 80px;\n}\n"
hints:
- kosten: 0
  text: Die erste Spalte soll mindestens 250 Pixel breit sein, darf aber auch wachsen.
- kosten: 2
  text: 'grid-template-columns: minmax(250px, 1fr) 1fr 1fr;'
starter_code: ".spalten {\n  display: grid;\n  grid-template-columns: 1fr 1fr 1fr;\n  gap: 6px;\n}\n\n.spalten div {\n  background-color:\
  \ teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 80px;\n}\n"
---

Die erste Spalte ist für den Tagesfisch und soll mindestens 250 Pixel breit sein. Die anderen teilen sich den Rest.

## Vorgaben

- Klasse `spalten`: Spalten `minmax(250px, 1fr) 1fr 1fr`
