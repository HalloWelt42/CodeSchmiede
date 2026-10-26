---
schema_version: 1
id: j115-alphabetisch
revision: 1
titel: Alphabetisch
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
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
  text: '`namen.slice().sort()` sortiert eine Kopie.'
- kosten: 2
  text: Auch fürs Umdrehen eine Kopie, sonst ist das Sortierte danach rückwärts.
tests_sichtbar:
- input:
  - Pia,Ole,Ida
  expected: 'Namen? Sortiert: Ida, Ole, Pia

    Rückwärts: Pia, Ole, Ida

    Original: Pia, Ole, Ida

    '
tests_versteckt:
- input:
  - Bo
  expected: 'Namen? Sortiert: Bo

    Rückwärts: Bo

    Original: Bo

    '
- input:
  - Zoe,Anna,Mia,Ben
  expected: 'Namen? Sortiert: Anna, Ben, Mia, Zoe

    Rückwärts: Zoe, Mia, Ben, Anna

    Original: Zoe, Anna, Mia, Ben

    '
starter_code: ''
---

Lies Namen mit Kommas getrennt ein. Gib sie sortiert aus, dann rückwärts sortiert und zuletzt in der ursprünglichen Reihenfolge, die also erhalten bleiben muss. Bei der Eingabe `Pia,Ole,Ida`:

```
Namen? Sortiert: Ida, Ole, Pia
Rückwärts: Pia, Ole, Ida
Original: Pia, Ole, Ida
```
