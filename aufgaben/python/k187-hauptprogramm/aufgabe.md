---
schema_version: 1
id: k187-hauptprogramm
revision: 1
titel: Das Hauptprogramm
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- modul
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ganz unten: `if __name__ == "__main__":` und darunter eingerückt `main()`.'
tests_sichtbar:
- input:
  - Polly
  expected: 'Willkommen an Bord, Polly!

    '
tests_versteckt:
- input:
  - Pit
  expected: 'Willkommen an Bord, Pit!

    '
starter_code: ''
---

Baue das Programm so, dass es auch als Modul taugt: eine Funktion `begruessung(name)` gibt den Gruß zurück, eine Funktion `main()` liest den Namen ein und gibt ihn aus, und gestartet wird mit `if __name__ == "__main__":`. Bei `Polly`:

```
Willkommen an Bord, Polly!
```
