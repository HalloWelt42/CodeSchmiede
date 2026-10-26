---
schema_version: 1
id: w174-jeder-dritte
revision: 1
titel: Jeder Dritte gratis
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- nth-child
- muster
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"schlange\">\n  <div>1</div>\n  <div>2</div>\n  <div>3</div>\n  <div>4</div>\n  <div>5</div>\n  <div>6</div>\n\
  \  <div>7</div>\n  <div>8</div>\n  <div>9</div>\n</div>\n"
ziel_css: ".schlange {\n  display: flex;\n  gap: 4px;\n}\n\n.schlange div {\n  padding: 10px 14px;\n  background-color: teal;\n\
  }\n\n.schlange div:nth-child(3n) {\n  background-color: gold;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: 'Jede dritte Stelle: ein Muster mit n.'
- kosten: 2
  text: .schlange div:nth-child(3n) {
starter_code: ".schlange {\n  display: flex;\n  gap: 4px;\n}\n\n.schlange div {\n  padding: 10px 14px;\n  background-color:\
  \ teal;\n}\n"
---

Pit verschenkt an jeden dritten Gast in der Schlange einen Fisch. Mach diese Gäste golden.

## Vorgaben

- jedes dritte `div` der Schlange: Hintergrund `gold`, Schrift `#2b3442`
