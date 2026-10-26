---
schema_version: 1
id: w088-eisschollen
revision: 1
titel: Eisschollen
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
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="scholle gross">Pit</div>

  <div class="scholle rund">Pia</div>

  <div class="scholle ecke">Paul</div>

  '
ziel_css: ".scholle {\n  background-color: #e3f1f8;\n  color: #2b3442;\n  padding: 10px;\n  margin-bottom: 12px;\n  border:\
  \ 2px dotted #38bdf8;\n}\n\n.gross {\n  width: 260px;\n  border-radius: 16px;\n}\n\n.rund {\n  width: 50px;\n  height: 50px;\n\
  \  border-radius: 35px;\n}\n\n.ecke {\n  width: 180px;\n  border-radius: 0 30px;\n  border-bottom: 6px solid #38bdf8;\n\
  }\n"
hints:
- kosten: 0
  text: Erst die gemeinsame Regel für alle Schollen, dann je eine für gross, rund und ecke.
- kosten: 3
  text: 'Die runde Scholle ist mit Polster und Rand 74 Pixel groß, 35 Pixel Radius machen sie fast ganz rund. Zwei Werte bei
    border-radius: der erste für oben links und unten rechts.'
starter_code: '/* Drei Eisschollen */

  '
---

Alles aus dem Kapitel: drei Eisschollen für drei Pinguine.

## Vorgaben

- Klasse `scholle`: Hintergrund `#e3f1f8`, Schrift `#2b3442`, Innenabstand `10px`, Außenabstand unten `12px`, Rand `2px dotted #38bdf8`
- Klasse `gross`: Breite `260px`, Eckenradius `16px`
- Klasse `rund`: Breite und Höhe `50px`, Eckenradius `35px`
- Klasse `ecke`: Breite `180px`, Eckenradius `0 30px`, Rand unten `6px solid #38bdf8`
