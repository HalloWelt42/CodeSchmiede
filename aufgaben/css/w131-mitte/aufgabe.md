---
schema_version: 1
id: w131-mitte
revision: 1
titel: Ab in die Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- justify-content
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ".reihe {\n  display: flex;\n  gap: 8px;\n  justify-content: center;\n}\n\n.reihe div {\n  background-color: teal;\n\
  \  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: Den freien Platz auf beide Seiten verteilen.
- kosten: 2
  text: 'justify-content: center;'
starter_code: ".reihe {\n  display: flex;\n  gap: 8px;\n}\n\n.reihe div {\n  background-color: teal;\n  padding: 10px;\n}\n"
---

Die Fische drängeln sich links. Schieb sie in die Mitte der Reihe.

## Vorgaben

- Klasse `reihe`: `justify-content: center`
