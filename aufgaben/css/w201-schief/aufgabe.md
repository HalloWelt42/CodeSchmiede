---
schema_version: 1
id: w201-schief
revision: 1
titel: Ein schiefes Schild
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- rotate
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="schild">Geöffnet</div>

  '
ziel_css: ".schild {\n  width: 180px;\n  margin: 50px;\n  padding: 14px;\n  text-align: center;\n  background-color: #ffd166;\n\
  \  color: #2b3442;\n  transform: rotate(-8deg);\n}\n"
hints:
- kosten: 0
  text: Gegen den Uhrzeigersinn heißt negativer Winkel.
- kosten: 2
  text: 'transform: rotate(-8deg);'
starter_code: ".schild {\n  width: 180px;\n  margin: 50px;\n  padding: 14px;\n  text-align: center;\n  background-color: #ffd166;\n\
  \  color: #2b3442;\n}\n"
---

Das Schild hängt am Fischwagen ein wenig schief, 8 Grad gegen den Uhrzeigersinn. Gerade so viel, dass es gemütlich aussieht.

## Vorgaben

- Klasse `schild`: Drehung `-8deg`
