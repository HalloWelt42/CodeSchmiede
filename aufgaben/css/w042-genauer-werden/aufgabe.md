---
schema_version: 1
id: w042-genauer-werden
revision: 1
titel: Genauer werden
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- spezifitaet
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul id=\"karte\">\n  <li>Hering <span class=\"preis\">4,50</span></li>\n  <li>Makrele <span>am Stiel</span></li>\n\
  </ul>\n"
ziel_css: "#karte span {\n  color: lightgreen;\n}\n\n#karte .preis {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: '#karte span hat eine id, .preis nur eine Klasse. Die id gewinnt, obwohl .preis später steht. Gib .preis auch die
    id davor.'
- kosten: 2
  text: '#karte .preis {'
starter_code: "#karte span {\n  color: lightgreen;\n}\n\n.preis {\n  color: gold;\n}\n"
---

Der Preis soll gold sein, bleibt aber hellgrün. Die Regel für `.preis` verliert gegen die genauere Regel darüber. Mach sie genauer, statt die erste Regel zu ändern.

## Vorgaben

- `span` in `#karte`: Schriftfarbe `lightgreen` (bleibt)
- der Preis (Klasse `preis`): Schriftfarbe `gold`
