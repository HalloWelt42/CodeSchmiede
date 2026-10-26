---
schema_version: 1
id: j043-wie-lang
revision: 1
titel: Wie lang ist der Name?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- text
- laenge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`wagen.length` zählt, auch die Leerzeichen.'
- kosten: 2
  text: In die Vorlage darf `${wagen.length}`.
tests_sichtbar:
- input: []
  expected: 'Zum frostigen Hering hat 20 Zeichen

    '
starter_code: 'const wagen = "Zum frostigen Hering";

  '
---

Pit will den Namen seines Wagens auf ein Schild malen und muss wissen, wie viele Zeichen das sind. Gib es mit einer Vorlage aus:

```
Zum frostigen Hering hat 20 Zeichen
```
