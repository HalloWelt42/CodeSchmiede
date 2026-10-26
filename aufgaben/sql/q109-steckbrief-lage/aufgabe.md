---
schema_version: 1
id: q109-steckbrief-lage
revision: 1
titel: 'Steckbrief: die Lage'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- projekt
- join
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 10
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
- name
- kuerzel
- kolonie
- lage
- lieblingsfisch
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - Pau
  - Nord
  - Packeis
  - Hering
  - 9
- - Pit
  - Pit
  - Nord
  - Packeis
  - Hering
  - 7
- - Polly
  - Pol
  - Nord
  - Packeis
  - Lachs
  - 7
- - Pablo
  - Pab
  - Ost
  - Sandstrand
  - Hering
  - 5
- - Pina
  - Pin
  - Nord
  - Packeis
  - unbekannt
  - 4
- - Pünktchen
  - Pün
  - Ost
  - Sandstrand
  - unbekannt
  - 3
hints:
- kosten: 0
  text: '`JOIN kolonien k ON k.name = p.kolonie`'
- kosten: 1
  text: name gibt es in beiden Tabellen, also `p.name`.
starter_code: 'SELECT name, SUBSTR(name, 1, 3) AS kuerzel, kolonie, COALESCE(lieblingsfisch, ''unbekannt'') AS lieblingsfisch,
  2026 - geburtsjahr AS jahre

  FROM pinguine

  WHERE kolonie IN (''Nord'', ''Ost'')

  ORDER BY jahre DESC, name;'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 10.** Deine Tafel-Abfrage aus Stück 7 steht schon da. Neben der Kolonie soll jetzt auch ihre Lage stehen (Spalte `lage`, direkt hinter `kolonie`). Gib den Tabellen die Kürzel `p` und `k` und setze sie überall davor, wo es nötig ist.
