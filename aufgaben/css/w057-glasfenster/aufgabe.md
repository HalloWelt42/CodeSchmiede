---
schema_version: 1
id: w057-glasfenster
revision: 1
titel: Glasfenster
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- transparenz
- rgb
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"wagen\">\n  <p class=\"fenster\">Blick in den Fischwagen</p>\n  <p class=\"tuer\">Tür</p>\n</div>\n"
ziel_css: ".wagen {\n  background-color: rgb(200, 60, 60);\n}\n\n.fenster {\n  background-color: rgb(180 220 255 / 0.5);\n\
  \  color: #000;\n}\n\n.tuer {\n  background-color: rgb(80, 40, 20);\n}\n"
hints:
- kosten: 0
  text: 'Drei Regeln: der Wagen deckend rot, das Fenster halb durchsichtig hellblau, die Tür deckend braun.'
- kosten: 3
  text: 'Das Fenster: rgb(180 220 255 / 0.5), mit Leerzeichen und Schrägstrich.'
starter_code: '/* Ein roter Wagen mit Glasfenster und Holztür */

  '
---

Der Fischwagen ist rot, die Tür aus dunklem Holz. Durchs Fenster schimmert das Rot des Wagens, denn das Glas deckt nur zur Hälfte.

## Vorgaben

- Klasse `wagen`: Hintergrundfarbe `rgb(200, 60, 60)`
- Klasse `fenster`: Hintergrundfarbe `rgb(180 220 255 / 0.5)`, Schriftfarbe `#000`
- Klasse `tuer`: Hintergrundfarbe `rgb(80, 40, 20)`
