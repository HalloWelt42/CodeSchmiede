---
schema_version: 1
id: w028-wochenplan
revision: 1
titel: Der Wochenplan
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
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2 id=\"woche\">Fischwoche</h2>\n<ul>\n  <li class=\"tag\">Montag: Hering</li>\n  <li class=\"tag frei\">Dienstag:\
  \ Ruhetag</li>\n  <li class=\"tag\">Mittwoch: Makrele</li>\n</ul>\n<p class=\"frei\">Am Ruhetag angelt Pit selbst.</p>\n"
ziel_css: "#woche {\n  color: gold;\n}\n\n.tag {\n  color: lightgreen;\n}\n\nli.frei {\n  background-color: maroon;\n}\n"
hints:
- kosten: 0
  text: 'Drei Regeln: die Überschrift über ihre id, alle Tage über ihre Klasse, und nur der freie Listeneintrag über Element
    und Klasse zusammen.'
- kosten: 3
  text: 'Der Absatz trägt auch die Klasse frei, soll aber keinen Hintergrund bekommen: li.frei.'
starter_code: '/* Der Wochenplan des Fischwagens */

  '
---

Alles aus dem Kapitel: Gestalte den Wochenplan mit id, Klasse und Element mit Klasse.

## Vorgaben

- Überschrift mit der id `woche`: Schriftfarbe `gold`
- Klasse `tag`: Schriftfarbe `lightgreen`
- nur Listeneinträge mit der Klasse `frei`: Hintergrundfarbe `maroon` (der Absatz mit derselben Klasse bleibt ohne)
