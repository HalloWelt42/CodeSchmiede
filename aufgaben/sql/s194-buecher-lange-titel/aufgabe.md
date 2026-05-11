---
schema_version: 1
id: s194-buecher-lange-titel
revision: 1
titel: "Buecher mit langem Titel"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, length]
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
erwartete_spalten: ["titel"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die linke Hand der Dunkelheit"]
  - ["Die Welt von Gestern"]
  - ["Stolz und Vorurteil"]
  - ["Karlsson vom Dach"]
  - ["Pippi Langstrumpf"]
hints:
  - kosten: 0
    text: |
      WHERE LENGTH(titel) > 15.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher mit langem Titel

Titel mit mehr als 15 Zeichen, längste zuerst.
