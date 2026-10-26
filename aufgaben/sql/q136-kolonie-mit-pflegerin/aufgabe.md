---
schema_version: 1
id: q136-kolonie-mit-pflegerin
revision: 1
titel: Kolonie mit Pflegerin
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
kontrolle: 'SELECT pf.name, k.name AS kolonie, k.lage

  FROM pfleger pf JOIN kolonien k ON k.name = pf.kolonie

  ORDER BY pf.name'
erwartete_spalten:
- name
- kolonie
- lage
sortierung_egal: false
erwartetes_ergebnis:
- - Greta
  - Nord
  - Packeis
- - Hannes
  - Süd
  - Felsenküste
- - Ida
  - Ost
  - Sandstrand
- - Karla
  - Mitte
  - Lagune
hints:
- kosten: 0
  text: Erst die Kolonie, dann die Pflegerin.
- kosten: 2
  text: '`INSERT INTO pfleger (name, kolonie) VALUES (''Karla'', ''Mitte'');`'
starter_code: ''
---

Lege die Kolonie Mitte an (Lagune, 6,5 Grad) und trage Karla als Pflegerin für diese Kolonie ein. Zwei Anweisungen, jede mit Semikolon.
