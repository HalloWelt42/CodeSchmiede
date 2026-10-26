---
schema_version: 1
id: w183-anfuehrung
revision: 1
titel: Ein Zitat
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- before
- after
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="zitat">Der beste Hering ist der, den man gerade isst.</p>

  <p class="wer">Pit, Fischbrater</p>

  '
ziel_css: ".zitat {\n  font-size: 20px;\n  font-style: italic;\n}\n\n.zitat::before {\n  content: \"> \";\n  color: gold;\n\
  }\n\n.zitat::after {\n  content: \" <\";\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Pseudoelemente: eins davor, eins dahinter.'
- kosten: 2
  text: '.zitat::before { content: "> "; } und .zitat::after { content: " <"; }, beide gold'
starter_code: ".zitat {\n  font-size: 20px;\n  font-style: italic;\n}\n"
---

Pits Lebensweisheit wird eingerahmt: vorne ein goldenes Größerzeichen, hinten ein goldenes Kleinerzeichen.

## Vorgaben

- `.zitat::before`: Inhalt `"> "`, Farbe `gold`
- `.zitat::after`: Inhalt `" <"`, Farbe `gold`
