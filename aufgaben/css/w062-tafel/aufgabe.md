---
schema_version: 1
id: w062-tafel
revision: 1
titel: Die Tafel vor dem Wagen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- font-size
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Zum frostigen Hering</h1>

  <p>Hering im Eismantel</p>

  <p class="klein">Fisch kann Gräten enthalten.</p>

  '
ziel_css: "h1 {\n  font-size: 40px;\n}\n\n.klein {\n  font-size: 12px;\n}\n"
hints:
- kosten: 0
  text: Für den Hinweis kommt eine zweite Regel mit seiner Klasse dazu.
- kosten: 2
  text: ".klein {\n  font-size: 12px;\n}"
starter_code: "h1 {\n  font-size: 40px;\n}\n"
---

Der Name ist schon riesig. Jetzt soll der Hinweis ganz klein werden, wie das Kleingedruckte auf jeder Tafel.

## Vorgaben

- `h1`: Schriftgröße `40px` (steht schon da)
- Klasse `klein`: Schriftgröße `12px`
