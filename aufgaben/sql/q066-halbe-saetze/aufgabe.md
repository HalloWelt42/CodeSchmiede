---
schema_version: 1
id: q066-halbe-saetze
revision: 1
titel: Halbe Sätze
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- null_werte
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
- satz
sortierung_egal: false
erwartetes_ergebnis:
- - Pit mag Hering
- - Pia mag Lachs
- - Paul mag Hering
- - Pina mag irgendeinen Fisch
- - Pepe mag Makrele
- - Polly mag Lachs
- - Pablo mag Hering
- - Pünktchen mag irgendeinen Fisch
hints:
- kosten: 0
  text: Text mit NULL verbunden ergibt NULL.
- kosten: 2
  text: '`COALESCE(lieblingsfisch, ''irgendeinen Fisch'')`'
starter_code: 'SELECT name || '' mag '' || lieblingsfisch AS satz

  FROM pinguine;'
---

Die Abfrage baut für die Tafel Sätze wie "Pit mag Hering". Bei zwei Pinguinen kommt aber nur NULL heraus. Repariere sie so, dass dort `mag irgendeinen Fisch` steht.
