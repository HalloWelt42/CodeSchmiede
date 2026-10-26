---
schema_version: 1
id: w065-mittig
revision: 1
titel: In die Mitte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- text-align
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Zum frostigen Hering</h1>

  <p class="motto">Seit 1999</p>

  <p class="preis">ab 3,80</p>

  '
ziel_css: "h1, .motto {\n  text-align: center;\n}\n\n.preis {\n  text-align: right;\n}\n"
hints:
- kosten: 0
  text: Überschrift und Motto in die Mitte, mit einer Gruppe. Der Preis nach rechts.
- kosten: 2
  text: 'h1, .motto { text-align: center; } und .preis { text-align: right; }'
starter_code: '/* Ausrichten */

  '
---

Das Schild soll ordentlich aussehen: Name und Motto in der Mitte, der Preis ganz rechts.

## Vorgaben

- `h1` und Klasse `motto`: Ausrichtung `center`
- Klasse `preis`: Ausrichtung `right`
