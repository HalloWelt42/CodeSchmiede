---
schema_version: 1
id: w038-lager
revision: 1
titel: Das Lager
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
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Lager</h1>\n<h2>Kühlraum</h2>\n<div class=\"regal\">\n  <p>Heringe</p>\n  <div class=\"kiste\">\n    <p>Sardinen</p>\n\
  \    <p>Makrelen</p>\n  </div>\n</div>\n<p>Tür bitte schließen!</p>\n"
ziel_css: "h1, h2 {\n  color: skyblue;\n}\n\n.regal > p {\n  background-color: teal;\n}\n\n.kiste * {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: 'Drei Regeln: eine Gruppe für die Überschriften, direkte Kinder des Regals, alles in der Kiste.'
- kosten: 3
  text: .regal > p trifft nur die Heringe, .kiste * die Sardinen und Makrelen.
starter_code: '/* Ordnung im Lager */

  '
---

Alles aus dem Kapitel: Bring Farbe ins Lager, ohne dass der Hinweis an der Tür etwas abbekommt.

## Vorgaben

- `h1` und `h2`: Schriftfarbe `skyblue`, in einer Regel
- Absätze direkt im Element mit der Klasse `regal`: Hintergrundfarbe `teal`
- alles im Element mit der Klasse `kiste`: Schriftfarbe `gold`
- der letzte Absatz bleibt, wie er ist
