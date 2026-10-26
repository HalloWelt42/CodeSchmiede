---
schema_version: 1
id: w078-ausweis
revision: 1
titel: Der Pinguin-Ausweis
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
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"ausweis\">\n  <h2>Pinguin-Ausweis</h2>\n  <p>Name: Pit</p>\n  <p>Beruf: Fischbrater</p>\n</div>\n"
ziel_css: "* {\n  box-sizing: border-box;\n}\n\n.ausweis {\n  width: 320px;\n  margin: 30px auto;\n  padding: 16px 24px;\n\
  \  border: 6px solid #ec6aa8;\n  background-color: #fbf4e2;\n  color: #2b3442;\n}\n\n.ausweis h2 {\n  margin: 0 0 12px;\n\
  }\n\n.ausweis p {\n  margin: 4px 0;\n}\n"
hints:
- kosten: 0
  text: Erst box-sizing für alle, dann der Ausweis selbst, dann die Abstände der Überschrift und der Absätze darin.
- kosten: 3
  text: 'margin mit drei Werten: oben, links und rechts, unten. margin: 0 0 12px heißt oben 0, seitlich 0, unten 12.'
starter_code: '/* Der Ausweis */

  '
---

Alles aus dem Kapitel: ein Ausweis mit Rand, Polster, fester Breite in der Mitte.

## Vorgaben

- alle Elemente: `box-sizing: border-box`
- Klasse `ausweis`: Breite `320px`, Außenabstand `30px auto`, Innenabstand `16px 24px`, Rand `6px solid #ec6aa8`, Hintergrund `#fbf4e2`, Schrift `#2b3442`
- `h2` im Ausweis: Außenabstand `0 0 12px`
- Absätze im Ausweis: Außenabstand `4px 0`
