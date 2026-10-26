---
schema_version: 1
id: w026-nur-listeneintraege
revision: 1
titel: Nur in der Liste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- klasse
- selektor
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<p class=\"ausverkauft\">Was heute schon weg ist:</p>\n<ul>\n  <li class=\"ausverkauft\">Eisscholle mit Sardinen</li>\n\
  \  <li>Hering im Eismantel</li>\n  <li class=\"ausverkauft\">Tintenfischringe</li>\n</ul>\n"
ziel_css: "li.ausverkauft {\n  color: gray;\n}\n"
hints:
- kosten: 0
  text: Im Moment wird auch der Absatz grau. Mit dem Namen des Elements vor der Klasse, ohne Leerzeichen, trifft die Regel
    nur Listeneinträge.
- kosten: 2
  text: li.ausverkauft {
starter_code: ".ausverkauft {\n  color: gray;\n}\n"
---

Ausverkaufte Gerichte sollen grau werden, aber nur in der Liste. Der Absatz darüber trägt dieselbe Klasse und soll hell bleiben.

## Vorgaben

- Listeneinträge (`li`) mit der Klasse `ausverkauft`: Schriftfarbe `gray`
- der Absatz behält seine helle Schrift
