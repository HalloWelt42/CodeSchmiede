---
schema_version: 1
id: w132-name-und-preis
revision: 1
titel: Name links, Preis rechts
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- space-between
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="zeile"><span>Hering im Eismantel</span><span class="preis">4,50</span></div>

  <div class="zeile"><span>Makrele am Stiel</span><span class="preis">3,80</span></div>

  '
ziel_css: ".zeile {\n  display: flex;\n  justify-content: space-between;\n  width: 320px;\n  border-bottom: 1px dotted gray;\n\
  }\n\n.preis {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Der freie Platz gehört zwischen Name und Preis.
- kosten: 2
  text: 'justify-content: space-between;'
starter_code: ".zeile {\n  display: flex;\n  width: 320px;\n  border-bottom: 1px dotted gray;\n}\n\n.preis {\n  color: gold;\n\
  }\n"
---

Wie auf jeder ordentlichen Speisekarte: Name links, Preis ganz rechts.

## Vorgaben

- Klasse `zeile`: `justify-content: space-between`
