---
schema_version: 1
id: w066-ausverkauft-streichen
revision: 1
titel: Weg damit
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- text-decoration
- text-transform
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2>Heute aus</h2>\n<ul>\n  <li class=\"weg\">Eisscholle mit Sardinen</li>\n  <li>Hering im Eismantel</li>\n</ul>\n"
ziel_css: "h2 {\n  text-transform: uppercase;\n}\n\n.weg {\n  text-decoration: line-through;\n  color: gray;\n}\n"
hints:
- kosten: 0
  text: Durchstreichen geht mit text-decoration und dem Wert line-through.
- kosten: 2
  text: ".weg {\n  text-decoration: line-through;\n  color: gray;\n}"
starter_code: "h2 {\n  text-transform: uppercase;\n}\n"
---

Was heute aus ist, wird durchgestrichen und grau. Die Überschrift schreit schon in Großbuchstaben.

## Vorgaben

- `h2`: Großbuchstaben (steht schon da)
- Klasse `weg`: durchgestrichen, Schriftfarbe `gray`
