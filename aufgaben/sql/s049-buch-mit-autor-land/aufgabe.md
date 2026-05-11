---
schema_version: 1
id: s049-buch-mit-autor-land
revision: 1
titel: "Buch + Autor + Land"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, order-multi]
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
erwartete_spalten: ["titel", "name", "land"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Drachenreiter", "Cornelia Funke", "Deutschland"]
  - ["Tintenherz", "Cornelia Funke", "Deutschland"]
  - ["Der Steppenwolf", "Hermann Hesse", "Deutschland"]
  - ["Siddhartha", "Hermann Hesse", "Deutschland"]
  - ["Buddenbrooks", "Thomas Mann", "Deutschland"]
  - ["Der Zauberberg", "Thomas Mann", "Deutschland"]
  - ["1984", "George Orwell", "Grossbritannien"]
  - ["Farm der Tiere", "George Orwell", "Grossbritannien"]
  - ["Emma", "Jane Austen", "Grossbritannien"]
  - ["Stolz und Vorurteil", "Jane Austen", "Grossbritannien"]
  - ["Kafka am Strand", "Haruki Murakami", "Japan"]
  - ["Naokos Laecheln", "Haruki Murakami", "Japan"]
  - ["Die Welt von Gestern", "Stefan Zweig", "Oesterreich"]
  - ["Schachnovelle", "Stefan Zweig", "Oesterreich"]
  - ["Karlsson vom Dach", "Astrid Lindgren", "Schweden"]
  - ["Pippi Langstrumpf", "Astrid Lindgren", "Schweden"]
  - ["Der Process", "Franz Kafka", "Tschechien"]
  - ["Die Verwandlung", "Franz Kafka", "Tschechien"]
  - ["Die linke Hand der Dunkelheit", "Ursula K. Le Guin", "USA"]
  - ["Erdsee", "Ursula K. Le Guin", "USA"]
hints:
  - kosten: 0
    text: |
      JOIN + Sortierung nach mehreren Spalten.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buch + Autor + Land

Titel, Autor-Name und Autor-Land. Sortiert nach Land, Autor, Titel.
