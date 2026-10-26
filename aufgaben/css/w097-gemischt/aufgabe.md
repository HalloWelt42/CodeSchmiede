---
schema_version: 1
id: w097-gemischt
revision: 1
titel: Maßband-Mix
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- einheiten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"rahmen\">\n  <h2>Fang des Tages</h2>\n  <p>Riesenmakrele</p>\n</div>\n"
ziel_css: ".rahmen {\n  width: 60vw;\n  padding: 1rem;\n  border: 0.25rem solid gold;\n}\n\nh2 {\n  font-size: 1.25rem;\n\
  \  margin: 0 0 0.5em;\n}\n\np {\n  width: 50%;\n  margin: 0;\n  background-color: teal;\n}\n"
hints:
- kosten: 0
  text: Drei Regeln. Lies bei jeder Angabe genau, welche Einheit gefordert ist.
- kosten: 3
  text: 'Rahmen: 60vw breit, 1rem Polster, 0.25rem Rand. h2: 1.25rem groß, unten 0.5em Abstand. p: halb so breit wie der Rahmen.'
starter_code: '/* Jedes Maß mit dem passenden Maßband */

  '
---

Ein Rahmen, in dem jedes Maß eine andere Einheit hat.

## Vorgaben

- Klasse `rahmen`: Breite `60vw`, Innenabstand `1rem`, Rand `0.25rem solid gold`
- `h2`: Schriftgröße `1.25rem`, Außenabstand `0 0 0.5em`
- Absätze: Breite `50%`, Außenabstand `0`, Hintergrund `teal`
