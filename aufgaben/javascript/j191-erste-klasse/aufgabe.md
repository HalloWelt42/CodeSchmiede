---
schema_version: 1
id: j191-erste-klasse
revision: 1
titel: Die erste Klasse
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Im constructor `this.name = name;`, in der Methode `this.name`.
tests_sichtbar:
- input: []
  expected: 'Ich bin Pit und 4 Jahre alt.

    Ich bin Pia und 5 Jahre alt.

    '
starter_code: ''
---

Schreib eine Klasse `Pinguin` mit `name` und `alter` im constructor und einer Methode `vorstellen()`, die einen Satz liefert. Bau zwei Pinguine:

```
Ich bin Pit und 4 Jahre alt.
Ich bin Pia und 5 Jahre alt.
```
