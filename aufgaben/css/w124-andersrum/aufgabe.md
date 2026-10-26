---
schema_version: 1
id: w124-andersrum
revision: 1
titel: Andersherum
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- flex-direction
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"countdown\">\n  <div>1</div>\n  <div>2</div>\n  <div>3</div>\n  <div>Los!</div>\n</div>\n"
ziel_css: ".countdown {\n  display: flex;\n  flex-direction: row-reverse;\n  gap: 8px;\n}\n\n.countdown div {\n  background-color:\
  \ teal;\n  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: Die Reihe soll rechts beginnen, ohne das HTML zu ändern.
- kosten: 2
  text: 'flex-direction: row-reverse;'
starter_code: ".countdown {\n  display: flex;\n  gap: 8px;\n}\n\n.countdown div {\n  background-color: teal;\n  padding: 10px;\n\
  }\n"
---

Der Countdown soll von rechts nach links laufen: rechts die 1, links das Los.

## Vorgaben

- Klasse `countdown`: Richtung `row-reverse`
