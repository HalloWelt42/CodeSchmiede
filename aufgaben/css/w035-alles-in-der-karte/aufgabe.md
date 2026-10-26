---
schema_version: 1
id: w035-alles-in-der-karte
revision: 1
titel: Alles in der Karte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- universal
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"karte\">\n  <h2>Hering</h2>\n  <p>mit <em>viel</em> Eis</p>\n  <ul>\n    <li>knusprig</li>\n  </ul>\n\
  </div>\n<p>Außerhalb der Karte</p>\n"
ziel_css: ".karte * {\n  color: lightgreen;\n}\n"
hints:
- kosten: 0
  text: Der Stern allein trifft alles. Mit der Klasse der Karte und einem Leerzeichen davor nur, was in der Karte steckt.
- kosten: 2
  text: .karte * {
starter_code: "* {\n  color: lightgreen;\n}\n"
---

Pit hat mit dem Stern alles hellgrün gemacht, auch den Absatz unter der Karte. Begrenze die Regel auf das Innere der Karte.

## Vorgaben

- alles im Element mit der Klasse `karte`: Schriftfarbe `lightgreen`
- der Absatz außerhalb bleibt hell
