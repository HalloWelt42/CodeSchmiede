---
schema_version: 1
id: k194-gedicht-zaehlen
revision: 1
titel: Das Gedicht zählen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- datei
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`len(zeile.split())` ist die Zahl der Wörter einer Zeile.'
tests_sichtbar:
- input: []
  expected: 'Zeilen: 3

    Wörter: 12

    '
starter_code: "with open(\"gedicht.txt\", \"w\") as datei:\n    datei.write(\"Ein Pinguin im Schnee\\n\")\n    datei.write(\"\
  trinkt am Morgen Tee\\n\")\n    datei.write(\"und ruft dann juchhe\\n\")\n"
---

Der Anfang schreibt ein Gedicht in `gedicht.txt`. Lies die Datei und zähle Zeilen und Wörter; die Wörter einer Zeile liefert `split()`.

```
Zeilen: 3
Wörter: 12
```
