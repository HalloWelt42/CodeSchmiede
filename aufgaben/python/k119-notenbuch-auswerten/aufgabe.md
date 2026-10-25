---
schema_version: 1
id: k119-notenbuch-auswerten
revision: 1
titel: 'Notenbuch: auswerten'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- projekt
- auswerten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`noten.append(note)`, `sum(noten) / len(noten)`, `sorted(noten)`.'
tests_sichtbar:
- input:
  - '2'
  - '1'
  - '3'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: [1, 2, 3]

    Beste: 1 Schlechteste: 3

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - '4'
  - '2'
  - '0'
  expected: '=== MEIN NOTENBUCH ===

    Fächer: Mathe, Deutsch, Musik

    Noten: [2, 4]

    Beste: 2 Schlechteste: 4

    Durchschnitt: 3.0

    Urteil: befriedigend

    Sterne: ****

    '
starter_code: "titel = \"Mein Notenbuch\"\nfaecher = \"Mathe, Deutsch, Musik\"\nprint(f\"=== {titel.upper()} ===\")\nprint(\"\
  Fächer:\", faecher)\nnoten = []\nwhile True:\n    note = int(input())\n    if note == 0:\n        break\n    noten = noten\
  \ + [note]\nsumme = 0\nfor note in noten:\n    summe += note\nschnitt = summe / len(noten)\nprint(\"Noten:\", noten)\nprint(\"\
  Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"Urteil:\
  \ gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\"\
  )\nelse:\n    print(\"Urteil: nicht bestanden\")\nprint(\"Sterne: \", end=\"\")\nfor i in range(7 - round(schnitt)):\n \
  \   print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 11.** Dein Code aus Stück 10 steht schon da. Benutze jetzt `append`, `sum`, `min`, `max` und `sorted`: die Noten erscheinen sortiert, darunter die beste und die schlechteste. Bei `2`, `1`, `3`, `0`:

```
=== MEIN NOTENBUCH ===
Fächer: Mathe, Deutsch, Musik
Noten: [1, 2, 3]
Beste: 1 Schlechteste: 3
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
