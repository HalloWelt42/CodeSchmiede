---
schema_version: 1
id: w077-mittig
revision: 1
titel: Ab in die Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- margin
- auto
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="karte">Speisekarte</div>

  '
ziel_css: ".karte {\n  width: 300px;\n  margin: 40px auto;\n  padding: 20px;\n  background-color: #ffd166;\n  color: #222;\n\
  \  text-align: center;\n}\n"
hints:
- kosten: 0
  text: 'margin mit zwei Werten: oben und unten 40 Pixel, links und rechts auto.'
- kosten: 2
  text: 'margin: 40px auto;'
starter_code: ".karte {\n  width: 300px;\n  padding: 20px;\n  background-color: #ffd166;\n  color: #222;\n  text-align: center;\n\
  }\n"
---

Die Karte klebt links oben. Sie soll mit 40 Pixeln Abstand nach oben in der Mitte der Bühne stehen.

## Vorgaben

- Klasse `karte`: wie bisher, dazu Außenabstand `40px` oben und unten, links und rechts `auto`
