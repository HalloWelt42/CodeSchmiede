---
schema_version: 1
id: k196-punkteliste
revision: 1
titel: Die Punkteliste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
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
  text: '`name, punkte = zeile.strip().split(";")` und dann `int(punkte)`.'
tests_sichtbar:
- input: []
  expected: 'Bester: Pia mit 42

    Summe: 67

    '
starter_code: "with open(\"punkte.txt\", \"w\") as datei:\n    datei.write(\"Pit;17\\nPia;42\\nPaul;8\\n\")\n"
---

Der Anfang schreibt eine Punkteliste in `punkte.txt`, je Zeile `Name;Punkte`. Lies sie, zerlege jede Zeile mit `split(";")` und gib den Besten und die Summe aus:

```
Bester: Pia mit 42
Summe: 67
```
