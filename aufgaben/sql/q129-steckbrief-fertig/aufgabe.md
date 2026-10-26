---
schema_version: 1
id: q129-steckbrief-fertig
revision: 1
titel: 'Steckbrief: fertig für die Tafel'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- projekt
- case
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
- name
- kuerzel
- kolonie
- lage
- lieblingsfisch
- jahre
- mahlzeiten
- stufe
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - Pau
  - Nord
  - Packeis
  - Hering
  - 9
  - 2
  - erwachsen
- - Pit
  - Pit
  - Nord
  - Packeis
  - Hering
  - 7
  - 3
  - erwachsen
- - Polly
  - Pol
  - Nord
  - Packeis
  - Lachs
  - 7
  - 1
  - erwachsen
- - Pablo
  - Pab
  - Ost
  - Sandstrand
  - Hering
  - 5
  - 1
  - erwachsen
- - Pina
  - Pin
  - Nord
  - Packeis
  - unbekannt
  - 4
  - 1
  - Jungtier
- - Pünktchen
  - Pün
  - Ost
  - Sandstrand
  - unbekannt
  - 3
  - 1
  - Jungtier
hints:
- kosten: 0
  text: Der Name jahre gilt im SELECT selbst noch nicht; rechne das Alter im CASE noch einmal aus.
- kosten: 2
  text: '`CASE WHEN 2026 - p.geburtsjahr <= 4 THEN ''Jungtier'' ELSE ''erwachsen'' END AS stufe`'
starter_code: "SELECT p.name, SUBSTR(p.name, 1, 3) AS kuerzel, p.kolonie, k.lage, COALESCE(p.lieblingsfisch, 'unbekannt')\
  \ AS lieblingsfisch,\n       2026 - p.geburtsjahr AS jahre,\n       (SELECT COUNT(*) FROM fuetterungen f WHERE f.pinguin_id\
  \ = p.id) AS mahlzeiten\nFROM pinguine p\nJOIN kolonien k ON k.name = p.kolonie\nWHERE p.kolonie IN ('Nord', 'Ost')\nORDER\
  \ BY jahre DESC, p.name;"
---

**Kapitelprojekt Pinguinsteckbrief, letztes Stück.** Deine Abfrage aus Stück 11 steht schon da. Zum Schluss bekommt jeder Pinguin hinter `mahlzeiten` eine Spalte `stufe`: bis einschließlich vier Jahre `'Jungtier'`, sonst `'erwachsen'`. Dann hängt die Tafel.
