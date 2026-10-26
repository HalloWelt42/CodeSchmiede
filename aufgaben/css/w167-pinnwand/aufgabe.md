---
schema_version: 1
id: w167-pinnwand
revision: 1
titel: Zettel an der Pinnwand
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- position
- absolute
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"wand\">\n  <div class=\"zettel eins\">Einkaufen</div>\n  <div class=\"zettel zwei\">Eis bestellen</div>\n\
  \  <div class=\"zettel drei\">Pia anrufen</div>\n</div>\n"
ziel_css: ".wand {\n  position: relative;\n  height: 300px;\n  background-color: #c98c55;\n}\n\n.zettel {\n  position: absolute;\n\
  \  width: 130px;\n  padding: 12px;\n  background-color: #fff6c2;\n  color: #2b3442;\n  box-shadow: 2px 4px 6px rgb(0 0 0\
  \ / 0.4);\n}\n\n.eins { top: 20px; left: 20px; }\n.zwei { top: 60px; left: 200px; }\n.drei { top: 170px; left: 100px; }\n"
hints:
- kosten: 0
  text: Alle Zettel werden absolut positioniert, dann bekommt jeder seine Lage.
- kosten: 3
  text: .zettel mit position absolute; .eins top 20px left 20px, .zwei top 60px left 200px, .drei top 170px left 100px
starter_code: ".wand {\n  position: relative;\n  height: 300px;\n  background-color: #c98c55;\n}\n\n.zettel {\n  width: 130px;\n\
  \  padding: 12px;\n  background-color: #fff6c2;\n  color: #2b3442;\n  box-shadow: 2px 4px 6px rgb(0 0 0 / 0.4);\n}\n"
---

Pit pinnt drei Zettel kreuz und quer an die Wand.

## Vorgaben

- Klasse `zettel`: `position: absolute`
- `.eins`: `top: 20px`, `left: 20px`
- `.zwei`: `top: 60px`, `left: 200px`
- `.drei`: `top: 170px`, `left: 100px`
