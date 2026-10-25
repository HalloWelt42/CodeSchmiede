---
schema_version: 1
id: k149-notenbuch-verschiedene
revision: 1
titel: 'Notenbuch: verschiedene Noten'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- projekt
- menge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`set(noten.values())` sind die verschiedenen Noten, `sorted` macht eine sortierte Liste daraus.'
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - Musik
  - '2'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Mathe: 2

    Deutsch: 1

    Musik: 2

    Verschiedene Noten: [1, 2]

    Durchschnitt: 1.6666666666666667

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - Sport
  - '3'
  - Kunst
  - '3'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Sport: 3

    Kunst: 3

    Verschiedene Noten: [3]

    Durchschnitt: 3.0

    Urteil: befriedigend

    Sterne: ****

    '
starter_code: "titel = \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten = {}\nwhile True:\n    fach = input()\n\
  \    if fach == \"ende\":\n        break\n    noten[fach] = int(input())\nfor fach, note in noten.items():\n    print(f\"\
  {fach}: {note}\")\nschnitt = sum(noten.values()) / len(noten)\nprint(\"Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n \
  \   print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"Urteil: gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil:\
  \ befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\")\nelse:\n    print(\"Urteil: nicht bestanden\"\
  )\nprint(\"Sterne: \", end=\"\")\nfor i in range(7 - round(schnitt)):\n    print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 14.** Dein Code aus Stück 13 steht schon da. Nach den Fächern zeigt das Notenbuch jetzt, welche verschiedenen Noten vorkommen, sortiert als Liste. Bei `Mathe`, `2`, `Deutsch`, `1`, `Musik`, `2`, `ende`:

```
=== MEIN NOTENBUCH ===
Mathe: 2
Deutsch: 1
Musik: 2
Verschiedene Noten: [1, 2]
Durchschnitt: 1.6666666666666667
Urteil: gut
Sterne: *****
```
