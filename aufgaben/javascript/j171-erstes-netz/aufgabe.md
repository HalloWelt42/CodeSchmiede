---
schema_version: 1
id: j171-erstes-netz
revision: 1
titel: Das erste Netz
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
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
  text: '`try { ... } catch (fehler) { ... }` um die Ausgabe herum.'
tests_sichtbar:
- input:
  - pia
  expected: 'Name? MOIN, PIA!

    '
tests_versteckt:
- input: []
  expected: 'Name? Kein Name, kein Gruß

    '
starter_code: 'const name = prompt("Name? ");

  console.log(`MOIN, ${name.toUpperCase()}!`);

  '
---

Kommt keine Eingabe, liefert prompt null, und das Programm bricht ab. Pack die gefährliche Zeile in ein `try` und gib im `catch` `Kein Name, kein Gruß` aus. Bei der Eingabe `pia`:

```
Name? MOIN, PIA!
```
