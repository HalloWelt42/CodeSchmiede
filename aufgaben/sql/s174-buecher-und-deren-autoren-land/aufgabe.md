---
schema_version: 1
id: s174-buecher-und-deren-autoren-land
revision: 1
titel: "Buecher mit Land des Autors"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [join, where, not-equal]
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
erwartete_spalten: ["titel", "land"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["1984", "Grossbritannien"]
  - ["Emma", "Grossbritannien"]
  - ["Farm der Tiere", "Grossbritannien"]
  - ["Stolz und Vorurteil", "Grossbritannien"]
  - ["Kafka am Strand", "Japan"]
  - ["Naokos Laecheln", "Japan"]
  - ["Die Welt von Gestern", "Oesterreich"]
  - ["Schachnovelle", "Oesterreich"]
  - ["Karlsson vom Dach", "Schweden"]
  - ["Pippi Langstrumpf", "Schweden"]
  - ["Der Process", "Tschechien"]
  - ["Die Verwandlung", "Tschechien"]
  - ["Die linke Hand der Dunkelheit", "USA"]
  - ["Erdsee", "USA"]
hints:
  - kosten: 0
    text: |
      JOIN + WHERE != 'Deutschland'.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Nicht-deutsche Autoren

Titel + Land aller Bücher von Autoren außerhalb Deutschlands.
