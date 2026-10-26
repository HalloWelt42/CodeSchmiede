---
schema_version: 1
id: w163-bezugsrahmen
revision: 1
titel: Der Bezugsrahmen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- position
- relative
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"karte\">\n  <p>Hering 4,50</p>\n  <p>Makrele 3,80</p>\n  <span class=\"marke\">Neu!</span>\n</div>\n"
ziel_css: ".karte {\n  position: relative;\n  width: 200px;\n  margin: 40px;\n  padding: 10px;\n  background-color: #2b3442;\n\
  }\n\n.marke {\n  position: absolute;\n  top: -14px;\n  right: -14px;\n  padding: 10px 18px;\n  font-size: 20px;\n  background-color:\
  \ crimson;\n  border-radius: 999px;\n}\n"
hints:
- kosten: 0
  text: Die Marke misst am ganzen Fenster, weil die Karte nicht positioniert ist.
- kosten: 2
  text: '.karte bekommt position: relative;'
starter_code: ".karte {\n  width: 200px;\n  margin: 40px;\n  padding: 10px;\n  background-color: #2b3442;\n}\n\n.marke {\n\
  \  position: absolute;\n  top: -14px;\n  right: -14px;\n  padding: 10px 18px;\n  font-size: 20px;\n  background-color: crimson;\n\
  \  border-radius: 999px;\n}\n"
---

Die Marke Neu! soll über der oberen rechten Ecke der Karte kleben, sie landet aber außerhalb der Bühne. Mach die Karte zum Bezugsrahmen.

## Vorgaben

- Klasse `karte`: `position: relative`, alles andere bleibt
