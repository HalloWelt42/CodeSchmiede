---
schema_version: 1
id: j175-noten
revision: 1
titel: Die richtige Art Fehler
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- fehlerarten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`Number.isInteger(note)` prüft auf ganze Zahl.'
- kosten: 2
  text: '`fehler.name` ist der Text TypeError oder RangeError.'
tests_sichtbar:
- input:
  - '7'
  expected: 'Note? Außerhalb: 7 gibt es nicht

    '
tests_versteckt:
- input:
  - '2.5'
  expected: 'Note? Falsche Art: Nur ganze Noten

    '
- input:
  - '2'
  expected: 'Note? Note 2 eingetragen

    '
- input:
  - '0'
  expected: 'Note? Außerhalb: 0 gibt es nicht

    '
starter_code: ''
---

Lies eine Note ein. Ist sie keine ganze Zahl, wirf einen `TypeError` (`Nur ganze Noten`), liegt sie nicht zwischen 1 und 6, einen `RangeError` (`n gibt es nicht`). Im catch unterscheidest du über `fehler.name`. Bei der Eingabe `7`:

```
Note? Außerhalb: 7 gibt es nicht
```

Bei `2.5` heißt es `Falsche Art: Nur ganze Noten`, bei `2` `Note 2 eingetragen`.
