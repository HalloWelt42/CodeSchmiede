---
schema_version: 1
id: w142-anteile
revision: 1
titel: Eins zu zwei
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
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
ziel_html: "<div class=\"seite\">\n  <div class=\"menue\">Menü</div>\n  <div class=\"inhalt\">Inhalt</div>\n</div>\n"
ziel_css: ".seite {\n  display: grid;\n  grid-template-columns: 1fr 2fr;\n  height: 200px;\n}\n\n.menue {\n  background-color:\
  \ #2b3442;\n}\n\n.inhalt {\n  background-color: #fbf4e2;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Der Inhalt bekommt doppelt so viel wie das Menü.
- kosten: 2
  text: 'grid-template-columns: 1fr 2fr;'
starter_code: ".seite {\n  display: grid;\n  grid-template-columns: 1fr 1fr;\n  height: 200px;\n}\n\n.menue {\n  background-color:\
  \ #2b3442;\n}\n\n.inhalt {\n  background-color: #fbf4e2;\n  color: #2b3442;\n}\n"
---

Menü und Inhalt sind gleich breit. Der Inhalt soll doppelt so viel Platz bekommen.

## Vorgaben

- Klasse `seite`: Spalten `1fr 2fr`
