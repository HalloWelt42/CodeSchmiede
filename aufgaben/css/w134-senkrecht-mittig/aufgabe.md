---
schema_version: 1
id: w134-senkrecht-mittig
revision: 1
titel: Senkrecht in die Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- align-items
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"theke\">\n  <div class=\"kasse\">Kasse</div>\n  <div class=\"fisch\">Fisch</div>\n  <div>Brot</div>\n\
  </div>\n"
ziel_css: ".theke {\n  display: flex;\n  gap: 8px;\n  height: 160px;\n  align-items: center;\n  background-color: #2b3442;\n\
  }\n\n.theke div {\n  background-color: teal;\n  padding: 10px;\n}\n\n.kasse {\n  height: 100px;\n}\n"
hints:
- kosten: 0
  text: Quer zur Reihe ausrichten, beim Behälter.
- kosten: 2
  text: 'align-items: center;'
starter_code: ".theke {\n  display: flex;\n  gap: 8px;\n  height: 160px;\n  background-color: #2b3442;\n}\n\n.theke div {\n\
  \  background-color: teal;\n  padding: 10px;\n}\n\n.kasse {\n  height: 100px;\n}\n"
---

Alle Kästen werden auf die volle Höhe gestreckt. Sie sollen ihre Höhe behalten und senkrecht in der Mitte stehen.

## Vorgaben

- Klasse `theke`: `align-items: center`
