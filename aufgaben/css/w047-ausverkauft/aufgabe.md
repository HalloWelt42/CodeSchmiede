---
schema_version: 1
id: w047-ausverkauft
revision: 1
titel: Die Klasse kommt nicht durch
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- spezifitaet
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"karte\">\n  <li>Hering</li>\n  <li class=\"ausverkauft\">Eisscholle</li>\n  <li>Makrele</li>\n</ul>\n"
ziel_css: ".karte li {\n  color: lightblue;\n}\n\n.karte .ausverkauft {\n  color: gray;\n}\n"
hints:
- kosten: 0
  text: .karte li ist eine Klasse und ein Element, .ausverkauft nur eine Klasse. Mach .ausverkauft genauer.
- kosten: 2
  text: .karte .ausverkauft {
starter_code: ".karte li {\n  color: lightblue;\n}\n\n.ausverkauft {\n  color: gray;\n}\n"
---

Die Eisscholle ist ausverkauft und soll grau werden, bleibt aber hellblau. Die Regel für alle Einträge ist genauer als die für ausverkaufte.

## Vorgaben

- Einträge der Karte: Schriftfarbe `lightblue` (bleibt)
- ausverkaufte Einträge: Schriftfarbe `gray`
