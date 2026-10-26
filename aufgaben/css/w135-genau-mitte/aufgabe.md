---
schema_version: 1
id: w135-genau-mitte
revision: 1
titel: Genau in der Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- zentrieren
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"rahmen\">\n  <div class=\"schild\">Geöffnet</div>\n</div>\n"
ziel_css: ".rahmen {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 300px;\n  background-color:\
  \ #2b3442;\n}\n\n.schild {\n  padding: 20px 40px;\n  background-color: #ffd166;\n  color: #2b3442;\n  border-radius: 8px;\n\
  }\n"
hints:
- kosten: 0
  text: Der Rahmen wird Flex-Behälter und zentriert auf beiden Achsen.
- kosten: 2
  text: 'display: flex; justify-content: center; align-items: center;'
starter_code: ".rahmen {\n  height: 300px;\n  background-color: #2b3442;\n}\n\n.schild {\n  padding: 20px 40px;\n  background-color:\
  \ #ffd166;\n  color: #2b3442;\n  border-radius: 8px;\n}\n"
---

Das Schild soll genau in der Mitte des Rahmens hängen, waagerecht und senkrecht.

## Vorgaben

- Klasse `rahmen`: Flex-Behälter, auf beiden Achsen zentriert
