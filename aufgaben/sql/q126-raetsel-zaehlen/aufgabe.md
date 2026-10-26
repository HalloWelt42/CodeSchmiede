---
schema_version: 1
id: q126-raetsel-zaehlen
revision: 1
titel: Wie viele Rätsel?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- case
- aggregat
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 12
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
- raetsel
- alle
sortierung_egal: false
erwartetes_ergebnis:
- - 2
  - 8
hints:
- kosten: 0
  text: 'Wie bei den Schwergewichten: 1 für ein Rätsel, sonst 0.'
- kosten: 2
  text: '`SUM(CASE WHEN lieblingsfisch IS NULL THEN 1 ELSE 0 END)`'
starter_code: ''
---

Zähle in einer Zeile, bei wie vielen Pinguinen der Lieblingsfisch unbekannt ist (Spalte `raetsel`) und wie viele es insgesamt sind (Spalte `alle`). Benutze CASE für die Rätsel.
