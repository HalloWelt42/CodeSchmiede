---
schema_version: 1
id: w102-harte-kante
revision: 1
titel: Harter Schatten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- box-shadow
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="karte">Comic-Fisch</div>

  '
ziel_css: ".karte {\n  width: 200px;\n  padding: 24px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 10px;\n  border: 3px solid black;\n  box-shadow: -8px 8px 0 crimson;\n}\n"
hints:
- kosten: 0
  text: Der Schatten soll nach links unten fallen und ganz scharf sein.
- kosten: 2
  text: 'box-shadow: -8px 8px 0 crimson;'
starter_code: ".karte {\n  width: 200px;\n  padding: 24px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 10px;\n  border: 3px solid black;\n  box-shadow: 8px 8px 8px crimson;\n}\n"
---

Wie im Comic: ein scharfer roter Schatten nach links unten, ohne Unschärfe.

## Vorgaben

- Klasse `karte`: Schatten `-8px 8px 0 crimson`, alles andere bleibt
