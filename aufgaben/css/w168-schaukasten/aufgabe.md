---
schema_version: 1
id: w168-schaukasten
revision: 1
titel: Der Schaukasten
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
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kasten\">\n  <p>Fang des Tages: Riesenhering</p>\n  <span class=\"preis\">9,90</span>\n  <span class=\"\
  stempel\">Rekord!</span>\n  <div class=\"glas\"></div>\n</div>\n"
ziel_css: ".kasten {\n  position: relative;\n  width: 320px;\n  height: 180px;\n  margin: 30px auto;\n  padding: 10px;\n \
  \ background-color: #2b3442;\n}\n\n.preis {\n  position: absolute;\n  bottom: 10px;\n  right: 10px;\n  font-size: 24px;\n\
  \  color: gold;\n}\n\n.stempel {\n  position: absolute;\n  top: -16px;\n  left: -16px;\n  z-index: 2;\n  padding: 6px 10px;\n\
  \  background-color: crimson;\n  border-radius: 999px;\n}\n\n.glas {\n  position: absolute;\n  inset: 0;\n  background:\
  \ linear-gradient(to bottom right, rgb(255 255 255 / 0.25), transparent);\n}\n"
hints:
- kosten: 0
  text: Der Kasten ist der Bezugsrahmen. Preis unten rechts, Stempel über die obere linke Ecke, das Glas als Schleier über
    allem außer dem Stempel.
- kosten: 3
  text: Das Glas mit inset 0; der Stempel braucht z-index 2, sonst liegt das Glas über ihm.
starter_code: '/* Der Schaukasten */

  '
---

Alles aus dem Kapitel in einem Schaukasten.

## Vorgaben

- Klasse `kasten`: Bezugsrahmen (`position: relative`), Breite `320px`, Höhe `180px`, Außenabstand `30px auto`, Polster `10px`, Hintergrund `#2b3442`
- Klasse `preis`: absolut, `bottom: 10px`, `right: 10px`, Schrift `24px`, `gold`
- Klasse `stempel`: absolut, `top: -16px`, `left: -16px`, `z-index: 2`, Polster `6px 10px`, Hintergrund `crimson`, Eckenradius `999px`
- Klasse `glas`: absolut, `inset: 0`, Hintergrund Verlauf nach rechts unten von `rgb(255 255 255 / 0.25)` zu `transparent`
