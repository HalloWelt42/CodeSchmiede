---
schema_version: 1
id: w017-abschalten
revision: 1
titel: Zu viel Farbe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- kommentar
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischwagen</h1>

  <p>Frischer Hering, eiskalt serviert.</p>

  '
ziel_css: "h1 {\n  color: gold;\n}\n\np {\n  color: skyblue;\n}\n"
hints:
- kosten: 0
  text: Setz die Angabe mit dem pinken Hintergrund zwischen /* und */. Dann überliest der Browser sie.
- kosten: 2
  text: '/* background-color: hotpink; */'
starter_code: "h1 {\n  color: gold;\n  background-color: hotpink;\n}\n\np {\n  color: skyblue;\n}\n"
---

Pia findet den pinken Hintergrund der Überschrift scheußlich, Pit will ihn für den Fasching aufheben. Schalte die Angabe mit einem **Kommentar** ab, statt sie zu löschen.

## Vorgaben

- Überschrift (`h1`): Schriftfarbe `gold`, kein eigener Hintergrund (die Angabe bleibt als Kommentar stehen)
- Absätze (`p`): Schriftfarbe `skyblue`
