---
schema_version: 1
id: s026-buecher-mit-autoren
revision: 1
titel: "Buecher mit Autorenname"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [join, inner-join]
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
erwartete_spalten: ["titel", "name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Karlsson vom Dach", "Astrid Lindgren"]
  - ["Pippi Langstrumpf", "Astrid Lindgren"]
  - ["Drachenreiter", "Cornelia Funke"]
  - ["Tintenherz", "Cornelia Funke"]
  - ["Der Process", "Franz Kafka"]
  - ["Die Verwandlung", "Franz Kafka"]
  - ["1984", "George Orwell"]
  - ["Farm der Tiere", "George Orwell"]
  - ["Kafka am Strand", "Haruki Murakami"]
  - ["Naokos Laecheln", "Haruki Murakami"]
  - ["Der Steppenwolf", "Hermann Hesse"]
  - ["Siddhartha", "Hermann Hesse"]
  - ["Emma", "Jane Austen"]
  - ["Stolz und Vorurteil", "Jane Austen"]
  - ["Die Welt von Gestern", "Stefan Zweig"]
  - ["Schachnovelle", "Stefan Zweig"]
  - ["Buddenbrooks", "Thomas Mann"]
  - ["Der Zauberberg", "Thomas Mann"]
  - ["Die linke Hand der Dunkelheit", "Ursula K. Le Guin"]
  - ["Erdsee", "Ursula K. Le Guin"]
hints:
  - kosten: 0
    text: |
      INNER JOIN ueber `autor_id = id`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher mit Autorenname

Titel + Autorenname, sortiert nach Autor und dann Titel.
