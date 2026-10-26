---
schema_version: 1
id: j048-namensschild
revision: 1
titel: Das Namensschild
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- text
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`vorname[0].toUpperCase() + vorname.slice(1)` macht aus pia Pia.'
- kosten: 2
  text: Leg den ganzen Namen in eine Konstante, dann helfen `name.length` und `"=".repeat(name.length)`.
tests_sichtbar:
- input: []
  expected: 'Name: Pia Pinguin

    Kürzel: PP

    Zeichen: 11

    ===========

    '
starter_code: 'const vorname = "pia";

  const nachname = "Pinguin";

  '
---

Pia hat ihren Vornamen klein geschrieben. Bau daraus das Namensschild: den Vornamen mit großem Anfangsbuchstaben (erstes Zeichen groß, Rest mit `slice`), das Kürzel aus den beiden Anfangsbuchstaben, die Zahl der Zeichen im ganzen Namen samt Leerzeichen und darunter einen Strich aus `=`, genau so lang wie der Name:

```
Name: Pia Pinguin
Kürzel: PP
Zeichen: 11
===========
```
