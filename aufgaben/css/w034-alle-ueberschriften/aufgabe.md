---
schema_version: 1
id: w034-alle-ueberschriften
revision: 1
titel: Eine Regel für drei
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- gruppe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischwagen</h1>

  <h2>Speisekarte</h2>

  <p class="motto">Eiskalt und fangfrisch</p>

  <p>Heute mit Musik.</p>

  '
ziel_css: "h1, h2, .motto {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Schreib die übrigen Selektoren mit Komma getrennt vor dieselbe Regel.
- kosten: 2
  text: h1, h2, .motto {
starter_code: "h1 {\n  color: gold;\n}\n"
---

Die Hauptüberschrift ist schon gold. Die Zwischenüberschrift und das Motto sollen mitmachen, mit derselben Regel statt mit zwei neuen.

## Vorgaben

- `h1`, `h2` und die Klasse `motto`: Schriftfarbe `gold`, alles in einer Regel
- der letzte Absatz bleibt hell
