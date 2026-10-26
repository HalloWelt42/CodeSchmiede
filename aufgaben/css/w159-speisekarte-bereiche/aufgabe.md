---
schema_version: 1
id: w159-speisekarte-bereiche
revision: 1
titel: 'Speisekarte: Bereiche'
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
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p class=\"motto\">Fisch, so frisch wie die Antarktis</p>\n<div class=\"karte\"\
  >\n  <h2 class=\"titel-essen\">Heute auf der Karte</h2>\n  <ul class=\"essen\">\n    <li>Hering im Eismantel <span class=\"\
  preis\">4,50</span></li>\n    <li id=\"tagesangebot\">Makrele am Stiel <span class=\"preis\">3,80</span></li>\n    <li class=\"\
  ausverkauft\">Eisscholle mit Sardinen <span class=\"preis\">5,20</span></li>\n  </ul>\n  <h2 class=\"titel-trinken\">Getränke</h2>\n\
  \  <ul class=\"trinken\">\n    <li>Eiswasser <span class=\"preis\">1,00</span></li>\n  </ul>\n</div>\n"
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
  }\n\n.preis {\n  padding: 0 6px;\n  border: 1px dotted #ffd166;\n  border-radius: 999px;\n}\n\nh1 {\n  font-size: 2.25rem;\n\
  }\n\n.karte {\n  width: 80%;\n  max-width: 460px;\n}\n\nh2 {\n  font-size: 1rem;\n  padding: 0.25em 0.5em;\n}\n\n.preis\
  \ {\n  font-size: 0.9em;\n}\n\nbody {\n  background: linear-gradient(to bottom, #0b1d3a, #12305e);\n}\n\nh1 {\n  text-shadow:\
  \ 2px 2px 0 #2b1a4a;\n}\n\n.karte {\n  box-shadow: 0 8px 24px black;\n}\n\n.karte h2 {\n  background: linear-gradient(to\
  \ right, darkslateblue, transparent);\n}\n\nh2 {\n  display: inline-block;\n}\n\n.preis {\n  display: inline-block;\n  min-width:\
  \ 3.5em;\n  text-align: center;\n}\n\n.karte > ul {\n  display: flex;\n  flex-direction: column;\n  gap: 4px;\n}\n\n.karte\
  \ li {\n  display: flex;\n  gap: 12px;\n}\n\n.karte > ul {\n  padding: 0;\n}\n\n.karte li {\n  justify-content: space-between;\n\
  \  align-items: center;\n  padding: 0 8px;\n  border-bottom: 2px dotted #ffd166;\n}\n\n.karte > ul {\n  display: grid;\n\
  \  grid-template-columns: repeat(2, 1fr);\n  gap: 4px 16px;\n}\n\n.karte {\n  display: grid;\n  grid-template-columns: 2fr\
  \ 1fr;\n  grid-template-areas:\n    \"titel-essen titel-trinken\"\n    \"essen trinken\";\n  column-gap: 16px;\n  align-items:\
  \ start;\n}\n\n.titel-essen { grid-area: titel-essen; }\n.titel-trinken { grid-area: titel-trinken; }\n\n.karte .essen {\n\
  \  grid-area: essen;\n  grid-template-columns: 1fr;\n}\n\n.karte .trinken {\n  grid-area: trinken;\n  grid-template-columns:\
  \ 1fr;\n}\n"
hints:
- kosten: 0
  text: Die Karte wird ein Raster mit zwei Spalten und einem Plan; Überschriften und Listen haben jetzt Klassen und kommen
    in ihre Bereiche.
- kosten: 3
  text: Die Listen brauchen .karte .essen und .karte .trinken, damit ihre eine Spalte gegen .karte > ul aus Kapitel 14 gewinnt.
starter_code: "body {\n  background-color: #0b1d3a;\n}\n\nh1, h2 {\n  color: #ffd166;\n}\n\n.preis {\n  color: gold;\n}\n\n\
  .motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n\n.karte h2 {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte > ul {\n  background-color: rgb(255 255 255 / 0.08);\n}\n\n.karte li {\n  background-color:\
  \ darkslateblue;\n}\n\n.karte .ausverkauft {\n  color: lightgray;\n  background-color: dimgray;\n  opacity: 0.6;\n}\n\n\
  #tagesangebot .preis {\n  color: orange;\n}\n\nh1 {\n  font-family: serif;\n  font-size: 40px;\n  text-align: center;\n\
  \  letter-spacing: 2px;\n}\n\n.motto {\n  font-style: italic;\n  text-align: center;\n}\n\nh2 {\n  font-size: 18px;\n  text-transform:\
  \ uppercase;\n}\n\n.preis {\n  font-weight: bold;\n}\n\n.karte .ausverkauft {\n  text-decoration: line-through;\n}\n\n*\
  \ {\n  box-sizing: border-box;\n}\n\nh1 {\n  margin: 0;\n}\n\n.karte {\n  width: 440px;\n  margin: 8px auto 0;\n  padding:\
  \ 4px 16px;\n  border: 3px solid #ffd166;\n}\n\nh2 {\n  padding: 2px 8px;\n}\n\n.karte {\n  border-style: double;\n  border-width:\
  \ 6px;\n  border-radius: 16px;\n}\n\nh2 {\n  border-radius: 6px;\n}\n\n#tagesangebot {\n  border-left: 6px solid orange;\n\
  }\n\n.preis {\n  padding: 0 6px;\n  border: 1px dotted #ffd166;\n  border-radius: 999px;\n}\n\nh1 {\n  font-size: 2.25rem;\n\
  }\n\n.karte {\n  width: 80%;\n  max-width: 460px;\n}\n\nh2 {\n  font-size: 1rem;\n  padding: 0.25em 0.5em;\n}\n\n.preis\
  \ {\n  font-size: 0.9em;\n}\n\nbody {\n  background: linear-gradient(to bottom, #0b1d3a, #12305e);\n}\n\nh1 {\n  text-shadow:\
  \ 2px 2px 0 #2b1a4a;\n}\n\n.karte {\n  box-shadow: 0 8px 24px black;\n}\n\n.karte h2 {\n  background: linear-gradient(to\
  \ right, darkslateblue, transparent);\n}\n\nh2 {\n  display: inline-block;\n}\n\n.preis {\n  display: inline-block;\n  min-width:\
  \ 3.5em;\n  text-align: center;\n}\n\n.karte > ul {\n  display: flex;\n  flex-direction: column;\n  gap: 4px;\n}\n\n.karte\
  \ li {\n  display: flex;\n  gap: 12px;\n}\n\n.karte > ul {\n  padding: 0;\n}\n\n.karte li {\n  justify-content: space-between;\n\
  \  align-items: center;\n  padding: 0 8px;\n  border-bottom: 2px dotted #ffd166;\n}\n\n.karte > ul {\n  display: grid;\n\
  \  grid-template-columns: repeat(2, 1fr);\n  gap: 4px 16px;\n}\n"
---

Getränke gehören neben das Essen. Überschriften und Listen der Karte haben dafür Klassen bekommen. Dein CSS aus Kapitel 14 steht schon da.

## Vorgaben

- Klasse `karte`: Raster mit den Spalten `2fr 1fr`, Plan `"titel-essen titel-trinken" "essen trinken"`, Spaltenlücke `16px` (`column-gap`), Kinder oben ausgerichtet (`align-items: start`)
- `.titel-essen`, `.titel-trinken`: in ihre Bereiche
- Listen `.karte .essen` und `.karte .trinken`: in ihre Bereiche, je nur eine Spalte (`grid-template-columns: 1fr`)
