---
schema_version: 1
id: s122-buecher-anzahl-leser-kombiniert
revision: 1
titel: "Buecher mit aktueller Verfuegbarkeit"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [left-join, group-by, berechnung]
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
erwartete_spalten: ["titel", "verfuegbar"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Der Zauberberg", -1]
  - ["Emma", 0]
  - ["Buddenbrooks", 1]
  - ["Der Process", 1]
  - ["Die Welt von Gestern", 1]
  - ["Der Steppenwolf", 2]
  - ["Die linke Hand der Dunkelheit", 2]
  - ["Erdsee", 2]
  - ["Naokos Laecheln", 2]
  - ["Stolz und Vorurteil", 2]
  - ["Drachenreiter", 3]
  - ["Farm der Tiere", 3]
  - ["Kafka am Strand", 3]
  - ["Siddhartha", 3]
  - ["Karlsson vom Dach", 4]
  - ["Schachnovelle", 4]
  - ["Tintenherz", 4]
  - ["1984", 5]
  - ["Die Verwandlung", 5]
  - ["Pippi Langstrumpf", 5]
hints:
  - kosten: 0
    text: |
      LEFT JOIN mit Filter im ON-Clause, dann GROUP BY + Differenz.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aktuelle Verfuegbarkeit

Buch + Anzahl verfuegbare Exemplare (Exemplare minus offene Ausleihen), wenig verfuegbar zuerst.
