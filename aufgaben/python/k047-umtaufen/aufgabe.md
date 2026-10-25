---
schema_version: 1
id: k047-umtaufen
revision: 1
titel: Umtaufen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- text
- methoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`replace` tauscht jedes Vorkommen aus und lässt satz selbst unverändert.'
tests_sichtbar:
- input: []
  expected: 'Der Eisbär sagt Hallo zum Eisbär.

    Der Pinguin sagt Hallo zum Pinguin.

    '
starter_code: 'satz = "Der Eisbär sagt Hallo zum Eisbär."

  '
---

Im Satz soll aus jedem `Eisbär` ein `Pinguin` werden, und der Satz kommt zweimal: erst das Original, dann die neue Fassung:

```
Der Eisbär sagt Hallo zum Eisbär.
Der Pinguin sagt Hallo zum Pinguin.
```
