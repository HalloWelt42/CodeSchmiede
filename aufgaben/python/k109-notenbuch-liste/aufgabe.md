---
schema_version: 1
id: k109-notenbuch-liste
revision: 1
titel: 'Notenbuch: die Notenliste'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- liste
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beginne mit `noten = []` und hänge jede Note mit `noten = noten + [note]` an.
- kosten: 2
  text: Die Summe danach in einer for-Schleife über noten.
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: [2, 1, 3]

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - '1'
  - '2'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: [1, 2]

    Durchschnitt: 1.5

    Urteil: sehr gut

    Sterne: *****

    '
- input:
  - '4'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: [4]

    Durchschnitt: 4.0

    Urteil: ausreichend

    Sterne: ***

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nsumme = 0\nanzahl = 0\nwhile True:\n    note = int(input())\n    if note == 0:\n        break\n   \
  \ summe += note\n    anzahl += 1\nschnitt = summe / anzahl\nprint(\"Noten:\", anzahl)\nprint(\"Durchschnitt:\", schnitt)\n\
  if schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"Urteil: gut\")\nelif schnitt <= 3.5:\n\
  \    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\")\nelse:\n    print(\"Urteil:\
  \ nicht bestanden\")\nprint(\"Sterne: \", end=\"\")\nfor i in range(7 - round(schnitt)):\n    print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 10.** Dein Code aus Stück 9 steht schon da. Statt nur zu zählen, merkt sich das Notenbuch jetzt alle Noten in einer Liste `noten` und zeigt sie an. Bei `2`, `1`, `3`, `0`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Noten: [2, 1, 3]
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
