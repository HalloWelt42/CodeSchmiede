---
schema_version: 1
id: w192-variable-benutzen
revision: 1
titel: Variable benutzen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- var
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Speisekarte</h2>

  <p class="preis">4,50</p>

  <div class="streifen"></div>

  '
ziel_css: ":root {\n  --hausfarbe: #7dd3fc;\n}\n\nh2, .preis {\n  color: var(--hausfarbe);\n}\n\n.streifen {\n  height: 12px;\n\
  \  background-color: var(--hausfarbe);\n}\n"
hints:
- kosten: 0
  text: Der Streifen benutzt noch eine feste Farbe.
- kosten: 2
  text: 'background-color: var(--hausfarbe);'
starter_code: ":root {\n  --hausfarbe: #7dd3fc;\n}\n\nh2, .preis {\n  color: var(--hausfarbe);\n}\n\n.streifen {\n  height:\
  \ 12px;\n  background-color: gold;\n}\n"
---

Überschrift und Preis benutzen schon die Hausfarbe, nur der Streifen hat noch ein festes Gold. Lass ihn die Variable benutzen.

## Vorgaben

- `.streifen`: Hintergrund `var(--hausfarbe)`
