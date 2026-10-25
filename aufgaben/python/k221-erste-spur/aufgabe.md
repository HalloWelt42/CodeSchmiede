---
schema_version: 1
id: k221-erste-spur
revision: 1
titel: Die erste Spur
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- regex
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 22
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: '7

    '
starter_code: 'import re


  treffer = re.search(r"\d+", "Polly fing 7 Fische")

  print(treffer.group())

  '
---

Der Code steht schon da: ein Muster sucht die erste Zahl in einem Satz. Prüfe ihn.
