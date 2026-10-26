---
schema_version: 1
id: w076-border-box
revision: 1
titel: Rechnen lassen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- box-sizing
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="a">Hering</div>

  <div class="b">Makrele mit viel Polster</div>

  '
ziel_css: ".a, .b {\n  width: 280px;\n  background-color: teal;\n  margin-bottom: 10px;\n  box-sizing: border-box;\n}\n\n\
  .b {\n  padding: 10px 40px;\n  border: 6px solid gold;\n}\n"
hints:
- kosten: 0
  text: Beide sollen gleich breit aussehen. Lass den Browser Polster und Rand innen abziehen.
- kosten: 2
  text: 'box-sizing: border-box;'
starter_code: ".a, .b {\n  width: 280px;\n  background-color: teal;\n  margin-bottom: 10px;\n}\n\n.b {\n  padding: 10px 40px;\n\
  \  border: 6px solid gold;\n}\n"
---

Die beiden Kästen haben dasselbe width, sehen aber verschieden breit aus. Sorge dafür, dass beide von Rand zu Rand 280 Pixel breit sind, ohne zu rechnen.

## Vorgaben

- beide Kästen von Rand zu Rand `280px` breit, mit `box-sizing: border-box`
