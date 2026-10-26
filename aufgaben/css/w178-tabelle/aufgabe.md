---
schema_version: 1
id: w178-tabelle
revision: 1
titel: Die Preistabelle
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
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n  <li>Dorsch</li>\n\
  \  <li>Scholle</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n\n.liste li:first-child {\n  font-weight: bold;\n\
  \  color: gold;\n}\n\n.liste li:nth-child(odd):not(:first-child) {\n  background-color: #2b3442;\n}\n\n.liste li:last-child\
  \ {\n  border-bottom: 4px solid gold;\n}\n\n.liste li:nth-child(n+5) {\n  font-style: italic;\n}\n"
hints:
- kosten: 0
  text: 'Vier Regeln: der Kopf (erstes li), dunkle ungerade Zeilen außer dem Kopf, eine Linie unter dem letzten, schräg ab
    dem fünften.'
- kosten: 3
  text: 'Pseudoklassen lassen sich verketten: li:nth-child(odd):not(:first-child)'
starter_code: "/* Die Preistabelle */\n.liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n"
---

Alles aus dem Kapitel in einer Preistabelle.

## Vorgaben

- erstes `li`: fett, Schrift `gold`
- ungerade `li` außer dem ersten: Hintergrund `#2b3442`
- letztes `li`: Rand unten `4px solid gold`
- `li` ab dem fünften: schräg
