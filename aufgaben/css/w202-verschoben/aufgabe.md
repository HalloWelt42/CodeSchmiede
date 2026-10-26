---
schema_version: 1
id: w202-verschoben
revision: 1
titel: Ein Stück zur Seite
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- translate
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="kiste">Hering</div>

  <div class="kiste mitte">Makrele</div>

  <div class="kiste">Sardine</div>

  '
ziel_css: ".kiste {\n  width: 180px;\n  padding: 10px;\n  margin-bottom: 6px;\n  background-color: teal;\n}\n\n.kiste.mitte\
  \ {\n  transform: translate(120px, 0);\n  background-color: crimson;\n}\n"
hints:
- kosten: 0
  text: 120 Pixel nach rechts, nicht nach unten.
- kosten: 2
  text: 'transform: translate(120px, 0);'
starter_code: ".kiste {\n  width: 180px;\n  padding: 10px;\n  margin-bottom: 6px;\n  background-color: teal;\n}\n\n.kiste.mitte\
  \ {\n  background-color: crimson;\n}\n"
---

Die mittlere Kiste soll 120 Pixel nach rechts rutschen, ohne dass die anderen sich bewegen.

## Vorgaben

- `.kiste.mitte`: Verschiebung `translate(120px, 0)`
