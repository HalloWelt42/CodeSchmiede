---
schema_version: 1
id: j035-eisscholle
revision: 1
titel: Die Eisscholle
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rechnen
- potenz
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`kante ** 2` ist kante mal kante.'
tests_sichtbar:
- input: []
  expected: 'Fläche: 49

    Würfel: 343

    '
starter_code: 'const kante = 7;

  '
---

Die quadratische Eisscholle ist 7 Meter lang. Ihre Fläche ist 7 hoch 2, ein Eiswürfel mit dieser Kante hätte 7 hoch 3 Kubikmeter. Rechne mit `**` und dem Namen `kante`:

```
Fläche: 49
Würfel: 343
```
