---
schema_version: 1
id: k072-else-ergaenzen
revision: 1
titel: Der andere Fall
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Das Wort für sonst, mit Doppelpunkt.
tests_sichtbar:
- input:
  - Regen
  expected: 'Schirm!

    '
tests_versteckt:
- input:
  - Sonne
  expected: 'Sonnenbrille!

    '
starter_code: "wetter = input()\nif wetter == \"Sonne\":\n    print(\"Sonnenbrille!\")\n___:\n    print(\"Schirm!\")\n"
---

Ergänze das fehlende Wort, damit bei Regen `Schirm!` erscheint. Die Eingabe ist das Wetter.
