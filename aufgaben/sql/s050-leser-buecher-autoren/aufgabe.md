---
schema_version: 1
id: s050-leser-buecher-autoren
revision: 1
titel: "Leser, Buch, Autor (3-fach JOIN)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [join, drei-fach, where]
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
erwartete_spalten: ["leser", "titel", "autor"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Bernd Mueller", "Der Zauberberg", "Thomas Mann"]
  - ["Clara Weber", "Tintenherz", "Cornelia Funke"]
  - ["Greta Hoffmann", "Drachenreiter", "Cornelia Funke"]
  - ["Greta Hoffmann", "Pippi Langstrumpf", "Astrid Lindgren"]
  - ["Ines Becker", "Emma", "Jane Austen"]
  - ["Lukas Richter", "Farm der Tiere", "George Orwell"]
  - ["Niklas Wolf", "Der Process", "Franz Kafka"]
  - ["Olivia Krueger", "Der Zauberberg", "Thomas Mann"]
hints:
  - kosten: 0
    text: |
      3 JOINs hintereinander: ausleihen->leser, ausleihen->bücher, bücher->autoren.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser, Buch, Autor (offene Ausleihen)

Für jede offene Ausleihe: Leser-Name, Buch-Titel, Autor-Name.
