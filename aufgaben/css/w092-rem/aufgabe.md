---
schema_version: 1
id: w092-rem
revision: 1
titel: Immer gleich groß
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- rem
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kiste\">\n  <div class=\"kiste\">\n    <p class=\"preis\">4,50</p>\n  </div>\n</div>\n"
ziel_css: ".kiste {\n  font-size: 1.5em;\n}\n\n.preis {\n  font-size: 1.25rem;\n}\n"
hints:
- kosten: 0
  text: Die Kisten vergrößern die Schrift, und em erbt das. rem misst immer mit der Grundschrift der Seite.
- kosten: 2
  text: 'font-size: 1.25rem;'
starter_code: ".kiste {\n  font-size: 1.5em;\n}\n\n.preis {\n  font-size: 1.25em;\n}\n"
---

Der Preis steckt in zwei Kisten, die jede die Schrift vergrößern, und ist darum riesig. Er soll genau 1,25-mal so groß sein wie die Grundschrift der Seite, egal wo er steckt.

## Vorgaben

- Klasse `kiste`: Schriftgröße `1.5em` (bleibt)
- Klasse `preis`: Schriftgröße `1.25rem`
