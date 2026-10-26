---
schema_version: 1
id: w023-gleiche-klasse
revision: 1
titel: Neu ist neu
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2 class=\"neu\">Frisch eingetroffen</h2>\n<ul>\n  <li class=\"neu\">Makrele am Stiel</li>\n  <li>Hering im Eismantel</li>\n\
  </ul>\n<p class=\"neu\">Nur solange der Vorrat reicht.</p>\n"
ziel_css: ".neu {\n  color: black;\n  background-color: lightgreen;\n}\n"
hints:
- kosten: 0
  text: Überschrift, Listeneintrag und Absatz tragen dieselbe Klasse. Eine einzige Regel reicht für alle drei.
- kosten: 2
  text: .neu mit color und background-color
starter_code: '/* Alles, was neu ist */

  '
---

Alles, was die Klasse `neu` trägt, soll hervorstechen, egal ob Überschrift, Listeneintrag oder Absatz.

## Vorgaben

- Klasse `neu`: Schriftfarbe `black`, Hintergrundfarbe `lightgreen`
