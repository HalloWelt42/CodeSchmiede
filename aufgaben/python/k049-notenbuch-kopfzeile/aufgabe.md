---
schema_version: 1
id: k049-notenbuch-kopfzeile
revision: 1
titel: 'Notenbuch: schöne Kopfzeile'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- projekt
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ersetze die erste print-Zeile durch einen f-String mit `titel.upper()` in den Klammern.
tests_sichtbar:
- input: []
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    '
starter_code: 'titel = "Mein Notenbuch"

  faecher = "Mathe, Deutsch, Musik"

  print("===", titel, "===")

  print("Fächer:", faecher)

  mathe = 2

  deutsch = 1

  musik = 3

  print("Durchschnitt:", (mathe + deutsch + musik) / 3)

  '
---

**Kapitelprojekt Notenbuch, Stück 4.** Dein Code aus Stück 3 steht schon da. Die erste Zeile soll jetzt mit einem f-String entstehen und den Titel in Großbuchstaben zeigen:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Durchschnitt: 2.0
```
