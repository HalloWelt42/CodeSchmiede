---
schema_version: 1
id: w033-direkt-in-der-kiste
revision: 1
titel: Direkt in der Kiste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- kind
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kiste\">\n  <p>Hering</p>\n  <p>Makrele</p>\n  <div>\n    <p>Sardinen in der Dose</p>\n  </div>\n\
  </div>\n"
ziel_css: ".kiste > p {\n  background-color: teal;\n}\n"
hints:
- kosten: 0
  text: Mit Leerzeichen trifft die Regel auch die Sardinen, die in einem weiteren div stecken. Das Größerzeichen nimmt nur
    direkte Kinder.
- kosten: 2
  text: .kiste > p {
starter_code: ".kiste p {\n  background-color: teal;\n}\n"
---

Nur was direkt in der Kiste liegt, bekommt den türkisen Hintergrund. Die Sardinen stecken in einer eigenen Dose (einem `div`) und bleiben ohne.

## Vorgaben

- Absätze, die direkte Kinder des Elements mit der Klasse `kiste` sind: Hintergrundfarbe `teal`
