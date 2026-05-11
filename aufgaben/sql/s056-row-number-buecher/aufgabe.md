---
schema_version: 1
id: s056-row-number-buecher
revision: 1
titel: "Buecher mit fortlaufender Nummer pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [window-function, row-number, partition-by]
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
erwartete_spalten: ["titel", "kategorie", "nummer"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die Welt von Gestern", "Biographie", 1]
  - ["Die Verwandlung", "Erzaehlung", 1]
  - ["Schachnovelle", "Erzaehlung", 2]
  - ["Erdsee", "Fantasy", 1]
  - ["Drachenreiter", "Kinderbuch", 1]
  - ["Karlsson vom Dach", "Kinderbuch", 2]
  - ["Pippi Langstrumpf", "Kinderbuch", 3]
  - ["Tintenherz", "Kinderbuch", 4]
  - ["1984", "Roman", 1]
  - ["Buddenbrooks", "Roman", 2]
  - ["Der Process", "Roman", 3]
  - ["Der Steppenwolf", "Roman", 4]
  - ["Der Zauberberg", "Roman", 5]
  - ["Emma", "Roman", 6]
  - ["Farm der Tiere", "Roman", 7]
  - ["Kafka am Strand", "Roman", 8]
  - ["Naokos Laecheln", "Roman", 9]
  - ["Siddhartha", "Roman", 10]
  - ["Stolz und Vorurteil", "Roman", 11]
  - ["Die linke Hand der Dunkelheit", "Sci-Fi", 1]
hints:
  - kosten: 0
    text: |
      `ROW_NUMBER() OVER (PARTITION BY x ORDER BY y)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Fortlaufende Nummer pro Kategorie

In jeder Kategorie nummerieren die Buecher alphabetisch ab 1.
