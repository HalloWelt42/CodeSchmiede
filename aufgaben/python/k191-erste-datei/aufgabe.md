---
schema_version: 1
id: k191-erste-datei
revision: 1
titel: Die erste Datei
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
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
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'Hallo Datei

    '
starter_code: "with open(\"gruss.txt\", \"w\") as datei:\n    datei.write(\"Hallo Datei\\n\")\n\nwith open(\"gruss.txt\")\
  \ as datei:\n    print(datei.read())\n"
---

Der Code steht schon da: eine Datei wird geschrieben und wieder gelesen. Prüfe ihn.
