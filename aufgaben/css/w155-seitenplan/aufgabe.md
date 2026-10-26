---
schema_version: 1
id: w155-seitenplan
revision: 1
titel: Der Seitenplan
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- grid-template-areas
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"seite\">\n  <div class=\"a\">Kopf</div>\n  <div class=\"b\">Menü</div>\n  <div class=\"c\">Inhalt</div>\n\
  \  <div class=\"d\">Fuß</div>\n</div>\n"
ziel_css: ".seite {\n  display: grid;\n  grid-template-columns: 140px 1fr;\n  grid-template-rows: 60px 180px 40px;\n  grid-template-areas:\n\
  \    \"kopf kopf\"\n    \"menue inhalt\"\n    \"fuss fuss\";\n  gap: 4px;\n}\n\n.seite div {\n  background-color: teal;\n\
  \  padding: 8px;\n}\n\n.a { grid-area: kopf; }\n.b { grid-area: menue; }\n.c { grid-area: inhalt; }\n.d { grid-area: fuss;\
  \ }\n"
hints:
- kosten: 0
  text: Die Kinder kennen ihre Bereiche schon. Es fehlt der Plan beim Behälter.
- kosten: 3
  text: 'grid-template-areas mit drei Texten: "kopf kopf", "menue inhalt", "fuss fuss"'
starter_code: ".seite {\n  display: grid;\n  grid-template-columns: 140px 1fr;\n  grid-template-rows: 60px 180px 40px;\n \
  \ gap: 4px;\n}\n\n.seite div {\n  background-color: teal;\n  padding: 8px;\n}\n\n.a { grid-area: kopf; }\n.b { grid-area:\
  \ menue; }\n.c { grid-area: inhalt; }\n.d { grid-area: fuss; }\n"
---

Die Kinder haben ihre Bereiche schon, aber der Plan fehlt. Zeichne ihn: Kopf und Fuß über die ganze Breite, dazwischen Menü links und Inhalt rechts.

## Vorgaben

- Klasse `seite`: Plan `"kopf kopf" "menue inhalt" "fuss fuss"`
