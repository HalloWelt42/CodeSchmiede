---
schema_version: 1
id: w106-markise
revision: 1
titel: Die Markise
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- linear-gradient
- farbhalt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="markise"></div>

  '
ziel_css: ".markise {\n  height: 60px;\n  background: linear-gradient(to right, white 25%, crimson 25%, crimson 50%, white\
  \ 50%, white 75%, crimson 75%);\n}\n"
hints:
- kosten: 0
  text: 'Statt weicher Übergänge harte Kanten: je zwei Farben an derselben Stelle.'
- kosten: 2
  text: white 25%, crimson 25%, crimson 50%, white 50%, white 75%, crimson 75%
starter_code: ".markise {\n  height: 60px;\n  background: linear-gradient(to right, white, crimson, white, crimson);\n}\n"
---

Die Markise über dem Wagen hat weiche Übergänge, echte Markisen haben harte Streifen. Vier gleich breite Streifen: weiß, rot, weiß, rot.

## Vorgaben

- Klasse `markise`: Höhe `60px`, Verlauf nach rechts mit harten Kanten bei 25, 50 und 75 Prozent
