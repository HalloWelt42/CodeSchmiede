---
schema_version: 1
id: w219-speisekarte-fertig
revision: 1
titel: 'Speisekarte: fertig für jeden Bildschirm'
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- projekt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p class=\"motto\">Fisch, so frisch wie die Antarktis</p>\n<div class=\"karte\"\
  >\n  <span class=\"aufkleber\">Täglich frisch</span>\n  <h2 class=\"titel-essen\">Heute auf der Karte</h2>\n  <ul class=\"\
  essen\">\n    <li>Hering im Eismantel <span class=\"preis\">4,50</span></li>\n    <li id=\"tagesangebot\">Makrele am Stiel\
  \ <span class=\"preis\">3,80</span></li>\n    <li class=\"ausverkauft\">Eisscholle mit Sardinen <span class=\"preis\">5,20</span></li>\n\
  \  </ul>\n  <h2 class=\"titel-trinken\">Getränke</h2>\n  <ul class=\"trinken\">\n    <li>Eiswasser <span class=\"preis\"\
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
  \  grid-template-columns: repeat(2, 1fr);\n  gap: 4px 16px;\n}\n\n.karte {\n  display: grid;\n  grid-template-columns: 2fr\
  \ 1fr;\n  grid-template-areas:\n    \"titel-essen titel-trinken\"\n    \"essen trinken\";\n  column-gap: 16px;\n  align-items:\
  \ start;\n}\n\n.titel-essen { grid-area: titel-essen; }\n.titel-trinken { grid-area: titel-trinken; }\n\n.karte .essen {\n\
  \  grid-area: essen;\n  grid-template-columns: 1fr;\n}\n\n.karte .trinken {\n  grid-area: trinken;\n  grid-template-columns:\
  \ 1fr;\n}\n\n.karte {\n  position: relative;\n}\n\n.aufkleber {\n  position: absolute;\n  top: -18px;\n  right: -18px;\n\
  \  z-index: 1;\n  padding: 6px 12px;\n  font-weight: bold;\n  color: white;\n  background-color: crimson;\n  border-radius:\
  \ 999px;\n  box-shadow: 0 3px 8px black;\n}\n\n.karte li:not(.ausverkauft):not(#tagesangebot) {\n  background-color: #0f5257;\n\
  }\n\n.karte li:last-child {\n  border-bottom: none;\n}\n\n.karte h2:first-of-type {\n  color: white;\n}\n\n.karte::after\
  \ {\n  content: \"Alle Preise in Euro\";\n  grid-column: 1 / -1;\n  font-size: 12px;\n  color: gray;\n}\n\nh1::first-letter\
  \ {\n  color: white;\n  font-size: 1.3em;\n}\n\n.motto::before {\n  content: \"~ \";\n}\n\n.motto::after {\n  content: \"\
  \ ~\";\n}\n\n:root {\n  --akzent: #7dd3fc;\n  --abstand: 16px;\n}\n\nh1, h2 {\n  color: var(--akzent);\n}\n\n.karte {\n\
  \  border-color: var(--akzent);\n  padding: calc(var(--abstand) / 2) var(--abstand);\n}\n\n.karte {\n  transform: rotate(-1.5deg);\n\
  }\n\n.aufkleber {\n  transform: rotate(12deg) scale(1.1);\n}\n\n@media (min-width: 500px) {\n  h1 {\n    font-size: 2.6rem;\n\
  \    letter-spacing: 4px;\n  }\n\n  .karte {\n    max-width: 520px;\n  }\n}\n"
hints:
- kosten: 0
  text: 'Eine Media Query ans Ende: ab 500 Pixeln wird der Name größer und gesperrt, und die Karte darf breiter werden.'
- kosten: 3
  text: '@media (min-width: 500px) { h1 { font-size: 2.6rem; letter-spacing: 4px; } .karte { max-width: 520px; } }'
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
  \  grid-template-columns: repeat(2, 1fr);\n  gap: 4px 16px;\n}\n\n.karte {\n  display: grid;\n  grid-template-columns: 2fr\
  \ 1fr;\n  grid-template-areas:\n    \"titel-essen titel-trinken\"\n    \"essen trinken\";\n  column-gap: 16px;\n  align-items:\
  \ start;\n}\n\n.titel-essen { grid-area: titel-essen; }\n.titel-trinken { grid-area: titel-trinken; }\n\n.karte .essen {\n\
  \  grid-area: essen;\n  grid-template-columns: 1fr;\n}\n\n.karte .trinken {\n  grid-area: trinken;\n  grid-template-columns:\
  \ 1fr;\n}\n\n.karte {\n  position: relative;\n}\n\n.aufkleber {\n  position: absolute;\n  top: -18px;\n  right: -18px;\n\
  \  z-index: 1;\n  padding: 6px 12px;\n  font-weight: bold;\n  color: white;\n  background-color: crimson;\n  border-radius:\
  \ 999px;\n  box-shadow: 0 3px 8px black;\n}\n\n.karte li:not(.ausverkauft):not(#tagesangebot) {\n  background-color: #0f5257;\n\
  }\n\n.karte li:last-child {\n  border-bottom: none;\n}\n\n.karte h2:first-of-type {\n  color: white;\n}\n\n.karte::after\
  \ {\n  content: \"Alle Preise in Euro\";\n  grid-column: 1 / -1;\n  font-size: 12px;\n  color: gray;\n}\n\nh1::first-letter\
  \ {\n  color: white;\n  font-size: 1.3em;\n}\n\n.motto::before {\n  content: \"~ \";\n}\n\n.motto::after {\n  content: \"\
  \ ~\";\n}\n\n:root {\n  --akzent: #7dd3fc;\n  --abstand: 16px;\n}\n\nh1, h2 {\n  color: var(--akzent);\n}\n\n.karte {\n\
  \  border-color: var(--akzent);\n  padding: calc(var(--abstand) / 2) var(--abstand);\n}\n\n.karte {\n  transform: rotate(-1.5deg);\n\
  }\n\n.aufkleber {\n  transform: rotate(12deg) scale(1.1);\n}\n"
---

Das letzte Stück: Auf breiten Bildschirmen zeigt sich die Speisekarte großzügiger. Dein CSS aus Kapitel 20 steht schon da. Danach ist die Speisekarte des Fischwagens Zum frostigen Hering fertig, Pit und Pia bedanken sich mit einem Hering im Eismantel.

## Vorgaben

- ab `min-width: 500px`: `h1` Schriftgröße `2.6rem` und Buchstabenabstand `4px`, `.karte` höchstens `520px` breit
