---
schema_version: 1
id: w101-schweben
revision: 1
titel: Die Karte schwebt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- box-shadow
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="karte">Tageskarte</div>

  '
ziel_css: ".karte {\n  width: 200px;\n  padding: 24px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 10px;\n  box-shadow: 10px 10px 20px black;\n}\n"
hints:
- kosten: 0
  text: 'Vier Werte: rechts, unten, Unschärfe, Farbe.'
- kosten: 2
  text: 'box-shadow: 10px 10px 20px black;'
starter_code: ".karte {\n  width: 200px;\n  padding: 24px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 10px;\n}\n"
---

Die Karte liegt flach auf. Gib ihr einen weichen Schatten nach rechts unten, dann schwebt sie.

## Vorgaben

- Klasse `karte`: wie bisher, dazu Schatten `10px 10px 20px black`
