---
schema_version: 1
id: j036-tagesbilanz
revision: 1
titel: Die Tagesbilanz
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- rechnen
- kurzschreibweise
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Je Kunde zwei Zeilen: `kasse += ...;` und `kunden++;`.'
tests_sichtbar:
- input: []
  expected: '3 Kunden, Kasse: 14

    '
starter_code: 'let kasse = 0;

  let kunden = 0;

  // erster Kunde


  // zweiter Kunde


  // dritter Kunde


  console.log(kunden, "Kunden, Kasse:", kasse);

  '
---

Drei Kunden kaufen für `2.5`, `7.5` und `4`. Zähle mit `+=` in `kasse` mit und mit `++` in `kunden`, so dass am Ende herauskommt:

```
3 Kunden, Kasse: 14
```
