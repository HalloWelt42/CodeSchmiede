---
schema_version: 1
id: k079-notenbuch-urteil
revision: 1
titel: 'Notenbuch: das Urteil'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
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
  text: Eine elif-Kette vom besten zum schlechtesten Urteil.
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 2.0

    Urteil: gut

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  - '2'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 1.3333333333333333

    Urteil: sehr gut

    '
- input:
  - '4'
  - '4'
  - '3'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 3.6666666666666665

    Urteil: ausreichend

    '
- input:
  - '5'
  - '5'
  - '5'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Durchschnitt: 5.0

    Urteil: nicht bestanden

    '
starter_code: 'titel = "Mein Notenbuch"

  faecher = "Mathe, Deutsch, Musik"

  print(f"=== {titel.upper()} ===")

  print("Fächer:", faecher)

  mathe = int(input())

  deutsch = int(input())

  musik = int(input())

  schnitt = (mathe + deutsch + musik) / 3

  print("Durchschnitt:", schnitt)

  print("Bestanden:", schnitt <= 4)

  '
---

**Kapitelprojekt Notenbuch, Stück 7.** Dein Code aus Stück 6 steht schon da. Ersetze die Zeile mit `Bestanden:` durch ein Urteil: bis 1,5 `Urteil: sehr gut`, bis 2,5 `Urteil: gut`, bis 3,5 `Urteil: befriedigend`, bis 4 `Urteil: ausreichend`, darüber `Urteil: nicht bestanden`. Bei `2`, `1`, `3`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Durchschnitt: 2.0
Urteil: gut
```
