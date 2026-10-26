---
schema_version: 1
id: w214-dazwischen
revision: 1
titel: Nur dazwischen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- media
- and
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="geraet">Du siehst die Tablet-Fassung.</p>

  '
ziel_css: ".geraet {\n  padding: 12px;\n  background-color: #2b3442;\n}\n\n@media (min-width: 500px) and (max-width: 900px)\
  \ {\n  .geraet {\n    background-color: purple;\n    border-left: 8px solid gold;\n  }\n}\n"
hints:
- kosten: 0
  text: Die obere Grenze ist zu klein, 600 liegt nicht dazwischen.
- kosten: 2
  text: '@media (min-width: 500px) and (max-width: 900px) {'
starter_code: ".geraet {\n  padding: 12px;\n  background-color: #2b3442;\n}\n\n@media (min-width: 500px) and (max-width: 550px)\
  \ {\n  .geraet {\n    background-color: purple;\n    border-left: 8px solid gold;\n  }\n}\n"
---

Der Hinweis soll nur auf Tablets lila werden: von 500 bis 900 Pixeln. Die obere Grenze stimmt noch nicht.

## Vorgaben

- Bedingung `(min-width: 500px) and (max-width: 900px)`
