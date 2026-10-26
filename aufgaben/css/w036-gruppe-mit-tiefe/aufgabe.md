---
schema_version: 1
id: w036-gruppe-mit-tiefe
revision: 1
titel: Gruppe mit Tiefe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- gruppe
- nachfahre
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2>Draußen</h2>\n<p>Preis für Luft: <span class=\"preis\">0,00</span></p>\n<div class=\"karte\">\n  <h2>Drinnen</h2>\n\
  \  <p>Hering <span class=\"preis\">4,50</span></p>\n</div>\n"
ziel_css: ".karte h2, .karte .preis {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Jeder Selektor der Gruppe steht für sich. Beide brauchen die Karte davor.
- kosten: 2
  text: .karte h2, .karte .preis {
starter_code: "h2, .preis {\n  color: gold;\n}\n"
---

Gold sollen nur Überschrift und Preis **in** der Karte werden. Die Regel hat schon die richtige Gruppe, trifft aber auch die Dinge draußen.

## Vorgaben

- `h2` und die Klasse `preis`, jeweils nur im Element mit der Klasse `karte`: Schriftfarbe `gold`, in einer Regel
