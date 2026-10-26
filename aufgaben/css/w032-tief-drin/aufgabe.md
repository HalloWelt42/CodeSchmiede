---
schema_version: 1
id: w032-tief-drin
revision: 1
titel: Ganz tief drin
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- nachfahre
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<p><strong>Achtung:</strong> Fisch ist kalt.</p>\n<ul>\n  <li><strong>Hering</strong> mit Eis</li>\n  <li>Makrele\
  \ <em>mit <strong>doppelt</strong> Eis</em></li>\n</ul>\n"
ziel_css: "ul strong {\n  color: tomato;\n}\n"
hints:
- kosten: 0
  text: 'Das Leerzeichen sucht in jeder Tiefe: ul, Leerzeichen, strong.'
- kosten: 2
  text: "ul strong {\n  color: tomato;\n}"
starter_code: '/* Hervorgehobenes in der Liste */

  '
---

Alles Hervorgehobene in der Liste soll tomatenrot werden, egal wie tief es steckt. Das Achtung über der Liste bleibt, wie es ist.

## Vorgaben

- `strong` irgendwo in einer `ul`: Schriftfarbe `tomato`
