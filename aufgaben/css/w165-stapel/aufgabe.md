---
schema_version: 1
id: w165-stapel
revision: 1
titel: Wer liegt oben?
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- z-index
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"stapel\">\n  <div class=\"a\">Hering</div>\n  <div class=\"b\">Makrele</div>\n  <div class=\"c\"\
  >Sardine</div>\n</div>\n"
ziel_css: ".stapel {\n  position: relative;\n  height: 200px;\n}\n\n.stapel div {\n  position: absolute;\n  width: 140px;\n\
  \  height: 90px;\n  padding: 6px;\n}\n\n.stapel .a { top: 0; left: 0; background-color: teal; z-index: 3; }\n.stapel .b\
  \ { top: 30px; left: 60px; background-color: crimson; z-index: 2; }\n.stapel .c { top: 60px; left: 120px; background-color:\
  \ purple; }\n"
hints:
- kosten: 0
  text: Der Hering soll ganz oben liegen, die Makrele in der Mitte, die Sardine unten.
- kosten: 2
  text: 'z-index: 3 beim Hering, z-index: 2 bei der Makrele'
starter_code: ".stapel {\n  position: relative;\n  height: 200px;\n}\n\n.stapel div {\n  position: absolute;\n  width: 140px;\n\
  \  height: 90px;\n  padding: 6px;\n}\n\n.stapel .a { top: 0; left: 0; background-color: teal; }\n.stapel .b { top: 30px;\
  \ left: 60px; background-color: crimson; }\n.stapel .c { top: 60px; left: 120px; background-color: purple; }\n"
---

Der Stapel liegt verkehrt herum. Der Hering soll ganz oben liegen, darunter die Makrele, ganz unten die Sardine.

## Vorgaben

- `.stapel .a`: `z-index: 3`
- `.stapel .b`: `z-index: 2`
