---
schema_version: 1
id: w216-zusatz-zeigen
revision: 1
titel: Zusätzlich auf großen Fenstern
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- media
- display
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"seite\">\n  <div class=\"inhalt\">Speisekarte</div>\n  <div class=\"zusatz\">Wetter: eisig</div>\n\
  </div>\n"
ziel_css: ".seite {\n  display: flex;\n  gap: 8px;\n}\n\n.inhalt {\n  flex-grow: 1;\n  padding: 20px;\n  background-color:\
  \ teal;\n}\n\n.zusatz {\n  display: none;\n}\n\n@media (min-width: 500px) {\n  .zusatz {\n    display: block;\n    width:\
  \ 140px;\n    padding: 20px;\n    background-color: #38bdf8;\n    color: #0b1d3a;\n  }\n}\n"
hints:
- kosten: 0
  text: Auf schmalen Fenstern bleibt der Zusatz versteckt, ab 500 Pixeln erscheint er.
- kosten: 3
  text: 'In der Media Query: .zusatz mit display block, Breite 140px, Polster 20px, Hintergrund #38bdf8, Schrift #0b1d3a'
starter_code: ".seite {\n  display: flex;\n  gap: 8px;\n}\n\n.inhalt {\n  flex-grow: 1;\n  padding: 20px;\n  background-color:\
  \ teal;\n}\n\n.zusatz {\n  display: none;\n}\n"
---

Auf Telefonen ist kein Platz für den Wetterkasten. Ab 500 Pixeln Breite soll er neben der Speisekarte erscheinen.

## Vorgaben

- `.zusatz` bleibt außerhalb versteckt (steht schon da)
- ab `min-width: 500px`: `.zusatz` mit `display: block`, Breite `140px`, Polster `20px`, Hintergrund `#38bdf8`, Schrift `#0b1d3a`
