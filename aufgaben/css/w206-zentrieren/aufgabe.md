---
schema_version: 1
id: w206-zentrieren
revision: 1
titel: Genau in die Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- translate
- position
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"buehne\">\n  <div class=\"fisch\">Fang des Tages</div>\n</div>\n"
ziel_css: ".buehne {\n  position: relative;\n  width: 360px;\n  height: 220px;\n  background-color: #2b3442;\n}\n\n.fisch\
  \ {\n  position: absolute;\n  top: 50%;\n  left: 50%;\n  transform: translate(-50%, -50%);\n  padding: 24px 36px;\n  font-size:\
  \ 20px;\n  background-color: gold;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: top und left setzen die linke obere Ecke in die Mitte. Schieb das Element um die halbe eigene Größe zurück.
- kosten: 2
  text: 'transform: translate(-50%, -50%);'
starter_code: ".buehne {\n  position: relative;\n  width: 360px;\n  height: 220px;\n  background-color: #2b3442;\n}\n\n.fisch\
  \ {\n  position: absolute;\n  top: 50%;\n  left: 50%;\n  padding: 24px 36px;\n  font-size: 20px;\n  background-color: gold;\n\
  \  color: #2b3442;\n}\n"
---

Der Fang des Tages soll genau in der Mitte liegen. top und left 50% setzen aber nur seine linke obere Ecke dorthin. Der alte Trick: um die halbe eigene Größe zurückschieben.

## Vorgaben

- Klasse `fisch`: Verschiebung `translate(-50%, -50%)`
