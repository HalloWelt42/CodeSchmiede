---
schema_version: 1
id: w048-streit-am-tresen
revision: 1
titel: Streit am Tresen
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
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div id=\"tresen\">\n  <h2>Am Tresen</h2>\n  <p>Hering <span class=\"preis\">4,50</span></p>\n  <p class=\"leise\"\
  >Bitte nicht drängeln</p>\n</div>\n"
ziel_css: "span {\n  color: gray;\n}\n\n#tresen {\n  color: gold;\n}\n\n#tresen p {\n  color: skyblue;\n}\n\n#tresen .leise\
  \ {\n  color: gray;\n}\n\n.preis {\n  color: inherit;\n  background-color: navy;\n}\n"
hints:
- kosten: 0
  text: 'Fünf Regeln, die erste macht alle span grau: die Farbe des Tresens erbt die Überschrift, die Absätze bekommen eine
    eigene, der leise Absatz eine noch genauere.'
- kosten: 3
  text: '#tresen p schlägt die geerbte Farbe, #tresen .leise ist genauer als #tresen p. Der Preis übernimmt mit inherit die
    Farbe seines Absatzes.'
starter_code: '/* Wer gewinnt am Tresen? */

  '
---

Alles aus dem Kapitel: Am Tresen streiten sich die Regeln. Sorge dafür, dass am Ende jede Farbe stimmt.

## Vorgaben

- id `tresen`: Schriftfarbe `gold` (die Überschrift erbt sie)
- Absätze im Tresen: Schriftfarbe `skyblue`
- der Absatz mit der Klasse `leise` im Tresen: Schriftfarbe `gray`
- alle `span`: Schriftfarbe `gray`
- Klasse `preis`: erbt trotzdem die Schriftfarbe ihres Absatzes (`inherit`), Hintergrundfarbe `navy`
