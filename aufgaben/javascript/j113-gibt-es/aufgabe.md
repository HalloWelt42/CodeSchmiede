---
schema_version: 1
id: j113-gibt-es
revision: 1
titel: Gibt es das?
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
  text: includes für ja oder nein, indexOf für die Stelle.
tests_sichtbar:
- input:
  - Makrele
  expected: 'Fisch? Makrele gibt es, Nummer 3

    '
tests_versteckt:
- input:
  - Lachs
  expected: 'Fisch? Lachs gibt es nicht

    '
- input:
  - Hering
  expected: 'Fisch? Hering gibt es, Nummer 1

    '
- input:
  - dorsch
  expected: 'Fisch? dorsch gibt es nicht

    '
starter_code: 'const karte = ["Hering", "Aal", "Makrele", "Dorsch"];

  '
---

Lies einen Fisch ein und sag, ob er auf der Karte steht und an welcher Stelle (ab 1 gezählt). Bei der Eingabe `Makrele`:

```
Fisch? Makrele gibt es, Nummer 3
```

Sonst heißt es zum Beispiel `Lachs gibt es nicht`.
