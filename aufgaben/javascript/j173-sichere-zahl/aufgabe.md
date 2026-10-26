---
schema_version: 1
id: j173-sichere-zahl
revision: 1
titel: Bis es passt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 5
tags:
- kurs
- throw
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im try lesen und mit break raus, im catch melden; die Schleife fragt dann von vorn.
tests_sichtbar:
- input:
  - zwei
  - ''
  - '2'
  expected: 'Anzahl? "zwei" ist keine Zahl

    Anzahl? "" ist keine Zahl

    Anzahl? Doppelt: 4

    '
tests_versteckt:
- input:
  - '7'
  expected: 'Anzahl? Doppelt: 14

    '
- input:
  - x
  - y
  - '1.5'
  expected: 'Anzahl? "x" ist keine Zahl

    Anzahl? "y" ist keine Zahl

    Anzahl? Doppelt: 3

    '
starter_code: ''
---

Schreib `liesZahl(text)`, die eine Zahl liefert oder einen Fehler `"text" ist keine Zahl` wirft (auch beim leeren Text). Frag so lange, bis eine Zahl kommt, und melde jeden Fehlversuch. Bei den Eingaben `zwei`, leer und `2`:

```
Anzahl? "zwei" ist keine Zahl
Anzahl? "" ist keine Zahl
Anzahl? Doppelt: 4
```
