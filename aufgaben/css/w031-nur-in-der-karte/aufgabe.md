---
schema_version: 1
id: w031-nur-in-der-karte
revision: 1
titel: Nur in der Karte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- nachfahre
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"karte\">\n  <p>Hering <span>4,50</span></p>\n  <p>Makrele <span>3,80</span></p>\n</div>\n<p>Parken:\
  \ <span>kostenlos</span></p>\n"
ziel_css: ".karte span {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Setz die Klasse der Karte und ein Leerzeichen vor span. Dann zählen nur span, die in der Karte stecken.
- kosten: 2
  text: .karte span {
starter_code: "span {\n  color: gold;\n}\n"
---

Gerade wird jeder `span` gold, auch der kostenlose Parkplatz. Gold sollen aber nur die Preise in der Karte sein.

## Vorgaben

- `span`-Elemente irgendwo im Element mit der Klasse `karte`: Schriftfarbe `gold`
- der `span` außerhalb der Karte bleibt hell
