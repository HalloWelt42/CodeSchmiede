---
schema_version: 1
id: s138-buecher-multi-autor-pro-kategorie
revision: 1
titel: "Anzahl distinkter Autoren pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, count-distinct]
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
erwartete_spalten: ["kategorie", "autoren"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 6]
  - ["Erzaehlung", 2]
  - ["Kinderbuch", 2]
  - ["Biographie", 1]
  - ["Fantasy", 1]
  - ["Sci-Fi", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY kategorie + COUNT(DISTINCT autor_id).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren pro Kategorie

Kategorie + Anzahl unterschiedlicher Autoren, häufigste zuerst.
