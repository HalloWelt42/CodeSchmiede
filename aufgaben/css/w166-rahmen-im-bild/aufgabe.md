---
schema_version: 1
id: w166-rahmen-im-bild
revision: 1
titel: Rahmen im Bild
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- inset
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"bild\">\n  Aussicht vom Eisberg\n  <div class=\"rahmen\"></div>\n</div>\n"
ziel_css: ".bild {\n  position: relative;\n  width: 260px;\n  height: 160px;\n  padding: 10px;\n  background: linear-gradient(to\
  \ bottom, #38bdf8, #0b4f8a);\n}\n\n.rahmen {\n  position: absolute;\n  inset: 16px;\n  border: 9px double white;\n}\n"
hints:
- kosten: 0
  text: Der Rahmen soll mit 16 Pixeln Abstand zu allen Seiten im Bild aufgespannt werden.
- kosten: 2
  text: "position: absolute;\n  inset: 16px;"
starter_code: ".bild {\n  position: relative;\n  width: 260px;\n  height: 160px;\n  padding: 10px;\n  background: linear-gradient(to\
  \ bottom, #38bdf8, #0b4f8a);\n}\n\n.rahmen {\n  border: 9px double white;\n}\n"
---

Im Bild soll ein doppelter weißer Rahmen liegen, 16 Pixel vom Rand entfernt, ohne den Text zu verschieben.

## Vorgaben

- Klasse `rahmen`: `position: absolute`, `inset: 16px`
