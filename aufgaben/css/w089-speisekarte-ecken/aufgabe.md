---
schema_version: 1
id: w089-speisekarte-ecken
revision: 1
titel: 'Speisekarte: Ecken'
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
  notiz: Aufbaukurs CSS, Kapitel 8
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
  \ 4px 16px;\n  border: 3px solid #ffd166;\n}\n\nh2 {\n  padding: 2px 8px;\n}\n\n.karte {\n  border-style: double;\n  border-width:\
  \ 6px;\n  border-radius: 16px;\n}\n\nh2 {\n  border-radius: 6px;\n}\n\n#tagesangebot {\n  border-left: 6px solid orange;\n\
  }\n\n.preis {\n  padding: 0 6px;\n  border: 1px dotted #ffd166;\n  border-radius: 999px;\n}\n"
hints:
- kosten: 0
  text: 'Vier neue Regeln am Ende: die Karte bekommt einen doppelten runden Rahmen, die Überschriften runde Ecken, das Tagesangebot
    einen Balken links, die Preise eine gepunktete Pille.'
- kosten: 3
  text: Für die Karte reichen border-style, border-width und border-radius; die Farbe des Randes bleibt aus Kapitel 7.
starter_code: "body {\n  background-color: #0b1d3a;\n}\n\nh1, h2 {\n  color: #ffd166;\n}\n\n.preis {\n  color: gold;\n}\n\n\
  .motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: rgb(255 255 255 / 0.08);\n}\n\n.karte li {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n  opacity: 0.6;\n}\n\n\
  #tagesangebot .preis {\n  color: orange;\n}\n\nh1 {\n  font-family: serif;\n  font-size: 40px;\n  text-align: center;\n\
  \  letter-spacing: 2px;\n}\n\n.motto {\n  font-style: italic;\n  text-align: center;\n}\n\nh2 {\n  font-size: 18px;\n  text-transform:\
  \ uppercase;\n}\n\n.preis {\n  font-weight: bold;\n}\n\n.karte .ausverkauft {\n  text-decoration: line-through;\n}\n\n*\
  \ {\n  box-sizing: border-box;\n}\n\nh1 {\n  margin: 0;\n}\n\n.karte {\n  width: 440px;\n  margin: 8px auto 0;\n  padding:\
  \ 4px 16px;\n  border: 3px solid #ffd166;\n}\n\nh2 {\n  padding: 2px 8px;\n}\n"
---

Die Speisekarte bekommt runde Ecken und feine Ränder. Dein CSS aus Kapitel 7 steht schon da.

## Vorgaben

- Klasse `karte`: Rand doppelt, `6px` breit, Eckenradius `16px` (die Farbe bleibt)
- `h2`: Eckenradius `6px`
- id `tagesangebot`: Rand links `6px solid orange`
- Klasse `preis`: Innenabstand `0 6px`, Rand `1px dotted #ffd166`, Eckenradius `999px`
