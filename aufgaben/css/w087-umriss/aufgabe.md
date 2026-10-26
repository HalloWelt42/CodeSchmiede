---
schema_version: 1
id: w087-umriss
revision: 1
titel: Umriss statt Rand
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- outline
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="wahl">Hering</p>

  <p>Makrele</p>

  <p>Sardinen</p>

  '
ziel_css: "p {\n  width: 200px;\n  background-color: #1f6f8b;\n  padding: 6px;\n}\n\n.wahl {\n  outline: 4px solid gold;\n\
  \  outline-offset: 4px;\n}\n"
hints:
- kosten: 0
  text: Der Rand macht den ersten Eintrag größer und schiebt alles. Ein Umriss braucht keinen Platz.
- kosten: 2
  text: ".wahl {\n  outline: 4px solid gold;\n  outline-offset: 4px;\n}"
starter_code: "p {\n  width: 200px;\n  background-color: #1f6f8b;\n  padding: 6px;\n}\n\n.wahl {\n  border: 4px solid gold;\n\
  }\n"
---

Der gewählte Eintrag soll markiert werden, ohne dass er größer wird als die anderen. Nimm einen Umriss mit etwas Abstand.

## Vorgaben

- `p`: wie bisher
- Klasse `wahl`: Umriss `4px solid gold`, Abstand des Umrisses `4px`, kein Rand
