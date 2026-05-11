---
schema_version: 1
id: s008-buecher-roman
revision: 1
titel: "Romane"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where, string-equal]
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
  - ["1984"]
  - ["Buddenbrooks"]
  - ["Der Process"]
  - ["Der Steppenwolf"]
  - ["Der Zauberberg"]
  - ["Emma"]
  - ["Farm der Tiere"]
  - ["Kafka am Strand"]
  - ["Naokos Laecheln"]
  - ["Siddhartha"]
  - ["Stolz und Vorurteil"]
hints:
  - kosten: 0
    text: |
      `WHERE kategorie = 'Roman'` -- String in einfachen Anführungszeichen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Romane

Alle Bücher der Kategorie `Roman`, alphabetisch nach Titel.
