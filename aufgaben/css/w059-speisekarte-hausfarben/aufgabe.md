---
schema_version: 1
id: w059-speisekarte-hausfarben
revision: 1
titel: 'Speisekarte: Hausfarben'
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
  notiz: Aufbaukurs CSS, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p class=\"motto\">Fisch, so frisch wie die Antarktis</p>\n<div class=\"karte\"\
  >\n  <h2>Heute auf der Karte</h2>\n  <ul>\n    <li>Hering im Eismantel <span class=\"preis\">4,50</span></li>\n    <li id=\"\
  tagesangebot\">Makrele am Stiel <span class=\"preis\">3,80</span></li>\n    <li class=\"ausverkauft\">Eisscholle mit Sardinen\
  \ <span class=\"preis\">5,20</span></li>\n  </ul>\n  <h2>Getränke</h2>\n  <ul>\n    <li>Eiswasser <span class=\"preis\"\
  >1,00</span></li>\n  </ul>\n</div>\n"
ziel_css: "body {\n  background-color: #0b1d3a;\n}\n\nh1, h2 {\n  color: #ffd166;\n}\n\n.preis {\n  color: gold;\n}\n\n.motto\
  \ {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: rgb(255 255 255 / 0.08);\n}\n\n.karte li {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n  opacity: 0.6;\n}\n\n\
  #tagesangebot .preis {\n  color: orange;\n}\n"
hints:
- kosten: 0
  text: 'Tausche vier Werte: den Hintergrund der Bühne, die Farbe der Überschriften, den Hintergrund der Listen, und gib den
    ausverkauften Einträgen opacity.'
- kosten: 3
  text: 'body #0b1d3a, h1 und h2 #ffd166, .karte > ul rgb(255 255 255 / 0.08), .karte .ausverkauft zusätzlich opacity: 0.6'
starter_code: "body {\n  background-color: midnightblue;\n}\n\nh1, h2 {\n  color: gold;\n}\n\n.preis {\n  color: gold;\n}\n\
  \n.motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: navy;\n}\n\n.karte li {\n  background-color: darkslateblue;\n\
  }\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n}\n\n#tagesangebot .preis {\n  color: orange;\n\
  }\n"
---

Die Speisekarte bekommt eigene Hausfarben statt Farbnamen. Dein CSS aus Kapitel 4 steht schon da.

## Vorgaben

- ganze Bühne: Hintergrundfarbe `#0b1d3a`
- `h1` und `h2`: Schriftfarbe `#ffd166`
- Listen direkt in der Karte: Hintergrund Weiß mit Alphawert `0.08`
- ausverkaufte Einträge: zusätzlich Deckkraft `0.6`
- alles Übrige bleibt
