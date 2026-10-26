---
schema_version: 1
id: w071-schild
revision: 1
titel: Ein Schild nach Maß
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- width
- height
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="schild">Geöffnet</div>

  '
ziel_css: ".schild {\n  background-color: teal;\n  width: 240px;\n  height: 100px;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Angaben kommen dazu: width und height, beide in Pixeln.'
- kosten: 2
  text: "width: 240px;\n  height: 100px;"
starter_code: ".schild {\n  background-color: teal;\n}\n"
---

Das Schild ist ein Streifen über die ganze Breite. Gib ihm feste Maße.

## Vorgaben

- Klasse `schild`: Hintergrund `teal` (steht schon da), Breite `240px`, Höhe `100px`
