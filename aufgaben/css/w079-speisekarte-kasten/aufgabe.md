---
schema_version: 1
id: w079-speisekarte-kasten
revision: 1
titel: 'Speisekarte: Kasten'
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
  notiz: Aufbaukurs CSS, Kapitel 7
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
  #tagesangebot .preis {\n  color: orange;\n}\n\nh1 {\n  font-family: serif;\n  font-size: 40px;\n  text-align: center;\n\
  \  letter-spacing: 2px;\n}\n\n.motto {\n  font-style: italic;\n  text-align: center;\n}\n\nh2 {\n  font-size: 18px;\n  text-transform:\
  \ uppercase;\n}\n\n.preis {\n  font-weight: bold;\n}\n\n.karte .ausverkauft {\n  text-decoration: line-through;\n}\n\n*\
  \ {\n  box-sizing: border-box;\n}\n\nh1 {\n  margin: 0;\n}\n\n.karte {\n  width: 440px;\n  margin: 8px auto 0;\n  padding:\
  \ 4px 16px;\n  border: 3px solid #ffd166;\n}\n\nh2 {\n  padding: 2px 8px;\n}\n"
hints:
- kosten: 0
  text: 'Vier neue Regeln: box-sizing für alle, die Hauptüberschrift ohne Außenabstand, die Karte als Kasten in der Mitte
    und etwas Polster für die Zwischenüberschriften.'
- kosten: 3
  text: '.karte: width 440px, margin 8px auto 0, padding 4px 16px, border 3px solid #ffd166'
starter_code: "body {\n  background-color: #0b1d3a;\n}\n\nh1, h2 {\n  color: #ffd166;\n}\n\n.preis {\n  color: gold;\n}\n\n\
  .motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: rgb(255 255 255 / 0.08);\n}\n\n.karte li {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n  opacity: 0.6;\n}\n\n\
  #tagesangebot .preis {\n  color: orange;\n}\n\nh1 {\n  font-family: serif;\n  font-size: 40px;\n  text-align: center;\n\
  \  letter-spacing: 2px;\n}\n\n.motto {\n  font-style: italic;\n  text-align: center;\n}\n\nh2 {\n  font-size: 18px;\n  text-transform:\
  \ uppercase;\n}\n\n.preis {\n  font-weight: bold;\n}\n\n.karte .ausverkauft {\n  text-decoration: line-through;\n}\n"
---

Die Speisekarte wird ein richtiger Kasten mit goldenem Rahmen in der Mitte der Bühne. Dein CSS aus Kapitel 6 steht schon da.

## Vorgaben

- alle Elemente: `box-sizing: border-box`
- `h1`: Außenabstand `0`
- Klasse `karte`: Breite `440px`, Außenabstand `8px auto 0`, Innenabstand `4px 16px`, Rand `3px solid #ffd166`
- `h2`: Innenabstand `2px 8px`
