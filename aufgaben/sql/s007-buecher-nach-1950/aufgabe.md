---
schema_version: 1
id: s007-buecher-nach-1950
revision: 1
titel: "Bücher nach 1950"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, order-by]
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
erwartete_spalten: ["titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Karlsson vom Dach", 1955]
  - ["Erdsee", 1968]
  - ["Die linke Hand der Dunkelheit", 1969]
  - ["Naokos Laecheln", 1987]
  - ["Drachenreiter", 1997]
  - ["Kafka am Strand", 2002]
  - ["Tintenherz", 2003]
hints:
  - kosten: 0
    text: |
      `WHERE jahr > 1950` filtert. `ORDER BY jahr` sortiert nach Jahr.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher nach 1950

Titel und Jahr aller Bücher, die **nach 1950** erschienen sind, aufsteigend nach Jahr.
