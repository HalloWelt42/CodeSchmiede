---
schema_version: 1
id: w114-ausblenden
revision: 1
titel: Ausblenden
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- display
- none
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li>Hering</li>\n  <li class=\"ausverkauft\">Eisscholle</li>\n  <li>Makrele</li>\n  <li class=\"ausverkauft\"\
  >Tintenfisch</li>\n</ul>\n"
ziel_css: "li {\n  background-color: #1f6f8b;\n  margin-bottom: 4px;\n}\n\n.ausverkauft {\n  display: none;\n}\n"
hints:
- kosten: 0
  text: 'Ganz weg, ohne Lücke: display none.'
- kosten: 2
  text: ".ausverkauft {\n  display: none;\n}"
starter_code: "li {\n  background-color: #1f6f8b;\n  margin-bottom: 4px;\n}\n"
---

Ausverkaufte Gerichte sollen heute gar nicht auf der Karte stehen, ohne Lücke.

## Vorgaben

- Klasse `ausverkauft`: ganz ausgeblendet, ohne Platz
