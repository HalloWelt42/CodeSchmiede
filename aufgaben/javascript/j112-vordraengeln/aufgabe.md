---
schema_version: 1
id: j112-vordraengeln
revision: 1
titel: Vordrängeln
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: unshift stellt vorne an, shift nimmt vorne weg.
tests_sichtbar:
- input: []
  expected: 'Bedient: Bo

    Wartet noch: Pia, Ole

    '
starter_code: 'const schlange = ["Pia", "Ole"];

  '
---

Bo drängelt sich vor, danach wird der Erste bedient. Nutze `unshift` und `shift`:

```
Bedient: Bo
Wartet noch: Pia, Ole
```
