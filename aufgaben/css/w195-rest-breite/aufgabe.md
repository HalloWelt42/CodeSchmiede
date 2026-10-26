---
schema_version: 1
id: w195-rest-breite
revision: 1
titel: Der Rest der Breite
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- calc
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"leiste\">\n  <div class=\"logo\">Fisch</div>\n  <div class=\"rest\">Alles andere</div>\n</div>\n"
ziel_css: ".logo, .rest {\n  display: inline-block;\n  padding: 10px 0;\n}\n\n.logo {\n  width: 100px;\n  background-color:\
  \ teal;\n}\n\n.rest {\n  width: calc(100% - 110px);\n  background-color: #ffd166;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Die volle Breite minus 110 Pixel, mit Leerzeichen um das Minus.
- kosten: 2
  text: 'width: calc(100% - 110px);'
starter_code: ".logo, .rest {\n  display: inline-block;\n  padding: 10px 0;\n}\n\n.logo {\n  width: 100px;\n  background-color:\
  \ teal;\n}\n\n.rest {\n  width: 100px;\n  background-color: #ffd166;\n  color: #2b3442;\n}\n"
---

Neben dem Logo soll der zweite Kasten die ganze restliche Breite nehmen, bis auf eine kleine Lücke.

## Vorgaben

- `.rest`: Breite `calc(100% - 110px)`
