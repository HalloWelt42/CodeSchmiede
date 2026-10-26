---
schema_version: 1
id: w208-wimpel
revision: 1
titel: Die Wimpelkette
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kette\">\n  <div>F</div><div>E</div><div>S</div><div>T</div>\n</div>\n"
ziel_css: ".kette {\n  display: flex;\n  gap: 16px;\n  margin: 40px;\n}\n\n.kette div {\n  width: 50px;\n  height: 60px;\n\
  \  text-align: center;\n  font-size: 24px;\n  background-color: crimson;\n  transform-origin: top center;\n}\n\n.kette div:nth-child(odd)\
  \ {\n  transform: rotate(-8deg);\n  background-color: #ffd166;\n  color: #2b3442;\n}\n\n.kette div:nth-child(even) {\n \
  \ transform: rotate(8deg) translate(0, 6px);\n}\n"
hints:
- kosten: 0
  text: Alle Wimpel hängen oben in der Mitte und drehen sich abwechselnd nach links und rechts.
- kosten: 3
  text: 'transform-origin: top center für alle; ungerade rotate(-8deg), gerade rotate(8deg) translate(0, 6px)'
starter_code: '/* Die Wimpelkette */

  '
---

Alles aus dem Kapitel: die Wimpelkette für das Fischfest.

## Vorgaben

- Klasse `kette`: Flex-Behälter, Lücke `16px`, Außenabstand `40px`
- Wimpel (`.kette div`): Breite `50px`, Höhe `60px`, Text mittig `24px`, Hintergrund `crimson`, Drehpunkt `top center`
- ungerade Wimpel: Drehung `-8deg`, Hintergrund `#ffd166`, Schrift `#2b3442`
- gerade Wimpel: `rotate(8deg) translate(0, 6px)`
