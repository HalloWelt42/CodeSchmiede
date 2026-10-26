---
schema_version: 1
id: w198-farbschema
revision: 1
titel: Das Farbschema
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
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"karte\">\n  <h2>Fischwagen</h2>\n  <p>Täglich frisch</p>\n</div>\n<div class=\"karte rot\">\n  <h2>Hummerstand</h2>\n\
  \  <p>Nur am Wochenende</p>\n</div>\n"
ziel_css: ":root {\n  --akzent: #38bdf8;\n  --abstand: 10px;\n}\n\n.rot {\n  --akzent: #f87171;\n}\n\n.karte {\n  width: calc(50%\
  \ - 4 * var(--abstand));\n  display: inline-block;\n  margin-right: var(--abstand);\n  padding: var(--abstand);\n  border-top:\
  \ calc(var(--abstand) / 2) solid var(--akzent);\n  background-color: #2b3442;\n}\n\n.karte h2 {\n  margin: 0;\n  color:\
  \ var(--akzent, white);\n}\n"
hints:
- kosten: 0
  text: Zwei Variablen in :root, eine davon für .rot neu gesetzt. Die Karten benutzen sie, auch in calc.
- kosten: 3
  text: Breite calc(50% - 4 * var(--abstand)), Rand oben calc(var(--abstand) / 2) solid var(--akzent)
starter_code: '/* Ein Farbschema für zwei Karten */

  '
---

Alles aus dem Kapitel: zwei Karten, ein Farbschema.

## Vorgaben

- `:root`: `--akzent: #38bdf8`, `--abstand: 10px`
- `.rot`: `--akzent: #f87171`
- `.karte`: Breite `calc(50% - 4 * var(--abstand))`, `display: inline-block`, Außenabstand rechts und Polster je `var(--abstand)`, Rand oben `calc(var(--abstand) / 2) solid var(--akzent)`, Hintergrund `#2b3442`
- `.karte h2`: Außenabstand `0`, Schrift `var(--akzent, white)`
