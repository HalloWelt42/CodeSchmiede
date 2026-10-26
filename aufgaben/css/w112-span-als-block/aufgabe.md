---
schema_version: 1
id: w112-span-als-block
revision: 1
titel: Der span wird ein Block
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- display
- block
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Heute im Angebot: <span class="angebot">Makrele am Stiel</span> nur solange der Vorrat reicht.</p>

  '
ziel_css: ".angebot {\n  display: block;\n  width: 220px;\n  margin: 10px 0;\n  padding: 10px;\n  background-color: gold;\n\
  \  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Als Inline-Element ignoriert der span Breite und Abstände nach oben und unten.
- kosten: 2
  text: 'display: block;'
starter_code: ".angebot {\n  width: 220px;\n  margin: 10px 0;\n  padding: 10px;\n  background-color: gold;\n  color: #2b3442;\n\
  }\n"
---

Das Angebot soll als eigener goldener Kasten mitten im Absatz stehen. Pits Angaben wirken aber nicht.

## Vorgaben

- Klasse `angebot`: `display: block`, alles andere bleibt
