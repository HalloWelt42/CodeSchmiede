---
schema_version: 1
id: j194-viele-objekte
revision: 1
titel: Eine ganze Kolonie
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
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
  text: '`kolonie.push(new Pinguin(name, Number(alter)));`'
- kosten: 2
  text: Bei Gleichstand bleibt der erste der Älteste.
tests_sichtbar:
- input:
  - Pit 4
  - Pia 7
  - Paul 2
  expected: 'Pinguin? Pinguin? Pinguin? Pinguin? Pit (4)

    Pia (7)

    Paul (2)

    Ältester: Pia

    '
tests_versteckt:
- input: []
  expected: "Pinguin? \n"
- input:
  - A 1
  - B 1
  expected: 'Pinguin? Pinguin? Pinguin? A (1)

    B (1)

    Ältester: A

    '
starter_code: "class Pinguin {\n  constructor(name, alter) {\n    this.name = name;\n    this.alter = alter;\n  }\n  vorstellen()\
  \ {\n    return `${this.name} (${this.alter})`;\n  }\n}\n"
---

Lies Pinguine wie `Pit 4`, bis eine leere Antwort oder keine mehr kommt, bau aus jedem ein Objekt der Klasse `Pinguin` und sammle sie in einem Array. Gib dann jeden mit `vorstellen()` aus und den ältesten. Bei den Eingaben `Pit 4`, `Pia 7` und `Paul 2`:

```
Pinguin? Pinguin? Pinguin? Pinguin? Pit (4)
Pia (7)
Paul (2)
Ältester: Pia
```
