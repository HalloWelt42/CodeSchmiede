---
schema_version: 1
id: s191-leser-mit-ausleihen-anzahl-rang
revision: 1
titel: "Leser-Aktivitäts-Ranking"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [left-join, window-function, rank, group-by]
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
erwartete_spalten: ["name", "anz", "rang"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Clara Weber", 3, 1]
  - ["Eva Schulz", 3, 1]
  - ["Anna Schmidt", 2, 3]
  - ["Bernd Mueller", 2, 3]
  - ["Greta Hoffmann", 2, 3]
  - ["Hans Wagner", 2, 3]
  - ["Ines Becker", 2, 3]
  - ["Jonas Schaefer", 2, 3]
  - ["Lukas Richter", 2, 3]
  - ["Maria Klein", 2, 3]
  - ["David Fischer", 1, 11]
  - ["Felix Bauer", 1, 11]
  - ["Karin Koehler", 1, 11]
  - ["Niklas Wolf", 1, 11]
  - ["Olivia Krueger", 1, 11]
hints:
  - kosten: 0
    text: |
      GROUP BY + RANK über COUNT-Aggregat.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser-Aktivitäts-Ranking

Name + Ausleih-Anzahl + Rang (häufigster = 1).
