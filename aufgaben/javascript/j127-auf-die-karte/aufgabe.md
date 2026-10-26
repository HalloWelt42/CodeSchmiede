---
schema_version: 1
id: j127-auf-die-karte
revision: 1
titel: Neu auf der Karte
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- objekt
- array
- delete
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`karte.push({ name: name, preis: preis })` hängt ein neues Objekt an.'
- kosten: 2
  text: '`delete karte[1].scharf;`'
tests_sichtbar:
- input:
  - Matjes
  - '3.8'
  expected: 'Gericht? Preis? Heringsbrötchen: 2.50

    Fischsuppe: 4.50

    Matjes: 3.80

    Scharf: false

    '
tests_versteckt:
- input:
  - Aal
  - '5'
  expected: 'Gericht? Preis? Heringsbrötchen: 2.50

    Fischsuppe: 4.50

    Aal: 5.00

    Scharf: false

    '
starter_code: "const karte = [\n  { name: \"Heringsbrötchen\", preis: 2.5 },\n  { name: \"Fischsuppe\", preis: 4.5, scharf:\
  \ true },\n];\n"
---

Lies ein neues Gericht und seinen Preis ein, hänge es als Objekt an die Karte und entferne bei der Fischsuppe die Eigenschaft `scharf`. Gib dann jedes Gericht als `Name: Preis` aus. Bei den Eingaben `Matjes` und `3.8`:

```
Gericht? Preis? Heringsbrötchen: 2.50
Fischsuppe: 4.50
Matjes: 3.80
```

Und zuletzt eine Zeile, ob die Suppe noch `scharf` hat: `Scharf: false`.
