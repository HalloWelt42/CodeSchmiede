---
schema_version: 1
id: s137-buecher-pro-kategorie-prozent
revision: 1
titel: "Bücher: Verteilung pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [group-by, subquery, prozent]
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
erwartete_spalten: ["kategorie", "anzahl", "prozent"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 11, 55.0]
  - ["Kinderbuch", 4, 20.0]
  - ["Erzählung", 2, 10.0]
  - ["Biographie", 1, 5.0]
  - ["Fantasy", 1, 5.0]
  - ["Sci-Fi", 1, 5.0]
hints:
  - kosten: 0
    text: |
      100.0 * COUNT(*) / Gesamtzahl (per Subquery).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Verteilung pro Kategorie

Kategorie + Anzahl + Anteil in Prozent (1 Nachkommastelle), häufigste zuerst.
