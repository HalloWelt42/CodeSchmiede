---
schema_version: 1
id: w016-markieren
revision: 1
titel: Mit dem Textmarker
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- span
- background-color
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Heute gibt es Hering mit <span>doppelt Eis</span> zum halben Preis.</p>

  '
ziel_css: "span {\n  color: black;\n  background-color: yellow;\n}\n"
hints:
- kosten: 0
  text: span ist ein Kasten mitten im Text. Sein Hintergrund liegt nur hinter seinen Wörtern, wie bei einem Textmarker.
- kosten: 2
  text: 'Eine Regel für span mit zwei Angaben: color und background-color.'
starter_code: '/* Markiere das Wichtige */

  '
---

Pit will, dass jeder das Angebot sieht. Markiere die Wörter im `span` wie mit einem gelben Textmarker: schwarze Schrift auf gelbem Grund.

## Vorgaben

- `span`: Schriftfarbe `black`, Hintergrundfarbe `yellow`
