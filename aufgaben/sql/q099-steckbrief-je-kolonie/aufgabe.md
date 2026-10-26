---
schema_version: 1
id: q099-steckbrief-je-kolonie
revision: 1
titel: 'Steckbrief: Kopfzeile je Kolonie'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
- group_by
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
- kolonie
- pinguine
- durchschnittsalter
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - 4
  - 6.8
- - Ost
  - 2
  - 4.0
hints:
- kosten: 0
  text: '`GROUP BY kolonie` nach WHERE, dann `ORDER BY kolonie`.'
starter_code: 'SELECT COUNT(*) AS pinguine, ROUND(AVG(2026 - geburtsjahr), 1) AS durchschnittsalter

  FROM pinguine

  WHERE kolonie IN (''Nord'', ''Ost'');'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 9.** Deine Kopfzeile aus Stück 8 steht schon da. Jetzt bekommt jede Kolonie auf der Tafel ihre eigene Kopfzeile: setze die Spalte `kolonie` vorn dazu, bilde eine Zeile je Kolonie und sortiere nach der Kolonie.
