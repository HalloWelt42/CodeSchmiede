---
schema_version: 1
id: s125-kategorien-mit-langem-buch
revision: 1
titel: "Kategorien mit mind. einem Buch ueber 500 Seiten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, having, max]
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
erwartete_spalten: ["kategorie", "max_seiten"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 992]
  - ["Kinderbuch", 576]
  - ["Biographie", 528]
hints:
  - kosten: 0
    text: |
      GROUP BY + HAVING MAX(seiten) > 500.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kategorien mit dickem Buch

Kategorie + maximaler Seitenzahl fuer Kategorien, in denen mindestens ein Buch > 500 Seiten hat.
