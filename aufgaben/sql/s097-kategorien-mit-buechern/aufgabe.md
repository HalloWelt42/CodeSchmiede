---
schema_version: 1
id: s097-kategorien-mit-buechern
revision: 1
titel: "Kategorien mit mind. 3 Buechern"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, having]
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
erwartete_spalten: ["kategorie", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 11]
  - ["Kinderbuch", 4]
hints:
  - kosten: 0
    text: |
      GROUP BY + HAVING COUNT(*) >= 3.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kategorien mit min. 3 Buechern

Kategorie + Anzahl, hauefigste zuerst.
