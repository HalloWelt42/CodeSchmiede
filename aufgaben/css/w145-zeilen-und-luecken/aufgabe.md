---
schema_version: 1
id: w145-zeilen-und-luecken
revision: 1
titel: Zeilen und Lücken
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- grid-template-rows
- gap
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"plan\">\n  <div>Mo</div>\n  <div>Di</div>\n  <div>Mi</div>\n  <div>Hering</div>\n  <div>Ruhetag</div>\n\
  \  <div>Makrele</div>\n</div>\n"
ziel_css: ".plan {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  grid-template-rows: 40px 120px;\n  gap:\
  \ 6px;\n}\n\n.plan div {\n  background-color: teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n}\n"
hints:
- kosten: 0
  text: Die Tage oben flach, die Gerichte darunter hoch. Und überall 6 Pixel Lücke.
- kosten: 2
  text: "grid-template-rows: 40px 120px;\n  gap: 6px;"
starter_code: ".plan {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n}\n\n.plan div {\n  background-color:\
  \ teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n}\n"
---

Der Wochenplan braucht eine flache Kopfzeile und eine hohe Zeile für die Gerichte, dazu Lücken.

## Vorgaben

- Klasse `plan`: Zeilen `40px 120px`, Lücke `6px`
