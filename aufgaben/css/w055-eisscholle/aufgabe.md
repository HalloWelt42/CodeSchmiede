---
schema_version: 1
id: w055-eisscholle
revision: 1
titel: Durchsichtiges Eis
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- transparenz
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"meer\">\n  <p class=\"eis\">Eisscholle</p>\n  <p>Offenes Wasser</p>\n</div>\n"
ziel_css: ".meer {\n  background-color: #0b4f8a;\n}\n\n.eis {\n  background-color: rgb(255 255 255 / 0.35);\n}\n"
hints:
- kosten: 0
  text: 'Gib dem Weiß einen Alphawert: nach den drei Anteilen ein Schrägstrich und die Deckkraft.'
- kosten: 2
  text: rgb(255 255 255 / 0.35)
starter_code: ".meer {\n  background-color: #0b4f8a;\n}\n\n.eis {\n  background-color: rgb(255 255 255);\n}\n"
---

Die Eisscholle ist reinweiß, und darauf ist ihre helle Schrift nicht zu lesen. Echte Eisschollen lassen das Meer durchscheinen: Das Weiß soll nur zu 35 Prozent decken.

## Vorgaben

- Klasse `meer`: Hintergrundfarbe `#0b4f8a` (steht schon da)
- Klasse `eis`: Hintergrund Weiß mit Alphawert `0.35`
