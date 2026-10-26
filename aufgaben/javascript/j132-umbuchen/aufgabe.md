---
schema_version: 1
id: j132-umbuchen
revision: 1
titel: Umbuchen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Den neuen Wert aus dem alten rechnen: `lager.get("Hering") - 3`.'
tests_sichtbar:
- input: []
  expected: 'Map(1) { ''Hering'' => 9 }

    '
starter_code: 'const lager = new Map();

  lager.set("Hering", 12);

  lager.set("Aal", 3);

  '
---

Drei Heringe werden verkauft, der Aal ist alle. Zieh beim Hering 3 ab (mit get und set), entferne den Aal und gib die Map aus:

```
Map(1) { 'Hering' => 9 }
```
