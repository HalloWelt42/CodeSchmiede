---
schema_version: 1
id: w108-plakat-fest
revision: 1
titel: Plakat zum Fischfest
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"plakat\">\n  <h1>Fischfest</h1>\n  <p class=\"knopf\">Hingehen!</p>\n</div>\n"
ziel_css: ".plakat {\n  width: 320px;\n  margin: 20px auto;\n  padding: 20px;\n  text-align: center;\n  border-radius: 16px;\n\
  \  background: linear-gradient(to bottom right, #0b4f8a, #2b1a4a);\n  box-shadow: 0 10px 24px black;\n}\n\nh1 {\n  color:\
  \ gold;\n  text-shadow: 3px 3px 0 crimson;\n}\n\n.knopf {\n  padding: 10px;\n  border-radius: 999px;\n  background: radial-gradient(gold,\
  \ orange);\n  color: #2b3442;\n  box-shadow: inset 0 -3px 0 crimson;\n}\n"
hints:
- kosten: 0
  text: Drei Regeln. Das Plakat bekommt einen schrägen Verlauf und einen Schatten, die Überschrift eine harte rote Kante,
    der Knopf einen runden Verlauf und einen inneren Schatten unten.
- kosten: 3
  text: to bottom right ist die schräge Richtung. inset 0 -3px 0 crimson zeichnet innen unten eine Kante.
starter_code: '/* Plakat zum Fischfest */

  '
---

Alles aus dem Kapitel auf einem Plakat.

## Vorgaben

- Klasse `plakat`: Breite `320px`, Außenabstand `20px auto`, Polster `20px`, mittig, Eckenradius `16px`, Verlauf nach rechts unten von `#0b4f8a` zu `#2b1a4a`, Schatten `0 10px 24px black`
- `h1`: Schrift `gold`, Textschatten `3px 3px 0 crimson`
- Klasse `knopf`: Polster `10px`, Eckenradius `999px`, runder Verlauf `gold` zu `orange`, Schrift `#2b3442`, innerer Schatten `0 -3px 0 crimson`
