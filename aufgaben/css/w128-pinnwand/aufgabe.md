---
schema_version: 1
id: w128-pinnwand
revision: 1
titel: Die Pinnwand
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"wand\">\n  <div class=\"spalte\">\n    <div>Montag</div>\n    <div>Hering</div>\n  </div>\n  <div\
  \ class=\"spalte\">\n    <div>Dienstag</div>\n    <div>Ruhetag</div>\n  </div>\n  <div class=\"spalte\">\n    <div>Mittwoch</div>\n\
  \    <div>Makrele</div>\n  </div>\n</div>\n"
ziel_css: ".wand {\n  display: flex;\n  flex-direction: row-reverse;\n  gap: 10px;\n}\n\n.spalte {\n  display: flex;\n  flex-direction:\
  \ column;\n  gap: 4px;\n}\n\n.spalte div {\n  padding: 8px;\n  background-color: #ffd166;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Flex-Behälter ineinander: die Wand als Reihe, rückwärts, und jede Spalte als Spalte.'
- kosten: 3
  text: .wand mit row-reverse, .spalte mit column, beide mit gap.
starter_code: '/* Die Pinnwand */

  '
---

Alles aus dem Kapitel: Pits Wochenplan an der Pinnwand. Pit hängt immer von rechts nach links auf.

## Vorgaben

- Klasse `wand`: Flex-Behälter, Richtung `row-reverse`, Lücke `10px`
- Klasse `spalte`: Flex-Behälter, Richtung `column`, Lücke `4px`
- Zettel (`.spalte div`): Polster `8px`, Hintergrund `#ffd166`, Schrift `#2b3442`
