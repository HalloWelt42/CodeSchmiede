---
schema_version: 1
id: w123-spalte
revision: 1
titel: Eine Spalte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- flex-direction
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"turm\">\n  <div>Dach</div>\n  <div>Fenster</div>\n  <div>Tür</div>\n</div>\n"
ziel_css: ".turm {\n  display: flex;\n  flex-direction: column;\n  gap: 6px;\n  width: 200px;\n}\n\n.turm div {\n  background-color:\
  \ teal;\n  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: Die Hauptachse soll von oben nach unten laufen.
- kosten: 2
  text: 'flex-direction: column;'
starter_code: ".turm {\n  display: flex;\n  gap: 6px;\n  width: 200px;\n}\n\n.turm div {\n  background-color: teal;\n  padding:\
  \ 10px;\n}\n"
---

Der Turm liegt auf der Seite. Stell ihn auf: die Kinder untereinander.

## Vorgaben

- Klasse `turm`: Richtung `column`, alles andere bleibt
