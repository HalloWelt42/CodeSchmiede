---
schema_version: 1
id: w185-punkt-davor
revision: 1
titel: Ein Punkt davor
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- before
- schmuck
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="frisch">Hering</p>

  <p>Makrele</p>

  <p class="frisch">Sardine</p>

  '
ziel_css: ".frisch::before {\n  content: \"\";\n  display: inline-block;\n  width: 12px;\n  height: 12px;\n  margin-right:\
  \ 8px;\n  background-color: #3fb950;\n  border-radius: 6px;\n}\n"
hints:
- kosten: 0
  text: Ein leerer Kasten als inline-block, damit er in der Zeile bleibt und trotzdem eine Größe bekommt.
- kosten: 3
  text: content leer, display inline-block, 12 mal 12 Pixel, Abstand rechts, grün, Radius 6px
starter_code: '/* Ein grüner Punkt vor allem, was frisch ist */

  '
---

Vor jedem frischen Fisch leuchtet ein kleiner grüner Punkt.

## Vorgaben

- `.frisch::before`: leerer Inhalt, `display: inline-block`, Breite und Höhe `12px`, Außenabstand rechts `8px`, Hintergrund `#3fb950`, Eckenradius `6px`
