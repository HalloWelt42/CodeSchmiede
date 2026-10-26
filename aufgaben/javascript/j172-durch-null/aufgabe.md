---
schema_version: 1
id: j172-durch-null
revision: 1
titel: Teilen durch niemanden
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
tags:
- kurs
- throw
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`throw new Error("Niemand da zum Teilen");` in der Funktion.'
- kosten: 2
  text: finally hinter catch läuft in beiden Fällen.
tests_sichtbar:
- input:
  - '12'
  - '0'
  expected: 'Fische? Pinguine? Fehler: Niemand da zum Teilen

    Fertig

    '
tests_versteckt:
- input:
  - '12'
  - '4'
  expected: 'Fische? Pinguine? Jeder bekommt 3

    Fertig

    '
- input:
  - '7'
  - '2'
  expected: 'Fische? Pinguine? Jeder bekommt 3.5

    Fertig

    '
starter_code: ''
---

Schreib `teilen(fische, pinguine)`, die bei 0 Pinguinen einen Fehler `Niemand da zum Teilen` wirft, statt Infinity zu liefern. Fang ihn beim Aufruf ab und gib `Fehler: ...` aus; `Fertig` kommt immer, mit finally. Bei den Eingaben `12` und `0`:

```
Fische? Pinguine? Fehler: Niemand da zum Teilen
Fertig
```
