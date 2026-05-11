---
schema_version: 1
id: s103-buecher-pro-autor-konkat
revision: 1
titel: "Buchliste pro Autor (GROUP_CONCAT)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [group-concat, join, aggregat]
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
erwartete_spalten: ["name", "buecher"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Astrid Lindgren", "Pippi Langstrumpf, Karlsson vom Dach"]
  - ["Cornelia Funke", "Tintenherz, Drachenreiter"]
  - ["Franz Kafka", "Die Verwandlung, Der Process"]
  - ["George Orwell", "1984, Farm der Tiere"]
  - ["Haruki Murakami", "Naokos Laecheln, Kafka am Strand"]
  - ["Hermann Hesse", "Siddhartha, Der Steppenwolf"]
  - ["Jane Austen", "Stolz und Vorurteil, Emma"]
  - ["Stefan Zweig", "Schachnovelle, Die Welt von Gestern"]
  - ["Thomas Mann", "Buddenbrooks, Der Zauberberg"]
  - ["Ursula K. Le Guin", "Erdsee, Die linke Hand der Dunkelheit"]
hints:
  - kosten: 0
    text: |
      `GROUP_CONCAT(spalte, ', ')` fasst die Spalten-Werte einer Gruppe zu einem String zusammen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher pro Autor als String

Für jeden Autor: name + komma-separierte Liste aller Buchtitel.
