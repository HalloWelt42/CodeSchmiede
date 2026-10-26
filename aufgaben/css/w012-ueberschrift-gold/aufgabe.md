---
schema_version: 1
id: w012-ueberschrift-gold
revision: 1
titel: Goldene Überschrift
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- color
- selektor
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischwagen</h1>

  <p>Frischer Hering, eiskalt serviert.</p>

  '
ziel_css: "p {\n  color: tomato;\n}\n\nh1 {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Schreib unter die Regel für p eine zweite Regel, diesmal mit dem Selektor h1.
- kosten: 2
  text: "h1 {\n  color: gold;\n}"
starter_code: "p {\n  color: tomato;\n}\n"
---

Der Absatz ist schon tomatenrot. Jetzt bekommt die Überschrift ihre eigene Regel und wird **gold**.

## Vorgaben

- Absätze (`p`): Schriftfarbe `tomato` (steht schon da)
- Überschrift (`h1`): Schriftfarbe `gold`
