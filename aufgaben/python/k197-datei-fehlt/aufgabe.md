---
schema_version: 1
id: k197-datei-fehlt
revision: 1
titel: Die fehlende Datei
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- datei
- ausnahme
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Das open gehört in den try-Block.
- kosten: 2
  text: '`datei.readlines()` liefert eine Liste der Zeilen.'
tests_sichtbar:
- input:
  - da.txt
  expected: 'da.txt hat 2 Zeilen

    '
- input:
  - weg.txt
  expected: 'weg.txt gibt es nicht

    '
tests_versteckt:
- input:
  - nichts.txt
  expected: 'nichts.txt gibt es nicht

    '
starter_code: "with open(\"da.txt\", \"w\") as datei:\n    datei.write(\"eins\\nzwei\\n\")\n"
---

Der Anfang legt `da.txt` mit zwei Zeilen an. Lies einen Dateinamen ein und gib aus, wie viele Zeilen die Datei hat. Gibt es sie nicht, fange den `FileNotFoundError` ab. Bei `da.txt`:

```
da.txt hat 2 Zeilen
```

Bei `weg.txt`:

```
weg.txt gibt es nicht
```
