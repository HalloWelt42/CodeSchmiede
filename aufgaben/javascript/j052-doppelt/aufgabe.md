---
schema_version: 1
id: j052-doppelt
revision: 1
titel: Doppelt so viele
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- eingabe
- umwandeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: prompt liefert Text, und Text plus Text wird geklebt.
- kosten: 2
  text: '`Number(prompt("Fische? "))` macht aus der Antwort eine Zahl.'
tests_sichtbar:
- input:
  - '21'
  expected: 'Fische? Doppelt: 42

    '
tests_versteckt:
- input:
  - '7'
  expected: 'Fische? Doppelt: 14

    '
starter_code: 'const fische = prompt("Fische? ");

  console.log("Doppelt:", fische + fische);

  '
---

Das Programm soll die eingegebene Zahl Fische verdoppeln, gibt bei `21` aber `2121` aus. Probier es aus und repariere es mit `Number`, ohne die zweite Zeile zu ändern. Bei der Eingabe `21`:

```
Fische? Doppelt: 42
```
