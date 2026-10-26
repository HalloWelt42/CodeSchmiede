---
schema_version: 1
id: w205-kombiniert
revision: 1
titel: Alles auf einmal
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- transform
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="stempel">Geprüft</div>

  '
ziel_css: ".stempel {\n  width: 120px;\n  margin: 60px;\n  padding: 10px;\n  text-align: center;\n  border: 4px double crimson;\n\
  \  color: crimson;\n  transform: translate(60px, 20px) rotate(-20deg) scale(1.3);\n}\n"
hints:
- kosten: 0
  text: Drei Verwandlungen in einer Angabe, mit Leerzeichen dazwischen.
- kosten: 2
  text: 'transform: translate(60px, 20px) rotate(-20deg) scale(1.3);'
starter_code: ".stempel {\n  width: 120px;\n  margin: 60px;\n  padding: 10px;\n  text-align: center;\n  border: 4px double\
  \ crimson;\n  color: crimson;\n}\n"
---

Pias Stempel landet verschoben, gedreht und etwas zu groß auf dem Zettel.

## Vorgaben

- Klasse `stempel`: `translate(60px, 20px) rotate(-20deg) scale(1.3)` in dieser Reihenfolge
