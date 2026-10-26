---
schema_version: 1
id: w082-urkunde
revision: 1
titel: Die Urkunde
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- border-style
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="urkunde">Bester Hering des Jahres</div>

  '
ziel_css: ".urkunde {\n  width: 300px;\n  padding: 30px;\n  text-align: center;\n  background-color: #fbf4e2;\n  color: #2b3442;\n\
  \  border: 10px double #c9a227;\n}\n"
hints:
- kosten: 0
  text: Ein doppelter Rand braucht genug Breite. 10 Pixel reichen für zwei Linien und eine Lücke.
- kosten: 2
  text: 'border: 10px double #c9a227;'
starter_code: ".urkunde {\n  width: 300px;\n  padding: 30px;\n  text-align: center;\n  background-color: #fbf4e2;\n  color:\
  \ #2b3442;\n}\n"
---

Pits Hering hat gewonnen. Die Urkunde bekommt einen doppelten Goldrand.

## Vorgaben

- Klasse `urkunde`: wie bisher, dazu Rand `10px`, doppelt, `#c9a227`
