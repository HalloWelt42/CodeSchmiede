---
schema_version: 1
id: w064-schriftfamilien
revision: 1
titel: Drei Familien
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- font-family
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Tageskarte</h2>

  <p class="bon">Bon 0042: 4,50</p>

  <p>Guten Appetit!</p>

  '
ziel_css: "h2 {\n  font-family: serif;\n}\n\n.bon {\n  font-family: monospace;\n}\n"
hints:
- kosten: 0
  text: Der Kassenbon braucht eine Schrift, in der jedes Zeichen gleich breit ist.
- kosten: 2
  text: ".bon {\n  font-family: monospace;\n}"
starter_code: "h2 {\n  font-family: serif;\n}\n"
---

Die Überschrift hat schon Füßchen. Der Bon soll aussehen wie aus der Kasse: jedes Zeichen gleich breit.

## Vorgaben

- `h2`: Schriftart `serif` (steht schon da)
- Klasse `bon`: Schriftart `monospace`
