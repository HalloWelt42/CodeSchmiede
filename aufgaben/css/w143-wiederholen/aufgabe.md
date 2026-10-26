---
schema_version: 1
id: w143-wiederholen
revision: 1
titel: Viermal dasselbe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- repeat
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"galerie\">\n  <div>1</div>\n  <div>2</div>\n  <div>3</div>\n  <div>4</div>\n  <div>5</div>\n  <div>6</div>\n\
  \  <div>7</div>\n  <div>8</div>\n</div>\n"
ziel_css: ".galerie {\n  display: grid;\n  grid-template-columns: repeat(4, 1fr);\n}\n\n.galerie div {\n  background-color:\
  \ teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 60px;\n}\n"
hints:
- kosten: 0
  text: Vier gleiche Spalten statt zwei.
- kosten: 2
  text: 'grid-template-columns: repeat(4, 1fr);'
starter_code: ".galerie {\n  display: grid;\n  grid-template-columns: repeat(2, 1fr);\n}\n\n.galerie div {\n  background-color:\
  \ teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n  height: 60px;\n}\n"
---

Die Galerie hat zwei Spalten und ist darum viel zu hoch. Mach vier gleich breite daraus.

## Vorgaben

- Klasse `galerie`: vier gleiche Spalten mit `repeat`
