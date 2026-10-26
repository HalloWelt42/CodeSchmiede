---
schema_version: 1
id: w156-luecke-im-plan
revision: 1
titel: Ein leeres Fach
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- grid-template-areas
- punkt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"theke\">\n  <div class=\"eis\">Eis</div>\n  <div class=\"fisch\">Fisch</div>\n  <div class=\"kasse\"\
  >Kasse</div>\n</div>\n"
ziel_css: ".theke {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  grid-template-rows: 90px 90px;\n  grid-template-areas:\n\
  \    \"eis fisch fisch\"\n    \". fisch fisch\"\n    \"kasse kasse kasse\";\n  gap: 4px;\n}\n\n.theke div {\n  background-color:\
  \ teal;\n  padding: 8px;\n}\n\n.eis { grid-area: eis; }\n.fisch { grid-area: fisch; }\n.kasse { grid-area: kasse; }\n"
hints:
- kosten: 0
  text: Erst der Plan mit einem Punkt für das leere Fach, dann je Kind sein Bereich.
- kosten: 3
  text: '"eis fisch fisch" ". fisch fisch" "kasse kasse kasse", dazu grid-area bei .eis, .fisch und .kasse'
starter_code: ".theke {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  grid-template-rows: 90px 90px;\n  gap:\
  \ 4px;\n}\n\n.theke div {\n  background-color: teal;\n  padding: 8px;\n}\n"
---

Die Theke: Eis oben links, der Fisch groß rechts über zwei Spalten und zwei Zeilen, unter dem Eis ein leeres Fach, ganz unten die Kasse über die ganze Breite.

## Vorgaben

- Klasse `theke`: Plan `"eis fisch fisch" ". fisch fisch" "kasse kasse kasse"`
- `.eis`, `.fisch`, `.kasse`: jeweils `grid-area` mit ihrem Namen
