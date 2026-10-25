---
schema_version: 1
id: k045-ausschnitt
revision: 1
titel: Der Ausschnitt
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- text
- scheiben
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Zähle die Zeichen: Schnee hat 6, ball 4.'
- kosten: 2
  text: '`wort[:6]`, `wort[6:10]`, `wort[10:]`'
tests_sichtbar:
- input: []
  expected: 'Schnee

    ball

    schlacht

    '
starter_code: 'wort = "Schneeballschlacht"

  '
---

Aus `Schneeballschlacht` sollen die Teile `Schnee`, `ball` und `schlacht` werden, jeder in seiner Zeile.
