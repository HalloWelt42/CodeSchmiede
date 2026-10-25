---
schema_version: 1
id: k048-namensschild
revision: 1
titel: Das Namensschild
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- text
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein f-String für den ganzen Namen, dann `.upper()`.
- kosten: 2
  text: 'Initialen: `vorname[0]` und `nachname[0]` im f-String.'
tests_sichtbar:
- input: []
  expected: 'PIA PINGUIN

    P.P.

    Vorname: 3 Buchstaben

    '
starter_code: 'vorname = "Pia"

  nachname = "Pinguin"

  '
---

Baue aus Vor- und Nachname ein Namensschild: der Name in Großbuchstaben, darunter die Initialen mit Punkt und die Anzahl der Buchstaben im Vornamen:

```
PIA PINGUIN
P.P.
Vorname: 3 Buchstaben
```
