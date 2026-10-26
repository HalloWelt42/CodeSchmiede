---
schema_version: 1
id: w204-am-nagel
revision: 1
titel: Am Nagel
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- transform-origin
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="schild">Bin gleich zurück</div>

  '
ziel_css: ".schild {\n  width: 180px;\n  margin: 50px;\n  padding: 14px;\n  text-align: center;\n  background-color: #ffd166;\n\
  \  color: #2b3442;\n  transform: rotate(15deg);\n  transform-origin: top left;\n}\n"
hints:
- kosten: 0
  text: Das Schild dreht sich um seine Mitte. Es hängt aber an einem Nagel oben links.
- kosten: 2
  text: 'transform-origin: top left;'
starter_code: ".schild {\n  width: 180px;\n  margin: 50px;\n  padding: 14px;\n  text-align: center;\n  background-color: #ffd166;\n\
  \  color: #2b3442;\n  transform: rotate(15deg);\n}\n"
---

Das Schild hängt an einem Nagel in der oberen linken Ecke und ist abgerutscht. Es soll sich also um diese Ecke drehen, nicht um seine Mitte.

## Vorgaben

- Klasse `schild`: Drehpunkt `top left`, die Drehung steht schon da
