---
schema_version: 1
id: w049-speisekarte-kaskade
revision: 1
titel: 'Speisekarte: wer gewinnt'
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- projekt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p class=\"motto\">Fisch, so frisch wie die Antarktis</p>\n<div class=\"karte\"\
  >\n  <h2>Heute auf der Karte</h2>\n  <ul>\n    <li>Hering im Eismantel <span class=\"preis\">4,50</span></li>\n    <li id=\"\
  tagesangebot\">Makrele am Stiel <span class=\"preis\">3,80</span></li>\n    <li class=\"ausverkauft\">Eisscholle mit Sardinen\
  \ <span class=\"preis\">5,20</span></li>\n  </ul>\n  <h2>Getränke</h2>\n  <ul>\n    <li>Eiswasser <span class=\"preis\"\
  >1,00</span></li>\n  </ul>\n</div>\n"
ziel_css: "body {\n  background-color: midnightblue;\n}\n\nh1, h2 {\n  color: gold;\n}\n\n.preis {\n  color: gold;\n}\n\n\
  .motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: navy;\n}\n\n.karte li {\n  background-color: darkslateblue;\n\
  }\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n}\n\n#tagesangebot .preis {\n  color: orange;\n\
  }\n"
hints:
- kosten: 0
  text: 'Seit der neuen Regel .karte li hat die Eisscholle keinen grauen Streifen mehr: .ausverkauft ist nicht genau genug.
    Und der Preis des Tagesangebots braucht eine eigene, genauere Regel als .preis.'
- kosten: 3
  text: '.karte .ausverkauft statt .ausverkauft, dazu #tagesangebot .preis'
starter_code: "body {\n  background-color: midnightblue;\n}\n\nh1, h2 {\n  color: gold;\n}\n\n.preis {\n  color: gold;\n}\n\
  \n.motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n.ausverkauft {\n  color: lightgray;\n\
  \  background-color: dimgray;\n}\n\n.karte h2 {\n  background-color: darkslateblue;\n}\n\n.karte > ul {\n  background-color:\
  \ navy;\n}\n\n.karte li {\n  background-color: darkslateblue;\n}\n"
---

Pit hat allen Einträgen der Karte einen Streifen gegeben, und schon ist die ausverkaufte Eisscholle nicht mehr grau hinterlegt. Außerdem soll der Preis des Tagesangebots orange leuchten statt gold.

## Vorgaben

- Einträge der Karte (`.karte li`): Hintergrundfarbe `darkslateblue` (steht schon da)
- ausverkaufte Einträge: Schriftfarbe `lightgray`, Hintergrundfarbe `dimgray`, und zwar so, dass die Regel gewinnt
- das Tagesangebot behält seinen grünen Hintergrund (die id gewinnt ohnehin)
- der Preis im Tagesangebot: Schriftfarbe `orange`, alle anderen Preise bleiben gold
