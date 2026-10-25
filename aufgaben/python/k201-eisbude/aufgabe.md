---
schema_version: 1
id: k201-eisbude
revision: 1
titel: Die Eisbude
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
tests_sichtbar:
- input: []
  expected: 'Strand 12

    '
starter_code: "class Eisbude:\n    def __init__(self, ort):\n        self.ort = ort\n        self.kugeln = 0\n\n\nbude = Eisbude(\"\
  Strand\")\nbude.kugeln = 12\nprint(bude.ort, bude.kugeln)\n"
---

Der Code steht schon da: ein Bauplan für Eisbuden und ein Objekt daraus. Prüfe ihn und schau ins Speicherbild.
