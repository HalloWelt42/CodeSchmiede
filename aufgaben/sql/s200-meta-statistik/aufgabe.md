---
schema_version: 1
id: s200-meta-statistik
revision: 1
titel: "Meta: Anzahl pro Tabelle"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [union-all, count]
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
erwartete_spalten: ["tabelle", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["autoren", 10]
  - ["buecher", 20]
  - ["leser", 15]
  - ["ausleihen", 27]
hints:
  - kosten: 0
    text: |
      UNION ALL kombiniert mehrere SELECTs, Reihenfolge bleibt erhalten.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Tabellen-Zaehler

Für jede Tabelle: Name + Zeilenzahl, in dieser Reihenfolge: autoren, buecher, leser, ausleihen.
