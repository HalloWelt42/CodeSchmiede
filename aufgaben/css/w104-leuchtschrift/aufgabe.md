---
schema_version: 1
id: w104-leuchtschrift
revision: 1
titel: Leuchtschrift
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- text-shadow
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Geöffnet</h1>

  '
ziel_css: "h1 {\n  font-size: 64px;\n  color: white;\n  text-align: center;\n  text-shadow: 0 0 16px #ff4fa3;\n}\n"
hints:
- kosten: 0
  text: Ein Textschatten ohne Versatz, aber mit viel Unschärfe leuchtet.
- kosten: 2
  text: 'text-shadow: 0 0 16px #ff4fa3;'
starter_code: "h1 {\n  font-size: 64px;\n  color: white;\n  text-align: center;\n}\n"
---

Die Leuchtreklame des Fischwagens: weiße Buchstaben mit pinkem Schein.

## Vorgaben

- `h1`: wie bisher, dazu Textschatten `0 0 16px #ff4fa3`
