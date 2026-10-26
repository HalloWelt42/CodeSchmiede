---
schema_version: 1
id: w015-liste
revision: 1
titel: Bunte Einkaufsliste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
tags:
- kurs
- liste
- color
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2>Einkaufsliste</h2>\n<ul>\n  <li>Eis</li>\n  <li>Hering</li>\n  <li>Noch mehr Eis</li>\n</ul>\n"
ziel_css: "h2 {\n  color: skyblue;\n}\n\nli {\n  color: lightgreen;\n}\n"
hints:
- kosten: 0
  text: Jeder Eintrag ist ein li-Element. Eine Regel mit dem Selektor li färbt alle Einträge.
- kosten: 2
  text: "li {\n  color: lightgreen;\n}"
starter_code: "h2 {\n  color: skyblue;\n}\n"
---

Pias Einkaufsliste soll frisch aussehen: Alle Einträge werden hellgrün. Die Punkte vor den Einträgen färben sich übrigens mit.

## Vorgaben

- Überschrift (`h2`): Schriftfarbe `skyblue` (steht schon da)
- Listeneinträge (`li`): Schriftfarbe `lightgreen`
