---
schema_version: 1
id: w116-knoepfe
revision: 1
titel: Knöpfe in einer Reihe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- inline-block
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Bestellen: <span class="knopf">klein</span> <span class="knopf">mittel</span> <span class="knopf">riesig</span></p>

  '
ziel_css: ".knopf {\n  display: inline-block;\n  min-width: 80px;\n  padding: 12px 8px;\n  margin: 8px 4px;\n  text-align:\
  \ center;\n  background-color: #e63946;\n  border-radius: 8px;\n}\n"
hints:
- kosten: 0
  text: Die Knöpfe sind span, also inline. Mindestbreite und Abstände nach oben und unten greifen erst als inline-block.
- kosten: 2
  text: 'display: inline-block;'
starter_code: ".knopf {\n  min-width: 80px;\n  padding: 12px 8px;\n  margin: 8px 4px;\n  text-align: center;\n  background-color:\
  \ #e63946;\n  border-radius: 8px;\n}\n"
---

Die drei Knöpfe sollen gleich breit sein und Abstand nach oben und unten halten, aber in der Zeile bleiben.

## Vorgaben

- Klasse `knopf`: `display: inline-block`, alles andere bleibt
