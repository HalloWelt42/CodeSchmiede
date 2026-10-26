---
schema_version: 1
id: w046-hintergrund-erbt-nicht
revision: 1
titel: Jeder sein eigener Hintergrund
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- vererbung
- background-color
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardinen</li>\n</ul>\n"
ziel_css: "li {\n  background-color: teal;\n}\n"
hints:
- kosten: 0
  text: Der Hintergrund der Liste liegt auch unter den Punkten links. Gemeint sind nur die Einträge selbst.
- kosten: 2
  text: "li {\n  background-color: teal;\n}"
starter_code: "ul {\n  background-color: teal;\n}\n"
---

Pit hat der ganzen Liste einen Hintergrund gegeben. Der reicht aber bis unter die Punkte. Nur die Einträge selbst sollen türkis sein. Hintergründe werden nicht vererbt, also braucht jeder Eintrag seinen eigenen.

## Vorgaben

- Listeneinträge (`li`): Hintergrundfarbe `teal`
- die Liste selbst (`ul`) bleibt ohne Hintergrund
