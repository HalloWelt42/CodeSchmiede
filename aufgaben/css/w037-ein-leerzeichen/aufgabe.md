---
schema_version: 1
id: w037-ein-leerzeichen
revision: 1
titel: Ein Leerzeichen zu wenig
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- nachfahre
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li class=\"neu\">Makrele am Stiel</li>\n  <li>Hering mit <span class=\"neu\">neuer Soße</span></li>\n\
  </ul>\n"
ziel_css: "li .neu {\n  background-color: purple;\n}\n"
hints:
- kosten: 0
  text: li.neu sind Listeneinträge mit der Klasse neu. Gemeint ist aber, was mit der Klasse neu in einem Listeneintrag steckt.
- kosten: 2
  text: li .neu {
starter_code: "li.neu {\n  background-color: purple;\n}\n"
---

Lila soll nur die neue Soße werden, also das Element mit der Klasse `neu`, das **in** einem Listeneintrag steckt. Pits Regel färbt stattdessen den ganzen ersten Eintrag.

## Vorgaben

- Elemente mit der Klasse `neu` in einem `li`: Hintergrundfarbe `purple`
- der Listeneintrag mit der Klasse `neu` selbst bleibt ohne Hintergrund
