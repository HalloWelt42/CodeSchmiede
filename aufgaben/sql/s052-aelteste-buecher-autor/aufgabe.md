---
schema_version: 1
id: s052-aelteste-buecher-autor
revision: 1
titel: "Aeltestes Buch jedes Autors"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [correlated-subquery]
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
erwartete_spalten: ["name", "titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Astrid Lindgren", "Pippi Langstrumpf", 1945]
  - ["Cornelia Funke", "Drachenreiter", 1997]
  - ["Franz Kafka", "Die Verwandlung", 1915]
  - ["George Orwell", "Farm der Tiere", 1945]
  - ["Haruki Murakami", "Naokos Laecheln", 1987]
  - ["Hermann Hesse", "Siddhartha", 1922]
  - ["Jane Austen", "Stolz und Vorurteil", 1813]
  - ["Stefan Zweig", "Schachnovelle", 1942]
  - ["Stefan Zweig", "Die Welt von Gestern", 1942]
  - ["Thomas Mann", "Buddenbrooks", 1901]
  - ["Ursula K. Le Guin", "Erdsee", 1968]
hints:
  - kosten: 0
    text: |
      Correlated Subquery: Subquery in WHERE referenziert die aeussere Tabelle.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aeltestes Buch jedes Autors

Fuer jeden Autor das frueh erschienene Buch.
