---
schema_version: 1
id: w027-ausnahme
revision: 1
titel: Die Ausnahme
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- klasse
- id
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li class=\"fisch\">Hering</li>\n  <li class=\"fisch\" id=\"chef\">Pits Lieblingsmakrele</li>\n  <li class=\"\
  fisch\">Sardinen</li>\n</ul>\n"
ziel_css: ".fisch {\n  color: skyblue;\n}\n\n#chef {\n  background-color: purple;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Regeln: eine für die Klasse fisch, eine für die id chef.'
- kosten: 2
  text: '.fisch bekommt color, #chef bekommt background-color.'
starter_code: '/* Alle Fische, und einer ganz besonders */

  '
---

Alle Fische sind himmelblau. Pits Lieblingsmakrele trägt zusätzlich die id `chef` und bekommt einen lila Hintergrund, Pit besteht darauf.

## Vorgaben

- Klasse `fisch`: Schriftfarbe `skyblue`
- id `chef`: Hintergrundfarbe `purple`
