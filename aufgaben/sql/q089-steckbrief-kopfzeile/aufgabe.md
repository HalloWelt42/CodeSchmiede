---
schema_version: 1
id: q089-steckbrief-kopfzeile
revision: 1
titel: 'Steckbrief: die Kopfzeile'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
- aggregat
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 8
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
- pinguine
- durchschnittsalter
sortierung_egal: false
erwartetes_ergebnis:
- - 6
  - 5.8
hints:
- kosten: 0
  text: Dieselbe WHERE-Bedingung wie die Tafel.
- kosten: 2
  text: '`ROUND(AVG(2026 - geburtsjahr), 1)`'
starter_code: ''
---

**Kapitelprojekt Pinguinsteckbrief, Stück 8.** Über die Tafel kommt eine Kopfzeile, eine eigene kleine Abfrage: wie viele Pinguine aus Nord und Ost stehen darauf (Spalte `pinguine`) und wie alt sind sie 2026 im Schnitt, auf eine Stelle gerundet (Spalte `durchschnittsalter`)?
