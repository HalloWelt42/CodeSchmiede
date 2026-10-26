---
schema_version: 1
id: w014-buehne-faerben
revision: 1
titel: Die ganze Bühne färben
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- background-color
- body
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Nachtverkauf</h1>

  <p>Fisch unter Sternen.</p>

  '
ziel_css: "body {\n  background-color: midnightblue;\n}\n\nh1 {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Alles Sichtbare steckt im Element body. Eine Regel für body färbt die ganze Bühne.
- kosten: 2
  text: "body {\n  background-color: midnightblue;\n}"
starter_code: "h1 {\n  color: gold;\n}\n"
---

Nachtverkauf am Fischwagen: Die ganze Bühne soll nachtblau werden, die Überschrift leuchtet gold wie der Mond.

## Vorgaben

- ganze Bühne (`body`): Hintergrundfarbe `midnightblue`
- Überschrift (`h1`): Schriftfarbe `gold` (steht schon da)
