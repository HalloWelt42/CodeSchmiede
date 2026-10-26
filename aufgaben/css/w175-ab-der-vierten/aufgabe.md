---
schema_version: 1
id: w175-ab-der-vierten
revision: 1
titel: Ab der Vierten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- nth-child
- muster
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n  <li>Dorsch</li>\n\
  \  <li>Scholle</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n\n.liste li:nth-child(n+4) {\n  opacity: 0.5;\n\
  }\n"
hints:
- kosten: 0
  text: 'Alle ab der vierten Stelle: n+4.'
- kosten: 2
  text: ".liste li:nth-child(n+4) {\n  opacity: 0.5;\n}"
starter_code: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n"
---

Nur die ersten drei Fische sind heute frisch. Alle ab dem vierten werden blass.

## Vorgaben

- `li` ab der vierten Stelle: Deckkraft `0.5`
