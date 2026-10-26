---
schema_version: 1
id: w126-preis-daneben
revision: 1
titel: Preis daneben
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- flex
- gap
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"karte\">\n  <li><span>Hering</span><span class=\"preis\">4,50</span></li>\n  <li><span>Makrele</span><span\
  \ class=\"preis\">3,80</span></li>\n</ul>\n"
ziel_css: ".karte li {\n  display: flex;\n  gap: 24px;\n}\n\n.preis {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Jeder Eintrag wird selbst zum Flex-Behälter für Name und Preis.
- kosten: 2
  text: ".karte li {\n  display: flex;\n  gap: 24px;\n}"
starter_code: ".preis {\n  color: gold;\n}\n"
---

Name und Preis kleben aneinander. Mach jeden Eintrag zum Flex-Behälter mit 24 Pixeln Lücke. Die Punkte verschwinden dabei, das ist gewollt.

## Vorgaben

- Einträge der Karte: `display: flex`, Lücke `24px`
- Klasse `preis`: Schrift `gold` (steht schon da)
