---
schema_version: 1
id: w063-dick-und-schraeg
revision: 1
titel: Dick und schräg
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- font-weight
- font-style
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Heute frisch</h2>

  <p class="preis">4,50</p>

  <p class="motto">Mit Liebe gebraten</p>

  '
ziel_css: "h2 {\n  font-weight: normal;\n}\n\n.preis {\n  font-weight: bold;\n}\n\n.motto {\n  font-style: italic;\n}\n"
hints:
- kosten: 0
  text: 'Drei Regeln: die Überschrift verliert ihr Fett, der Preis bekommt welches, das Motto wird schräg.'
- kosten: 2
  text: 'h2: font-weight normal, .preis: font-weight bold, .motto: font-style italic'
starter_code: '/* Fett, normal und schräg */

  '
---

Die Überschrift soll ausnahmsweise nicht fett sein, dafür der Preis. Und das Motto steht schräg.

## Vorgaben

- `h2`: Schriftstärke `normal`
- Klasse `preis`: Schriftstärke `bold`
- Klasse `motto`: Schriftstil `italic`
