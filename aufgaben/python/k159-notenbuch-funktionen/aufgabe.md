---
schema_version: 1
id: k159-notenbuch-funktionen
revision: 1
titel: 'Notenbuch: eigene Funktionen'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- projekt
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Das if/elif des Urteils wandert in die Funktion, statt print steht dort `return "gut"` und so weiter.
- kosten: 2
  text: '`sterne(note)` kann `"*" * (7 - round(note))` zurückgeben.'
tests_sichtbar:
- input:
  - Mathe
  - '2'
  - Deutsch
  - '1'
  - Musik
  - '3'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Mathe: 2 (gut)

    Deutsch: 1 (sehr gut)

    Musik: 3 (befriedigend)

    Verschiedene Noten: [1, 2, 3]

    Durchschnitt: 2.0

    Urteil: gut

    Sterne: *****

    '
tests_versteckt:
- input:
  - Sport
  - '5'
  - Kunst
  - '4'
  - ende
  expected: '=== MEIN NOTENBUCH ===

    Sport: 5 (nicht bestanden)

    Kunst: 4 (ausreichend)

    Verschiedene Noten: [4, 5]

    Durchschnitt: 4.5

    Urteil: nicht bestanden

    Sterne: ***

    '
starter_code: "titel = \"Mein Notenbuch\"\nprint(f\"=== {titel.upper()} ===\")\nnoten = {}\nwhile True:\n    fach = input()\n\
  \    if fach == \"ende\":\n        break\n    noten[fach] = int(input())\nfor fach, note in noten.items():\n    print(f\"\
  {fach}: {note}\")\nprint(\"Verschiedene Noten:\", sorted(set(noten.values())))\nschnitt = sum(noten.values()) / len(noten)\n\
  print(\"Durchschnitt:\", schnitt)\nif schnitt <= 1.5:\n    print(\"Urteil: sehr gut\")\nelif schnitt <= 2.5:\n    print(\"\
  Urteil: gut\")\nelif schnitt <= 3.5:\n    print(\"Urteil: befriedigend\")\nelif schnitt <= 4:\n    print(\"Urteil: ausreichend\"\
  )\nelse:\n    print(\"Urteil: nicht bestanden\")\nprint(\"Sterne: \", end=\"\")\nfor i in range(7 - round(schnitt)):\n \
  \   print(\"*\", end=\"\")\nprint()\n"
---

**Kapitelprojekt Notenbuch, Stück 15.** Dein Code aus Stück 14 steht schon da. Baue zwei Funktionen: `urteil(note)` gibt das Urteil als Text zurück, `sterne(note)` die Sterne. Damit steht hinter jedem Fach sein Urteil in Klammern, und Urteil und Sterne unten kommen aus denselben Funktionen. Bei `Mathe`, `2`, `Deutsch`, `1`, `Musik`, `3`, `ende`:

```
=== MEIN NOTENBUCH ===
Mathe: 2 (gut)
Deutsch: 1 (sehr gut)
Musik: 3 (befriedigend)
Verschiedene Noten: [1, 2, 3]
Durchschnitt: 2.0
Urteil: gut
Sterne: *****
```
