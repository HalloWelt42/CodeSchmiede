---
schema_version: 1
id: s181-buecher-mit-letztes-ausleihe
revision: 1
titel: "Buecher: letztes Ausleihdatum"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, max, group-by]
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
erwartete_spalten: ["titel", "letztes"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Emma", "2025-04-15"]
  - ["Drachenreiter", "2025-04-12"]
  - ["Pippi Langstrumpf", "2025-04-12"]
  - ["Farm der Tiere", "2025-04-05"]
  - ["Der Process", "2025-04-01"]
  - ["Tintenherz", "2025-04-01"]
  - ["Siddhartha", "2025-03-22"]
  - ["Die Verwandlung", "2025-03-20"]
  - ["Karlsson vom Dach", "2025-03-15"]
  - ["Kafka am Strand", "2025-03-12"]
  - ["Stolz und Vorurteil", "2025-03-10"]
  - ["Der Zauberberg", "2025-03-01"]
  - ["Die linke Hand der Dunkelheit", "2025-03-01"]
  - ["1984", "2025-02-12"]
  - ["Der Steppenwolf", "2025-02-01"]
  - ["Erdsee", "2025-01-30"]
  - ["Naokos Laecheln", "2025-01-18"]
  - ["Die Welt von Gestern", "2025-01-15"]
  - ["Buddenbrooks", "2025-01-10"]
  - ["Schachnovelle", "2024-12-10"]
hints:
  - kosten: 0
    text: |
      MAX(Datum) pro Buch.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Letztes Ausleihdatum pro Buch

Titel + jüngstes Ausleihdatum, neuestes zuerst.
