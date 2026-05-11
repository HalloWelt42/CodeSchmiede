---
schema_version: 1
id: s186-buecher-kategorie-jahresspanne
revision: 1
titel: "Kategorien: Jahres-Spanne"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [group-by, min, max]
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
erwartete_spalten: ["kategorie", "frueh", "spaet", "spanne"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 1813, 2002, 189]
  - ["Kinderbuch", 1945, 2003, 58]
  - ["Erzaehlung", 1915, 1942, 27]
  - ["Biographie", 1942, 1942, 0]
  - ["Fantasy", 1968, 1968, 0]
  - ["Sci-Fi", 1969, 1969, 0]
hints:
  - kosten: 0
    text: |
      GROUP BY + MIN/MAX/Differenz.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Jahres-Spanne pro Kategorie

Kategorie + frühestes Jahr + spätestes Jahr + Differenz, größte Spanne zuerst.
