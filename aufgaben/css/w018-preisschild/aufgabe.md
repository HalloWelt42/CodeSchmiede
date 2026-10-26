---
schema_version: 1
id: w018-preisschild
revision: 1
titel: Das Preisschild
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
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Angebot</h1>\n<p>Makrele am Stiel für nur <span>3,80</span></p>\n<ul>\n  <li>knusprig</li>\n  <li>eiskalt</li>\n\
  </ul>\n"
ziel_css: "body {\n  background-color: darkslategray;\n}\n\nh1 {\n  color: gold;\n}\n\nspan {\n  color: black;\n  background-color:\
  \ gold;\n}\n\nli {\n  color: lightgreen;\n}\n"
hints:
- kosten: 0
  text: 'Vier Regeln: für body, h1, span und li.'
- kosten: 3
  text: body bekommt background-color, span bekommt color und background-color.
starter_code: '/* Das Preisschild */

  '
---

Alles aus dem Kapitel auf einem Schild: Färbe Bühne, Überschrift, Preis und Liste.

## Vorgaben

- ganze Bühne (`body`): Hintergrundfarbe `darkslategray`
- Überschrift (`h1`): Schriftfarbe `gold`
- Preis (`span`): Schriftfarbe `black`, Hintergrundfarbe `gold`
- Listeneinträge (`li`): Schriftfarbe `lightgreen`
