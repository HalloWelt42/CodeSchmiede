---
schema_version: 1
id: k192-dranhaengen
revision: 1
titel: Dranhängen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- datei
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Anhängen heißt append, der Modus ist `"a"`.
tests_sichtbar:
- input: []
  expected: 'Montag

    Dienstag

    '
starter_code: "with open(\"tage.txt\", \"w\") as datei:\n    datei.write(\"Montag\\n\")\nwith open(\"tage.txt\", ___) as datei:\n\
  \    datei.write(\"Dienstag\\n\")\nwith open(\"tage.txt\") as datei:\n    print(datei.read())\n"
---

Ergänze die Lücke `___` mit dem Modus, damit der Dienstag angehängt wird und der Montag stehen bleibt:

```
Montag
Dienstag
```
