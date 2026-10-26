---
schema_version: 1
id: j047-umtaufen
revision: 1
titel: Neuer Fisch
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- text
- textmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`trim()` entfernt die Leerzeichen außen.'
- kosten: 1
  text: '`replaceAll` tauscht alle Vorkommen. Achte auf Frischer und Frische: der erste Hering braucht auch ein anderes Wort
    davor.'
- kosten: 3
  text: 'Zwei Schritte: `.replaceAll("Frischer Hering", "Frische Makrele")`, dann `.replaceAll("Hering", "Makrele")`.'
tests_sichtbar:
- input: []
  expected: 'Frische Makrele, Makrele frisch!

    '
starter_code: 'const ruf = "   Frischer Hering, Hering frisch!  ";

  '
---

Der Ruf vom Band ist verrauscht: vorne und hinten Leerzeichen, und er nennt den Hering von gestern. Säubere ihn und tausche **jeden** Hering gegen Makrele:

```
Frische Makrele, Makrele frisch!
```
