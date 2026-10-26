---
schema_version: 1
id: w041-reihenfolge
revision: 1
titel: Wer zuletzt schreibt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- kaskade
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Heute: Hering</p>

  '
ziel_css: "p {\n  color: skyblue;\n}\n\np {\n  color: gold;\n}\n"
hints:
- kosten: 0
  text: Beide Regeln sind gleich genau, also gewinnt die spätere. Tausche die beiden Regeln.
- kosten: 2
  text: Die Regel mit gold muss unten stehen.
starter_code: "p {\n  color: gold;\n}\n\np {\n  color: skyblue;\n}\n"
---

Der Absatz soll gold sein, ist aber himmelblau. Ändere keine Farbe, sondern nur die Reihenfolge der Regeln.

## Vorgaben

- der Absatz ist am Ende `gold`
- beide Regeln bleiben stehen
