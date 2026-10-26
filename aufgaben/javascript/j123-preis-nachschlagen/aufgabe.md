---
schema_version: 1
id: j123-preis-nachschlagen
revision: 1
titel: Preis nachschlagen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- objekt
- for_in
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Der Name steht in einer Variable, also eckige Klammern: `preise[fisch]`.'
- kosten: 2
  text: '`fisch in preise` fragt, ob es ihn gibt.'
tests_sichtbar:
- input:
  - Aal
  expected: 'Fisch? Aal kostet 5.00 Euro

    '
tests_versteckt:
- input:
  - Lachs
  expected: 'Fisch? Lachs haben wir nicht

    '
- input:
  - Makrele
  expected: 'Fisch? Makrele kostet 3.20 Euro

    '
starter_code: 'const preise = { Hering: 2.5, Aal: 5, Makrele: 3.2 };

  '
---

Lies einen Fisch ein und schlag seinen Preis im Objekt nach. Bei der Eingabe `Aal`:

```
Fisch? Aal kostet 5.00 Euro
```

Gibt es den Fisch nicht, heißt es zum Beispiel `Lachs haben wir nicht`.
