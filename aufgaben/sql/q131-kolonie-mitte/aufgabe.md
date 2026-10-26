---
schema_version: 1
id: q131-kolonie-mitte
revision: 1
titel: Die Kolonie Mitte
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- insert
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 13
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
kontrolle: SELECT * FROM kolonien ORDER BY name
erwartete_spalten:
- name
- lage
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Mitte
  - Lagune
  - 6.5
- - Nord
  - Packeis
  - -1.5
- - Ost
  - Sandstrand
  - 9.5
- - Süd
  - Felsenküste
  - 4.0
- - West
  - Eishöhle
  - -0.5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'INSERT INTO kolonien (name, lage, wassertemperatur)

  VALUES (''Mitte'', ''Lagune'', 6.5);'
---

Das Skript steht schon da: es legt die neue Kolonie Mitte an einer Lagune an. Prüfe es; rechts siehst du danach die Tabelle kolonien, wie die Kontrollabfrage sie liefert.
