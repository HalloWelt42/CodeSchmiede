---
schema_version: 1
id: s112-buecher-mit-stufen
revision: 1
titel: "Bücher mit Dichte-Stufen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [case-when, klassifizierung]
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
erwartete_spalten: ["titel", "seiten", "dicke"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die Verwandlung", 74, "duenn"]
  - ["Schachnovelle", 96, "duenn"]
  - ["Farm der Tiere", 112, "duenn"]
  - ["Karlsson vom Dach", 124, "duenn"]
  - ["Siddhartha", 153, "duenn"]
  - ["Pippi Langstrumpf", 168, "duenn"]
  - ["Erdsee", 224, "mittel"]
  - ["Der Steppenwolf", 288, "mittel"]
  - ["Naokos Laecheln", 296, "mittel"]
  - ["Die linke Hand der Dunkelheit", 304, "mittel"]
  - ["Der Process", 312, "mittel"]
  - ["1984", 326, "mittel"]
  - ["Drachenreiter", 432, "mittel"]
  - ["Stolz und Vorurteil", 432, "mittel"]
  - ["Emma", 474, "mittel"]
  - ["Die Welt von Gestern", 528, "dick"]
  - ["Tintenherz", 576, "dick"]
  - ["Kafka am Strand", 624, "dick"]
  - ["Buddenbrooks", 759, "dick"]
  - ["Der Zauberberg", 992, "dick"]
hints:
  - kosten: 0
    text: |
      CASE mit drei Zweigen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher mit Dicke-Klassifizierung

Titel + Seitenzahl + Klassifizierung: <200=duenn, <500=mittel, sonst dick.
