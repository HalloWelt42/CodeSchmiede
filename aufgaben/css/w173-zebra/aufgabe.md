---
schema_version: 1
id: w173-zebra
revision: 1
titel: Zebrastreifen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- nth-child
- even
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n  <li>Dorsch</li>\n\
  \  <li>Scholle</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n\n.liste li:nth-child(even) {\n  background-color:\
  \ #2b3442;\n}\n"
hints:
- kosten: 0
  text: Jede zweite Zeile, also die geraden Stellen.
- kosten: 2
  text: .liste li:nth-child(even) {
starter_code: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n"
---

Damit niemand in der Zeile verrutscht, bekommt jede gerade Zeile einen dunkleren Hintergrund.

## Vorgaben

- `li` an geraden Stellen: Hintergrund `#2b3442`
