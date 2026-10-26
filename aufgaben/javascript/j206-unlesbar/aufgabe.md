---
schema_version: 1
id: j206-unlesbar
revision: 1
titel: Unlesbare Zettel
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- json
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: parse ins try; geht es gut, zählen und ausgeben.
- kosten: 2
  text: '`daten?.name ?? "ohne Namen"` hilft auch, wenn der Zettel nur null enthält.'
tests_sichtbar:
- input:
  - '{"name":"Pia"}'
  - '{name:Ole}'
  - '[1,2]'
  expected: 'Zettel? Pia

    Zettel? unlesbar

    Zettel? ohne Namen

    Zettel? Gelesen: 2

    '
tests_versteckt:
- input:
  - 'null'
  - '''x'''
  - ''
  expected: 'Zettel? ohne Namen

    Zettel? unlesbar

    Zettel? Gelesen: 1

    '
starter_code: ''
---

Lies JSON-Zettel, bis eine leere Antwort oder keine mehr kommt. Für lesbare Zettel mit Eigenschaft `name` gib den Namen aus, für unlesbare `unlesbar` und für lesbare ohne Namen `ohne Namen`. Am Ende, wie viele gelesen wurden. Bei den Eingaben `{"name":"Pia"}`, `{name:Ole}` und `[1,2]`:

```
Zettel? Pia
Zettel? unlesbar
Zettel? ohne Namen
Zettel? Gelesen: 2
```
