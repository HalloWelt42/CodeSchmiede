---
schema_version: 1
id: w098-wegweiser
revision: 1
titel: Der Wegweiser
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
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"schild\">\n  <p class=\"ziel\">Zum Fischwagen</p>\n  <p class=\"weit\">noch 200 Watschelschritte</p>\n\
  </div>\n"
ziel_css: ".schild {\n  width: 80%;\n  max-width: 360px;\n  min-height: 30vh;\n  margin: 2rem auto;\n  padding: 1em;\n  background-color:\
  \ #c98c55;\n  color: #2b3442;\n  border-radius: 0.5rem;\n}\n\n.ziel {\n  font-size: 1.75rem;\n  margin: 0;\n}\n\n.weit {\n\
  \  font-size: 0.8em;\n  margin-top: 2em;\n}\n"
hints:
- kosten: 0
  text: Drei Regeln, fast jede Einheit aus dem Kapitel kommt vor.
- kosten: 3
  text: 'Das Schild: 80% breit, aber höchstens 360px, mindestens 30vh hoch, 2rem auto Außenabstand.'
starter_code: '/* Ein Wegweiser */

  '
---

Alles aus dem Kapitel auf einem Wegweiser.

## Vorgaben

- Klasse `schild`: Breite `80%`, höchstens `360px`, Höhe mindestens `30vh`, Außenabstand `2rem auto`, Innenabstand `1em`, Hintergrund `#c98c55`, Schrift `#2b3442`, Eckenradius `0.5rem`
- Klasse `ziel`: Schriftgröße `1.75rem`, Außenabstand `0`
- Klasse `weit`: Schriftgröße `0.8em`, Außenabstand oben `2em`
