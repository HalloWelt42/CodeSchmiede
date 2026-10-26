---
schema_version: 1
id: j051-begruessung
revision: 1
titel: Wer bist du?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Frage mit Leerzeichen am Ende genau so in prompt schreiben.
- kosten: 2
  text: Die Antwort von prompt in einen Namen legen und in eine Vorlage einsetzen.
tests_sichtbar:
- input:
  - Pia
  expected: 'Wie heißt du? Moin, Pia!

    '
tests_versteckt:
- input:
  - Ole
  expected: 'Wie heißt du? Moin, Ole!

    '
starter_code: ''
---

Frag mit `prompt("Wie heißt du? ")` nach dem Namen und begrüße dann. Bei der Eingabe `Pia` sieht die Ausgabe so aus (die Antwort selbst erscheint nicht, die tippt man ja):

```
Wie heißt du? Moin, Pia!
```
