---
schema_version: 1
id: s083-buecher-jahresalter
revision: 1
titel: "Alter der Buecher (in 2026)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [math, subtraction]
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
erwartete_spalten: ["titel", "alter_jahre"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Stolz und Vorurteil", 213]
  - ["Emma", 211]
  - ["Buddenbrooks", 125]
  - ["Die Verwandlung", 111]
  - ["Siddhartha", 104]
  - ["Der Zauberberg", 102]
  - ["Der Process", 101]
  - ["Der Steppenwolf", 99]
  - ["Die Welt von Gestern", 84]
  - ["Schachnovelle", 84]
  - ["Farm der Tiere", 81]
  - ["Pippi Langstrumpf", 81]
  - ["1984", 77]
  - ["Karlsson vom Dach", 71]
  - ["Erdsee", 58]
  - ["Die linke Hand der Dunkelheit", 57]
  - ["Naokos Laecheln", 39]
  - ["Drachenreiter", 29]
  - ["Kafka am Strand", 24]
  - ["Tintenherz", 23]
hints:
  - kosten: 0
    text: |
      Einfache Subtraktion `2026 - jahr`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Alter der Buecher

Titel + Alter in Jahren (Stand 2026), aelteste zuerst.
