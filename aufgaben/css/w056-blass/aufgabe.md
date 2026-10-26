---
schema_version: 1
id: w056-blass
revision: 1
titel: Blass vor Neid
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- transparenz
- opacity
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li>Hering</li>\n  <li class=\"ausverkauft\">Eisscholle mit Sardinen</li>\n  <li>Makrele</li>\n</ul>\n"
ziel_css: "li {\n  background-color: #1f6f8b;\n}\n\n.ausverkauft {\n  opacity: 0.4;\n}\n"
hints:
- kosten: 0
  text: opacity macht das ganze Element durchsichtig, mit Schrift und Hintergrund.
- kosten: 2
  text: ".ausverkauft {\n  opacity: 0.4;\n}"
starter_code: "li {\n  background-color: #1f6f8b;\n}\n"
---

Was ausverkauft ist, soll blass werden, mit Schrift, Hintergrund und Punkt. Die anderen Einträge bleiben kräftig.

## Vorgaben

- `li`: Hintergrundfarbe `#1f6f8b` (steht schon da)
- Klasse `ausverkauft`: Deckkraft `0.4`
