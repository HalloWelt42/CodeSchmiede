---
schema_version: 1
id: s078-dense-rank-jahr
revision: 1
titel: "Bücher: DENSE_RANK nach Jahr"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [window-function, dense-rank]
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
erwartete_spalten: ["titel", "jahr", "rang"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Stolz und Vorurteil", 1813, 1]
  - ["Emma", 1815, 2]
  - ["Buddenbrooks", 1901, 3]
  - ["Die Verwandlung", 1915, 4]
  - ["Siddhartha", 1922, 5]
  - ["Der Zauberberg", 1924, 6]
  - ["Der Process", 1925, 7]
  - ["Der Steppenwolf", 1927, 8]
  - ["Die Welt von Gestern", 1942, 9]
  - ["Schachnovelle", 1942, 9]
  - ["Farm der Tiere", 1945, 10]
  - ["Pippi Langstrumpf", 1945, 10]
  - ["1984", 1949, 11]
  - ["Karlsson vom Dach", 1955, 12]
  - ["Erdsee", 1968, 13]
  - ["Die linke Hand der Dunkelheit", 1969, 14]
  - ["Naokos Laecheln", 1987, 15]
  - ["Drachenreiter", 1997, 16]
  - ["Kafka am Strand", 2002, 17]
  - ["Tintenherz", 2003, 18]
hints:
  - kosten: 0
    text: |
      `DENSE_RANK()` -- gleiche Werte teilen sich den Rang, ohne Lücken im nächsten.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# DENSE_RANK nach Jahr

Buchtitel + Jahr + DENSE_RANK nach Erscheinungsjahr (früh = 1).
