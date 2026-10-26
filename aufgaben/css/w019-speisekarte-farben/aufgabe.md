---
schema_version: 1
id: w019-speisekarte-farben
revision: 1
titel: 'Speisekarte: erste Farben'
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
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h1>Zum frostigen Hering</h1>\n<p>Fisch, so frisch wie die Antarktis</p>\n<h2>Heute auf der Karte</h2>\n<ul>\n\
  \  <li>Hering im Eismantel <span>4,50</span></li>\n  <li>Makrele am Stiel <span>3,80</span></li>\n  <li>Eisscholle mit Sardinen\
  \ <span>5,20</span></li>\n</ul>\n"
ziel_css: "body {\n  background-color: midnightblue;\n}\n\nh1 {\n  color: gold;\n}\n\nh2 {\n  color: skyblue;\n}\n\nspan {\n\
  \  color: gold;\n}\n"
hints:
- kosten: 0
  text: Vier Regeln, je eine für body, h1, h2 und span.
- kosten: 3
  text: Die Preise stecken in span-Elementen.
starter_code: '/* Die Speisekarte des Fischwagens Zum frostigen Hering */

  '
---

Das Kapitelprojekt: Die Speisekarte des Fischwagens **Zum frostigen Hering** wird eine Webseite. Das HTML steht, jetzt kommt Farbe dazu. In den nächsten Kapiteln wächst die Karte weiter.

## Vorgaben

- ganze Bühne (`body`): Hintergrundfarbe `midnightblue`
- Hauptüberschrift (`h1`): Schriftfarbe `gold`
- Zwischenüberschrift (`h2`): Schriftfarbe `skyblue`
- Preise (`span`): Schriftfarbe `gold`
