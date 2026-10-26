---
schema_version: 1
id: w113-kacheln
revision: 1
titel: Kacheln
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- display
- inline-block
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="kachel">Hering</div>

  <div class="kachel">Makrele</div>

  <div class="kachel">Sardine</div>

  <div class="kachel">Thunfisch</div>

  <div class="kachel">Lachs</div>

  <div class="kachel">Scholle</div>

  '
ziel_css: ".kachel {\n  display: inline-block;\n  width: 160px;\n  height: 80px;\n  margin: 6px;\n  background-color: #1f6f8b;\n\
  \  border-radius: 8px;\n}\n"
hints:
- kosten: 0
  text: Die Kacheln sollen nebeneinander stehen und trotzdem ihre Größe behalten.
- kosten: 2
  text: 'display: inline-block;'
starter_code: ".kachel {\n  width: 160px;\n  height: 80px;\n  margin: 6px;\n  background-color: #1f6f8b;\n  border-radius:\
  \ 8px;\n}\n"
---

Die Kacheln stehen untereinander. Sie sollen nebeneinander stehen, drei in einer Reihe, und dabei ihre Größe behalten.

## Vorgaben

- Klasse `kachel`: `display: inline-block`, alles andere bleibt
