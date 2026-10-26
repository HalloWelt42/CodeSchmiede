---
schema_version: 1
id: w107-sonne
revision: 1
titel: Die Sonne
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- radial-gradient
- border-radius
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="sonne"></div>

  '
ziel_css: ".sonne {\n  width: 160px;\n  height: 160px;\n  border-radius: 80px;\n  background: radial-gradient(#fff6c2, gold,\
  \ orange);\n  box-shadow: 0 0 30px 10px orange;\n  margin: 40px auto;\n}\n"
hints:
- kosten: 0
  text: Ein Kreis, ein runder Verlauf von Hellgelb nach Orange und ein oranger Schein mit Ausdehnung.
- kosten: 3
  text: 'border-radius: 80px; background: radial-gradient(#fff6c2, gold, orange); box-shadow: 0 0 30px 10px orange;'
starter_code: ".sonne {\n  width: 160px;\n  height: 160px;\n  margin: 40px auto;\n}\n"
---

Über dem Fischwagen geht die Sonne auf: rund, innen hell, außen orange, mit einem Schein drumherum.

## Vorgaben

- Klasse `sonne`: wie bisher, dazu Eckenradius `80px`, runder Verlauf `#fff6c2`, `gold`, `orange`, Schatten `0 0 30px 10px orange`
