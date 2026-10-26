---
schema_version: 1
id: w054-grautoene
revision: 1
titel: Fünfzig Grautöne, na ja, drei
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- hex
- grau
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="a">Morgennebel</p>

  <p class="b">Möwe</p>

  <p class="c">Gewitterwolke</p>

  '
ziel_css: ".a {\n  background-color: #ddd;\n  color: #222;\n}\n\n.b {\n  background-color: #999;\n  color: #222;\n}\n\n.c\
  \ {\n  background-color: #444;\n}\n"
hints:
- kosten: 0
  text: 'Grau heißt: alle drei Anteile gleich. #ddd ist hell, #444 dunkel.'
- kosten: 2
  text: Drei Regeln für .a, .b und .c; die ersten beiden bekommen dunkle Schrift.
starter_code: '/* Drei Grautöne */

  '
---

Das Wetter über dem Fischwagen in drei Grautönen, von hell nach dunkel.

## Vorgaben

- Klasse `a`: Hintergrundfarbe `#ddd`, Schriftfarbe `#222`
- Klasse `b`: Hintergrundfarbe `#999`, Schriftfarbe `#222`
- Klasse `c`: Hintergrundfarbe `#444`
