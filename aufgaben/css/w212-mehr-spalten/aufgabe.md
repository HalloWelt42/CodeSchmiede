---
schema_version: 1
id: w212-mehr-spalten
revision: 1
titel: Mehr Spalten, wenn Platz ist
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- media
- mobile-first
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kacheln\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n  <div>Lachs</div>\n\
  </div>\n"
ziel_css: ".kacheln {\n  display: grid;\n  gap: 6px;\n}\n\n.kacheln div {\n  padding: 14px;\n  background-color: teal;\n}\n\
  \n@media (min-width: 500px) {\n  .kacheln {\n    grid-template-columns: repeat(4, 1fr);\n  }\n}\n"
hints:
- kosten: 0
  text: 'Grundgerüst: alles untereinander. Ab 500 Pixeln Breite vier Spalten.'
- kosten: 2
  text: "@media (min-width: 500px) {\n  .kacheln {\n    grid-template-columns: repeat(4, 1fr);\n  }\n}"
starter_code: ".kacheln {\n  display: grid;\n  gap: 6px;\n}\n\n.kacheln div {\n  padding: 14px;\n  background-color: teal;\n\
  }\n"
---

Die Kacheln stehen untereinander, so wie es auf einem Telefon sein soll. Ab 500 Pixeln Breite sollen sie in vier Spalten nebeneinander stehen.

## Vorgaben

- ab `min-width: 500px`: `.kacheln` mit vier gleichen Spalten
