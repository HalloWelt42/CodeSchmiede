---
schema_version: 1
id: w073-rahmen
revision: 1
titel: Goldener Rahmen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- border
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="bild">Pit beim Angeln</div>

  '
ziel_css: ".bild {\n  width: 200px;\n  padding: 30px;\n  background-color: #ddd;\n  color: #222;\n  border: 8px solid gold;\n\
  }\n"
hints:
- kosten: 0
  text: Der Rand ist nicht zu sehen. Ihm fehlt etwas Wichtiges zwischen Breite und Farbe.
- kosten: 2
  text: 'border: 8px solid gold;'
starter_code: ".bild {\n  width: 200px;\n  padding: 30px;\n  background-color: #ddd;\n  color: #222;\n  border: 8px gold;\n\
  }\n"
---

Pits Foto soll einen goldenen Rahmen bekommen, aber der Rand ist unsichtbar.

## Vorgaben

- Klasse `bild`: Rand `8px`, durchgezogen, `gold`; alles andere steht schon da
