---
schema_version: 1
id: w053-hex-kurz
revision: 1
titel: Kurz und knapp
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- hex
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="eis">Eiswürfel</p>

  <p class="meer">Meer</p>

  '
ziel_css: ".eis {\n  background-color: #aef;\n  color: #000;\n}\n\n.meer {\n  background-color: #06c;\n}\n"
hints:
- kosten: 0
  text: 'Die Kurzform verdoppelt jedes Zeichen: #06c ist #0066cc.'
- kosten: 2
  text: ".meer {\n  background-color: #06c;\n}"
starter_code: ".eis {\n  background-color: #aaeeff;\n  color: #000000;\n}\n"
---

Der Eiswürfel ist schon hellblau. Das Meer bekommt `#06c`, die kurze Form von `#0066cc`. Welche Form du schreibst, ist egal.

## Vorgaben

- Klasse `eis`: Hintergrundfarbe `#aef`, Schriftfarbe `#000` (steht schon da, in langer Form)
- Klasse `meer`: Hintergrundfarbe `#06c`
