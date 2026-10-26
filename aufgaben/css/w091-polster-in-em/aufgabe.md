---
schema_version: 1
id: w091-polster-in-em
revision: 1
titel: Polster, das mitwächst
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- em
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="knopf">Bestellen</p>

  '
ziel_css: ".knopf {\n  font-size: 24px;\n  width: 6em;\n  padding: 0.5em 1em;\n  background-color: #e63946;\n}\n"
hints:
- kosten: 0
  text: 'Gib das Polster in em an: ein halbes em oben und unten, ein ganzes links und rechts.'
- kosten: 2
  text: 'padding: 0.5em 1em;'
starter_code: ".knopf {\n  font-size: 24px;\n  width: 6em;\n  padding: 6px 12px;\n  background-color: #e63946;\n}\n"
---

Der Knopf ist schon in em breit, nur das Polster steht noch in Pixeln. Gib es in em an, damit es mit der Schrift wächst.

## Vorgaben

- Klasse `knopf`: Innenabstand `0.5em 1em`, alles andere bleibt
