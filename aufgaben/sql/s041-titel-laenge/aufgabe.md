---
schema_version: 1
id: s041-titel-laenge
revision: 1
titel: "Buchtitel mit Laenge"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [string, length]
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
erwartete_spalten: ["titel", "laenge"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die linke Hand der Dunkelheit", 29]
  - ["Die Welt von Gestern", 20]
  - ["Stolz und Vorurteil", 19]
  - ["Karlsson vom Dach", 17]
  - ["Pippi Langstrumpf", 17]
  - ["Der Steppenwolf", 15]
  - ["Die Verwandlung", 15]
  - ["Kafka am Strand", 15]
  - ["Naokos Laecheln", 15]
  - ["Der Zauberberg", 14]
  - ["Farm der Tiere", 14]
  - ["Drachenreiter", 13]
  - ["Schachnovelle", 13]
  - ["Buddenbrooks", 12]
  - ["Der Process", 11]
  - ["Siddhartha", 10]
  - ["Tintenherz", 10]
  - ["Erdsee", 6]
  - ["1984", 4]
  - ["Emma", 4]
hints:
  - kosten: 0
    text: |
      `LENGTH(titel)` liefert die Zeichenzahl.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buchtitel mit Laenge

Titel + Anzahl Zeichen, laengster zuerst.
