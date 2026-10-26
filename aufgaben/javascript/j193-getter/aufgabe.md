---
schema_version: 1
id: j193-getter
revision: 1
titel: Die Scholle
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- klasse
- getter
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`get flaeche() { return ...; }` in der Klasse.'
tests_sichtbar:
- input: []
  expected: 'Fläche: 12

    Umfang: 14

    Fläche: 20

    '
starter_code: "class Scholle {\n  constructor(breite, laenge) {\n    this.breite = breite;\n    this.laenge = laenge;\n  }\n\
  }\nconst s = new Scholle(3, 4);\nconsole.log(\"Fläche:\", s.flaeche);\nconsole.log(\"Umfang:\", s.umfang);\ns.breite = 5;\n\
  console.log(\"Fläche:\", s.flaeche);\n"
---

Gib der Klasse `Scholle` die berechneten Eigenschaften `flaeche` und `umfang` mit `get`:

```
Fläche: 12
Umfang: 14
Fläche: 20
```
