---
schema_version: 1
id: s023-anzahl-pro-kategorie
revision: 1
titel: "Buecher pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [group-by, count, aggregat]
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
  - ["Erzaehlung", 2]
  - ["Biographie", 1]
  - ["Fantasy", 1]
  - ["Sci-Fi", 1]
hints:
  - kosten: 0
    text: |
      `GROUP BY kategorie` plus `COUNT(*)`. Sortiere absteigend nach Anzahl.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher pro Kategorie

Kategorie und Anzahl der Buecher, hauefigste zuerst.
