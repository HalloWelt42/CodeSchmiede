---
schema_version: 1
id: w058-farbtafel
revision: 1
titel: Die Farbtafel
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"tafel\">\n  <p class=\"rot\">Hummer</p>\n  <p class=\"gelb\">Zitrone</p>\n  <p class=\"blass\">Gestern</p>\n\
  </div>\n"
ziel_css: ".tafel {\n  background-color: #1d3557;\n}\n\n.rot {\n  background-color: rgb(230, 57, 70);\n}\n\n.gelb {\n  background-color:\
  \ #fc3;\n  color: #000;\n}\n\n.blass {\n  background-color: rgb(255 255 255 / 0.25);\n  opacity: 0.5;\n}\n"
hints:
- kosten: 0
  text: 'Vier Regeln mit vier Schreibweisen: Hex lang, rgb, Hex kurz und rgb mit Alphawert.'
- kosten: 3
  text: 'Der Absatz Gestern bekommt zwei Angaben: einen durchscheinenden Hintergrund und opacity.'
starter_code: '/* Die Farbtafel des Fischwagens */

  '
---

Alles aus dem Kapitel auf einer Tafel.

## Vorgaben

- Klasse `tafel`: Hintergrundfarbe `#1d3557`
- Klasse `rot`: Hintergrundfarbe `rgb(230, 57, 70)`
- Klasse `gelb`: Hintergrundfarbe `#fc3`, Schriftfarbe `#000`
- Klasse `blass`: Hintergrundfarbe Weiß mit Alphawert `0.25` und Deckkraft `0.5` für das ganze Element
