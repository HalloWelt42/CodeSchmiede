---
schema_version: 1
id: s184-buecher-pro-leser-schnitt
revision: 1
titel: "Durchschnittliche Bücher pro Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [cte, avg]
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
erwartete_spalten: ["schnitt"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1.8]
hints:
  - kosten: 0
    text: |
      CTE mit COUNT pro Leser, AVG außen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Durchschnittliche Bücher pro Leser

Eine Zahl: AVG der Pro-Leser-Anzahl Ausleihen.
