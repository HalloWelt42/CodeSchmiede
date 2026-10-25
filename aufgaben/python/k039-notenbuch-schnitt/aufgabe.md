---
schema_version: 1
id: k039-notenbuch-schnitt
revision: 1
titel: 'Notenbuch: der Durchschnitt'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- projekt
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zusammenzählen in Klammern, dann durch 3 teilen.
tests_sichtbar:
- input: []
  expected: '=== Mein Notenbuch ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    '
starter_code: 'titel = "Mein Notenbuch"

  faecher = "Mathe, Deutsch, Musik"

  print("===", titel, "===")

  print("Fächer:", faecher)

  '
---

**Kapitelprojekt Notenbuch, Stück 3.** Dein Code aus Stück 2 steht schon da. Lege darunter die Noten an, `mathe` mit 2, `deutsch` mit 1, `musik` mit 3, und gib als dritte Zeile den Durchschnitt aus:

```
=== Mein Notenbuch ===
Fächer: Mathe, Deutsch, Musik
Durchschnitt: 2.0
```
