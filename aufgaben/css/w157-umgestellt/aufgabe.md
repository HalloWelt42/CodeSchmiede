---
schema_version: 1
id: w157-umgestellt
revision: 1
titel: Anders als im HTML
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- grid-area
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"bon\">\n  <div class=\"summe\">Summe: 8,30</div>\n  <div class=\"posten\">Hering 4,50<br>Makrele\
  \ 3,80</div>\n  <div class=\"kopf\">Zum frostigen Hering</div>\n</div>\n"
ziel_css: ".bon {\n  display: grid;\n  width: 280px;\n  grid-template-areas:\n    \"kopf\"\n    \"posten\"\n    \"summe\"\
  ;\n  gap: 2px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  font-family: monospace;\n  padding: 12px;\n}\n\n.kopf\
  \ { grid-area: kopf; font-weight: bold; }\n.posten { grid-area: posten; }\n.summe { grid-area: summe; border-top: 1px dashed\
  \ #2b3442; }\n"
hints:
- kosten: 0
  text: Im HTML steht die Summe zuerst. Der Plan bestimmt, wo sie landet.
- kosten: 3
  text: Ein Plan mit drei Zeilen "kopf" "posten" "summe" und grid-area für alle drei Kinder.
starter_code: ".bon {\n  display: grid;\n  width: 280px;\n  gap: 2px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n \
  \ font-family: monospace;\n  padding: 12px;\n}\n\n.kopf { font-weight: bold; }\n.summe { border-top: 1px dashed #2b3442;\
  \ }\n"
---

Im HTML des Kassenbons steht alles verkehrt herum. Ordne ihn mit einem Plan: oben der Kopf, dann die Posten, unten die Summe. Das HTML bleibt, wie es ist.

## Vorgaben

- Klasse `bon`: Plan aus drei Zeilen `"kopf" "posten" "summe"`
- `.kopf`, `.posten`, `.summe`: in ihre Bereiche
