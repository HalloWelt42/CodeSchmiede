---
schema_version: 1
id: w186-initiale
revision: 1
titel: Die Initiale
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- first-letter
- first-line
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="geschichte">Es war einmal ein Hering, der wollte nicht in die Pfanne. Also schwamm er bis zum Eisberg
  und eröffnete dort einen Fischwagen, der bis heute jeden Tag geöffnet hat.</p>

  '
ziel_css: ".geschichte {\n  width: 400px;\n  line-height: 1.6;\n}\n\n.geschichte::first-letter {\n  font-size: 48px;\n  font-family:\
  \ serif;\n  color: gold;\n}\n\n.geschichte::first-line {\n  text-transform: uppercase;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Pseudoelemente: der erste Buchstabe groß und golden, die erste Zeile in Großbuchstaben.'
- kosten: 3
  text: ::first-letter mit font-size 48px, font-family serif, color gold; ::first-line mit text-transform uppercase
starter_code: ".geschichte {\n  width: 400px;\n  line-height: 1.6;\n}\n"
---

Die Geschichte des Fischwagens beginnt wie ein altes Märchenbuch: mit einem großen goldenen Anfangsbuchstaben und einer ersten Zeile in Großbuchstaben.

## Vorgaben

- `.geschichte::first-letter`: Schrift `48px`, `serif`, `gold`
- `.geschichte::first-line`: Großbuchstaben
