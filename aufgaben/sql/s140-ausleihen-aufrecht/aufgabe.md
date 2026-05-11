---
schema_version: 1
id: s140-ausleihen-aufrecht
revision: 1
titel: "Aktuelle Ausleihen-Tabelle"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, is-null]
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
erwartete_spalten: ["leser", "buch", "ausgeliehen_am"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Olivia Krueger", "Der Zauberberg", "2025-02-25"]
  - ["Bernd Mueller", "Der Zauberberg", "2025-03-01"]
  - ["Clara Weber", "Tintenherz", "2025-04-01"]
  - ["Niklas Wolf", "Der Process", "2025-04-01"]
  - ["Lukas Richter", "Farm der Tiere", "2025-04-05"]
  - ["Greta Hoffmann", "Pippi Langstrumpf", "2025-04-12"]
  - ["Greta Hoffmann", "Drachenreiter", "2025-04-12"]
  - ["Ines Becker", "Emma", "2025-04-15"]
hints:
  - kosten: 0
    text: |
      JOIN aller drei Tabellen, WHERE IS NULL.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aktuelle Ausleihen

Leser, Buchtitel, Ausleihdatum aller offenen Ausleihen, chronologisch.
