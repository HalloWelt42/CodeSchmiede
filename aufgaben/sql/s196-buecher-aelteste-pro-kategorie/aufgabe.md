---
schema_version: 1
id: s196-buecher-aelteste-pro-kategorie
revision: 1
titel: "Bücher: Älteste pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [cte, window-function, top-per-group]
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
erwartete_spalten: ["kategorie", "titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Biographie", "Die Welt von Gestern", 1942]
  - ["Erzählung", "Die Verwandlung", 1915]
  - ["Fantasy", "Erdsee", 1968]
  - ["Kinderbuch", "Pippi Langstrumpf", 1945]
  - ["Roman", "Stolz und Vorurteil", 1813]
  - ["Sci-Fi", "Die linke Hand der Dunkelheit", 1969]
hints:
  - kosten: 0
    text: |
      CTE mit ROW_NUMBER pro Kategorie nach Jahr.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Ältestes Buch pro Kategorie

Kategorie + Titel + Jahr des ältesten Buchs.
