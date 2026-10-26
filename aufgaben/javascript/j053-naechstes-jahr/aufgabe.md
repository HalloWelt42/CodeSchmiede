---
schema_version: 1
id: j053-naechstes-jahr
revision: 1
titel: Nächstes Jahr
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
  text: Ohne Umwandeln kleben `"4" + 1` zu 41.
- kosten: 2
  text: '`Number(prompt(...))` und dann `${alter + 1}` in der Vorlage.'
tests_sichtbar:
- input:
  - '4'
  expected: 'Wie alt bist du? Nächstes Jahr bist du 5.

    '
tests_versteckt:
- input:
  - '11'
  expected: 'Wie alt bist du? Nächstes Jahr bist du 12.

    '
- input:
  - '0'
  expected: 'Wie alt bist du? Nächstes Jahr bist du 1.

    '
starter_code: ''
---

Frag nach dem Alter und sag, wie alt man nächstes Jahr ist. Bei der Eingabe `4`:

```
Wie alt bist du? Nächstes Jahr bist du 5.
```
