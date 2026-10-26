---
schema_version: 1
id: w029-speisekarte-klassen
revision: 1
titel: 'Speisekarte: Klassen und ids'
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
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p class=\"motto\">Fisch, so frisch wie die Antarktis</p>\n<h2>Heute auf der Karte</h2>\n\
  <ul>\n  <li>Hering im Eismantel <span class=\"preis\">4,50</span></li>\n  <li id=\"tagesangebot\">Makrele am Stiel <span\
  \ class=\"preis\">3,80</span></li>\n  <li class=\"ausverkauft\">Eisscholle mit Sardinen <span class=\"preis\">5,20</span></li>\n\
  </ul>\n"
ziel_css: "body {\n  background-color: midnightblue;\n}\n\nh1 {\n  color: gold;\n}\n\nh2 {\n  color: skyblue;\n}\n\n.preis\
  \ {\n  color: gold;\n}\n\n.motto {\n  color: lightblue;\n}\n\n#tagesangebot {\n  background-color: darkgreen;\n}\n\n.ausverkauft\
  \ {\n  color: gray;\n}\n"
hints:
- kosten: 0
  text: 'Die Preise tragen jetzt die Klasse preis: span darf zu .preis werden. Dazu kommen Regeln für .motto, #tagesangebot
    und .ausverkauft.'
- kosten: 3
  text: Die ausverkaufte Eisscholle wird grau, ihr Preis bleibt gold, denn .preis gilt für den span selbst.
starter_code: "body {\n  background-color: midnightblue;\n}\n\nh1 {\n  color: gold;\n}\n\nh2 {\n  color: skyblue;\n}\n\nspan\
  \ {\n  color: gold;\n}\n"
---

Die Speisekarte hat Namensschilder bekommen: ein Motto, ein Tagesangebot und ein ausverkauftes Gericht. Dein CSS aus Kapitel 1 steht schon da, jetzt kommen die neuen Regeln dazu.

## Vorgaben

- wie bisher: Bühne `midnightblue`, `h1` gold, `h2` skyblue, Preise gold (jetzt über die Klasse `preis`)
- Klasse `motto`: Schriftfarbe `lightblue`
- id `tagesangebot`: Hintergrundfarbe `darkgreen`
- Klasse `ausverkauft`: Schriftfarbe `gray`
