---
schema_version: 1
id: w184-strich-drunter
revision: 1
titel: Ein Strich als Schmuck
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- after
- schmuck
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Speisekarte</h2>

  <p>Heute frisch aus dem Eis.</p>

  '
ziel_css: "h2::after {\n  content: \"\";\n  display: block;\n  width: 80px;\n  height: 6px;\n  margin-top: 8px;\n  background-color:\
  \ gold;\n  border-radius: 3px;\n}\n"
hints:
- kosten: 0
  text: Der Strich ist ein leerer Kasten. Auch ein leerer Kasten braucht content.
- kosten: 2
  text: 'content: "";'
starter_code: "h2::after {\n  display: block;\n  width: 80px;\n  height: 6px;\n  margin-top: 8px;\n  background-color: gold;\n\
  \  border-radius: 3px;\n}\n"
---

Unter der Überschrift soll ein kurzer goldener Strich liegen. Pit hat alles gestaltet, aber der Strich erscheint nicht.

## Vorgaben

- `h2::after`: leerer Inhalt `""`, alles andere steht schon da
