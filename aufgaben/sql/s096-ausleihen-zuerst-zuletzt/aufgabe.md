---
schema_version: 1
id: s096-ausleihen-zuerst-zuletzt
revision: 1
titel: "Erste und letzte Ausleihe pro Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, min, max, group-by]
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
erwartete_spalten: ["name", "erste", "letzte"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", "2025-01-05", "2025-02-12"]
  - ["Bernd Mueller", "2025-01-10", "2025-03-01"]
  - ["Clara Weber", "2025-02-20", "2025-04-01"]
  - ["David Fischer", "2025-01-22", "2025-01-22"]
  - ["Eva Schulz", "2024-12-10", "2025-03-10"]
  - ["Felix Bauer", "2025-02-08", "2025-02-08"]
  - ["Greta Hoffmann", "2025-04-12", "2025-04-12"]
  - ["Hans Wagner", "2024-11-05", "2025-02-01"]
  - ["Ines Becker", "2025-03-22", "2025-04-15"]
  - ["Jonas Schaefer", "2025-01-30", "2025-03-01"]
  - ["Karin Koehler", "2025-02-10", "2025-02-10"]
  - ["Lukas Richter", "2025-03-20", "2025-04-05"]
  - ["Maria Klein", "2025-01-18", "2025-03-12"]
  - ["Niklas Wolf", "2025-04-01", "2025-04-01"]
  - ["Olivia Krueger", "2025-02-25", "2025-02-25"]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY + MIN/MAX.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Erste und letzte Ausleihe pro Leser

Name + Datum der ersten und letzten Ausleihe.
