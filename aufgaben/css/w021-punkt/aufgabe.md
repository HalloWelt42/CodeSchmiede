---
schema_version: 1
id: w021-punkt
revision: 1
titel: Der fehlende Punkt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Hering <span class="preis">4,50</span></p>

  <p>Makrele <span class="preis">3,80</span></p>

  '
ziel_css: ".preis {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Ohne Punkt sucht der Browser ein Element namens preis. Eine Klasse wählt man mit einem Punkt davor.
- kosten: 2
  text: .preis {
starter_code: "preis {\n  color: gold;\n}\n"
---

Pit hat die Regel für die Preise geschrieben, aber nichts wird gold. Ein einziges Zeichen fehlt.

## Vorgaben

- alles mit der Klasse `preis`: Schriftfarbe `gold`
