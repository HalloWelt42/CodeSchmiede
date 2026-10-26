---
schema_version: 1
id: w191-hausfarbe
revision: 1
titel: Die Hausfarbe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- variablen
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
ziel_css: ":root {\n  --hausfarbe: #f472b6;\n}\n\nh2, .preis {\n  color: var(--hausfarbe);\n}\n\n.streifen {\n  height: 12px;\n\
  \  background-color: var(--hausfarbe);\n}\n"
hints:
- kosten: 0
  text: Ändere nur eine einzige Zeile.
- kosten: 2
  text: '--hausfarbe: #f472b6;'
starter_code: ":root {\n  --hausfarbe: #ffd166;\n}\n\nh2, .preis {\n  color: var(--hausfarbe);\n}\n\n.streifen {\n  height:\
  \ 12px;\n  background-color: var(--hausfarbe);\n}\n"
---

Pia will eine neue Hausfarbe: Rosa statt Gelb. Dank der Variable reicht eine einzige Änderung.

## Vorgaben

- `--hausfarbe` in `:root`: `#f472b6`
