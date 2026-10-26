---
schema_version: 1
id: w025-mehrere-klassen
revision: 1
titel: Preis im Angebot
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Hering <span class="preis">4,50</span></p>

  <p>Makrele <span class="preis angebot">2,90</span></p>

  <p>Sardinen <span class="preis">5,20</span></p>

  '
ziel_css: ".preis {\n  color: gold;\n}\n\n.angebot {\n  background-color: crimson;\n}\n"
hints:
- kosten: 0
  text: Der Preis der Makrele trägt zwei Klassen. Für die zweite Klasse kommt eine zweite Regel dazu.
- kosten: 2
  text: ".angebot {\n  background-color: crimson;\n}"
starter_code: ".preis {\n  color: gold;\n}\n"
---

Alle Preise sind gold. Der Preis im Angebot trägt zusätzlich die Klasse `angebot` und soll auf rotem Grund stehen.

## Vorgaben

- Klasse `preis`: Schriftfarbe `gold` (steht schon da)
- Klasse `angebot`: Hintergrundfarbe `crimson`
