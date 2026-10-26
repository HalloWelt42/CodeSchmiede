---
schema_version: 1
id: w118-regal
revision: 1
titel: Das Regal
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<h2>Regal</h2>\n<ul class=\"brett\">\n  <li>Sardinen</li>\n  <li>Thunfisch</li>\n  <li class=\"weg\">Hering</li>\n\
  \  <li>Muscheln</li>\n</ul>\n<p>Zuständig: <span class=\"name\">Pit</span></p>\n"
ziel_css: ".brett li {\n  display: inline-block;\n  width: 110px;\n  height: 70px;\n  margin: 4px;\n  background-color: #c98c55;\n\
  \  color: #2b3442;\n}\n\n.brett .weg {\n  display: none;\n}\n\n.name {\n  display: block;\n  width: 120px;\n  padding: 6px;\n\
  \  background-color: teal;\n}\n"
hints:
- kosten: 0
  text: 'Drei Regeln: die Dosen nebeneinander mit fester Größe, den Hering ganz weg, den Namen als eigenen Kasten.'
- kosten: 3
  text: 'Die Dosen sind li in der Liste brett: .brett li mit display inline-block. Damit display none für den Hering gewinnt,
    muss sein Selektor genauer sein: .brett .weg.'
starter_code: '/* Ordnung im Regal */

  '
---

Alles aus dem Kapitel in einem Regal.

## Vorgaben

- Einträge der Liste `brett`: `inline-block`, Breite `110px`, Höhe `70px`, Außenabstand `4px`, Hintergrund `#c98c55`, Schrift `#2b3442`
- Klasse `weg` im Brett (`.brett .weg`, genauer als `.brett li`): ganz ausgeblendet
- Klasse `name`: `block`, Breite `120px`, Polster `6px`, Hintergrund `teal`
