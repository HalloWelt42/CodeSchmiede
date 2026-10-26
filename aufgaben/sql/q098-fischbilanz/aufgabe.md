---
schema_version: 1
id: q098-fischbilanz
revision: 1
titel: Die Fischbilanz
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- group_by
- having
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
dataset: pinguinzoo
schema_hinweis: 'kolonien(name, lage, wassertemperatur)

  pinguine(id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)

  pfleger(id, name, kolonie)

  fuetterungen(id, pinguin_id, tag, fisch, menge)

  '
erwartete_spalten:
- fisch
- mal
- fische
sortierung_egal: false
erwartetes_ergebnis:
- - Lachs
  - 2
  - 11
- - Hering
  - 2
  - 9
- - Sardine
  - 3
  - 8
hints:
- kosten: 0
  text: WHERE für die Tage, HAVING für die Sorten, ORDER BY zum Schluss.
- kosten: 2
  text: '`HAVING COUNT(*) >= 2 ORDER BY fische DESC`'
starter_code: ''
---

Hole für die Fütterungen ab dem 21. Oktober 2026 je Fischsorte die Zahl der Fütterungen (`mal`) und die Fische insgesamt (`fische`). Nur Sorten mit mindestens zwei Fütterungen sollen kommen, die mit den meisten Fischen zuerst.
