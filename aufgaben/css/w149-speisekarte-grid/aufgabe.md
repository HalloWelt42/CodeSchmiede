---
schema_version: 1
id: w149-speisekarte-grid
revision: 1
titel: 'Speisekarte: Raster'
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
  notiz: Aufbaukurs CSS, Kapitel 14
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
  }\n\n.preis {\n  padding: 0 6px;\n  border: 1px dotted #ffd166;\n  border-radius: 999px;\n}\n\nh1 {\n  font-size: 2.25rem;\n\
  }\n\n.karte {\n  width: 80%;\n  max-width: 460px;\n}\n\nh2 {\n  font-size: 1rem;\n  padding: 0.25em 0.5em;\n}\n\n.preis\
  \ {\n  font-size: 0.9em;\n}\n\nbody {\n  background: linear-gradient(to bottom, #0b1d3a, #12305e);\n}\n\nh1 {\n  text-shadow:\
  \ 2px 2px 0 #2b1a4a;\n}\n\n.karte {\n  box-shadow: 0 8px 24px black;\n}\n\n.karte h2 {\n  background: linear-gradient(to\
  \ right, darkslateblue, transparent);\n}\n\nh2 {\n  display: inline-block;\n}\n\n.preis {\n  display: inline-block;\n  min-width:\
  \ 3.5em;\n  text-align: center;\n}\n\n.karte > ul {\n  display: flex;\n  flex-direction: column;\n  gap: 4px;\n}\n\n.karte\
  \ li {\n  display: flex;\n  gap: 12px;\n}\n\n.karte > ul {\n  padding: 0;\n}\n\n.karte li {\n  justify-content: space-between;\n\
  \  align-items: center;\n  padding: 0 8px;\n  border-bottom: 2px dotted #ffd166;\n}\n\n.karte > ul {\n  display: grid;\n\
  \  grid-template-columns: repeat(2, 1fr);\n  gap: 4px 16px;\n}\n"
hints:
- kosten: 0
  text: 'Eine neue Regel für die Listen in der Karte: ein Raster mit zwei gleichen Spalten statt der Flex-Spalte.'
- kosten: 3
  text: '.karte > ul { display: grid; grid-template-columns: repeat(2, 1fr); gap: 4px 16px; }'
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
  \  align-items: center;\n  padding: 0 8px;\n  border-bottom: 2px dotted #ffd166;\n}\n"
---

Die Gerichte stehen jetzt in zwei Spalten nebeneinander. Dein CSS aus Kapitel 13 steht schon da; die neue Regel ersetzt für die Listen display flex durch grid.

## Vorgaben

- Listen direkt in der Karte: Raster mit zwei gleichen Spalten, Lücke `4px 16px`
