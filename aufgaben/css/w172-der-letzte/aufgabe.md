---
schema_version: 1
id: w172-der-letzte
revision: 1
titel: Der Letzte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- last-child
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n  <li>Dorsch</li>\n\
  \  <li>Scholle</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n\n.liste li:last-child {\n  background-color: #444;\n\
  \  color: gray;\n  text-decoration: line-through;\n}\n"
hints:
- kosten: 0
  text: Das letzte Kind der Liste.
- kosten: 2
  text: .liste li:last-child {
starter_code: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n"
---

Der letzte Fisch ist ausverkauft: grau und durchgestrichen.

## Vorgaben

- das letzte `li` der Liste: Hintergrund `#444`, Schrift `gray`, durchgestrichen
