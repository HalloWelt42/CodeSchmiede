---
schema_version: 1
id: w177-trennlinien
revision: 1
titel: Linien dazwischen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- not
- last-child
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"karte\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n</ul>\n"
ziel_css: ".karte {\n  width: 240px;\n  padding: 0;\n  background-color: #2b3442;\n}\n\n.karte li {\n  padding: 8px;\n}\n\n\
  .karte li:not(:last-child) {\n  border-bottom: 3px dotted gold;\n}\n"
hints:
- kosten: 0
  text: Eine Linie unter jedem Eintrag, außer unter dem letzten.
- kosten: 2
  text: ".karte li:not(:last-child) {\n  border-bottom: 3px dotted gold;\n}"
starter_code: ".karte {\n  width: 240px;\n  padding: 0;\n  background-color: #2b3442;\n}\n\n.karte li {\n  padding: 8px;\n\
  }\n"
---

Zwischen die Einträge der Karte kommen gepunktete goldene Linien, aber nicht unter den letzten.

## Vorgaben

- alle `li` außer dem letzten: Rand unten `3px dotted gold`
