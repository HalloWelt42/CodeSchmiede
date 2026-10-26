---
schema_version: 1
id: w039-speisekarte-bereiche
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
  notiz: Aufbaukurs CSS, Kapitel 3
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
  .motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n.ausverkauft {\n  color: gray;\n\
  }\n\n.karte h2 {\n  background-color: darkslateblue;\n}\n\n.karte > ul {\n  background-color: navy;\n}\n"
hints:
- kosten: 0
  text: Fasse die Regeln für h1 und h2 zu einer Gruppe zusammen, beide werden gold. Dann zwei neue Regeln für die Überschriften
    und Listen in der Karte.
- kosten: 3
  text: .karte h2 bekommt darkslateblue, .karte > ul bekommt navy.
starter_code: "body {\n  background-color: midnightblue;\n}\n\nh1 {\n  color: gold;\n}\n\nh2 {\n  color: skyblue;\n}\n\n.preis\
  \ {\n  color: gold;\n}\n\n.motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n.ausverkauft\
  \ {\n  color: gray;\n}\n"
---

Die Speisekarte hat Bereiche bekommen: Alles Essbare steckt jetzt in einem `div` mit der Klasse `karte`, und es gibt auch Getränke. Dein CSS aus Kapitel 2 steht schon da.

## Vorgaben

- `h1` und `h2` in einer Regel: Schriftfarbe `gold` (die Zwischenüberschriften werden also auch gold)
- `h2` in der Karte: Hintergrundfarbe `darkslateblue`
- `ul`, die direkte Kinder der Karte sind: Hintergrundfarbe `navy`
- alles Übrige bleibt wie in Kapitel 2
