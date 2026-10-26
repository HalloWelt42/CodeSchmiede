---
schema_version: 1
id: w137-suchleiste
revision: 1
titel: Die Suchleiste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- flex-grow
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"leiste\">\n  <div class=\"logo\">Fisch</div>\n  <div class=\"suche\">Suchen ...</div>\n  <div class=\"\
  knopf\">Los</div>\n</div>\n"
ziel_css: ".leiste {\n  display: flex;\n  gap: 8px;\n}\n\n.leiste div {\n  background-color: teal;\n  padding: 10px;\n}\n\n\
  .leiste .suche {\n  flex-grow: 1;\n  background-color: #e3f1f8;\n  color: #555;\n}\n"
hints:
- kosten: 0
  text: Das Suchfeld soll den ganzen freien Platz bekommen.
- kosten: 2
  text: ".leiste .suche {\n  flex-grow: 1;"
starter_code: ".leiste {\n  display: flex;\n  gap: 8px;\n}\n\n.leiste div {\n  background-color: teal;\n  padding: 10px;\n\
  }\n\n.leiste .suche {\n  background-color: #e3f1f8;\n  color: #555;\n}\n"
---

Das Suchfeld ist viel zu kurz. Es soll allen freien Platz zwischen Logo und Knopf einnehmen.

## Vorgaben

- Klasse `suche` in der Leiste (`.leiste .suche`): `flex-grow: 1`, alles andere bleibt
