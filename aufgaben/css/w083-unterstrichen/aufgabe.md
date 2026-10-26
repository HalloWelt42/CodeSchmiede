---
schema_version: 1
id: w083-unterstrichen
revision: 1
titel: Linie drunter
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- border-bottom
- border-left
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Speisekarte</h2>

  <p class="tipp">Tipp: Montags gibt es doppelt Eis.</p>

  '
ziel_css: "h2 {\n  border-bottom: 3px solid gold;\n}\n\n.tipp {\n  border-left: 6px solid teal;\n  padding-left: 12px;\n}\n"
hints:
- kosten: 0
  text: Der Tipp bekommt nur links einen Rand und etwas Innenabstand links.
- kosten: 2
  text: ".tipp {\n  border-left: 6px solid teal;\n  padding-left: 12px;\n}"
starter_code: "h2 {\n  border-bottom: 3px solid gold;\n}\n"
---

Die Überschrift ist schon unterstrichen. Der Tipp soll links einen türkisen Balken bekommen, mit etwas Abstand zum Text.

## Vorgaben

- `h2`: Rand unten `3px solid gold` (steht schon da)
- Klasse `tipp`: Rand links `6px solid teal`, Innenabstand links `12px`
