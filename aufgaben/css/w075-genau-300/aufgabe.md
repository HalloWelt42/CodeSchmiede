---
schema_version: 1
id: w075-genau-300
revision: 1
titel: Genau 300 Pixel
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- kastenmodell
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="tafel">Tagesangebot</div>

  '
ziel_css: ".tafel {\n  width: 250px;\n  padding: 20px;\n  border: 5px solid white;\n  background-color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Von Rand zu Rand zählen width, zweimal padding und zweimal border. Rechne zurück, wie breit der Inhalt sein darf.
- kosten: 2
  text: 300 - 2 × 20 - 2 × 5 = 250
starter_code: ".tafel {\n  width: 300px;\n  padding: 20px;\n  border: 5px solid white;\n  background-color: #2b3442;\n}\n"
---

Die Tafel soll von Rand zu Rand genau 300 Pixel breit sein. Pit hat width 300 geschrieben, jetzt ist sie zu breit. Ändere nur die Breite, ohne box-sizing.

## Vorgaben

- Klasse `tafel`: von Rand zu Rand `300px` breit, Innenabstand `20px`, Rand `5px solid white`, Hintergrund `#2b3442`
