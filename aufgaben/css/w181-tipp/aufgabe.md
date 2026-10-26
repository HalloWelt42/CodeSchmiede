---
schema_version: 1
id: w181-tipp
revision: 1
titel: Ein Tipp davor
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- before
- content
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="tipp">Montags gibt es doppelt Eis.</p>

  <p class="tipp">Pia kennt alle Fische beim Namen.</p>

  '
ziel_css: ".tipp::before {\n  content: \"Tipp: \";\n  color: gold;\n  font-weight: bold;\n}\n"
hints:
- kosten: 0
  text: Ohne content erscheint das Pseudoelement nicht.
- kosten: 2
  text: 'content: "Tipp: ";'
starter_code: ".tipp::before {\n  color: gold;\n  font-weight: bold;\n}\n"
---

Vor jedem Tipp soll fett und golden Tipp: stehen. Die Regel ist fast fertig.

## Vorgaben

- `.tipp::before`: Inhalt `"Tipp: "` (mit Leerzeichen am Ende), Farbe und Stärke stehen schon da
