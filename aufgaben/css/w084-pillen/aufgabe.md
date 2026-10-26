---
schema_version: 1
id: w084-pillen
revision: 1
titel: Pillen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- border-radius
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p><span class="marke">neu</span> Makrele am Stiel</p>

  <p><span class="marke">scharf</span> Hering mit Chili</p>

  '
ziel_css: ".marke {\n  background-color: crimson;\n  padding: 2px 10px;\n  border-radius: 999px;\n}\n"
hints:
- kosten: 0
  text: Ein sehr großer Radius macht aus einem flachen Kasten eine Pille.
- kosten: 2
  text: 'border-radius: 999px;'
starter_code: ".marke {\n  background-color: crimson;\n  padding: 2px 10px;\n}\n"
---

Die Marken vor den Gerichten sollen aussehen wie kleine Pillen.

## Vorgaben

- Klasse `marke`: wie bisher, dazu Eckenradius `999px`
