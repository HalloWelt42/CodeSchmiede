---
schema_version: 1
id: s025-leser-mit-buchnamen
revision: 1
titel: "Leser und ihre ausgeliehenen Bücher"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [join, where, is-null]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  autoren(id, name, geburtsjahr, land)
  buecher(id, titel, autor_id, jahr, seiten, kategorie, exemplare)
  leser(id, name, ort, alter_jahre, mitglied_seit)
  ausleihen(id, leser_id, buch_id, ausgeliehen_am, zurueck_am)
erwartete_spalten: ["name", "titel"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Bernd Mueller", "Der Zauberberg"]
  - ["Clara Weber", "Tintenherz"]
  - ["Greta Hoffmann", "Drachenreiter"]
  - ["Greta Hoffmann", "Pippi Langstrumpf"]
  - ["Ines Becker", "Emma"]
  - ["Lukas Richter", "Farm der Tiere"]
  - ["Niklas Wolf", "Der Process"]
  - ["Olivia Krueger", "Der Zauberberg"]
hints:
  - kosten: 0
    text: |
      Zwei JOINs verkettet: `ausleihen` -> `leser` und `ausleihen` -> .
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser und ihre offenen Ausleihen

Leser-Name + Buch-Titel aller noch nicht zurückgegebenen Ausleihen, sortiert nach Leser dann Titel.
