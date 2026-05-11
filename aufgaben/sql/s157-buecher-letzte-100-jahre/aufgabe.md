---
schema_version: 1
id: s157-buecher-letzte-100-jahre
revision: 1
titel: "Buecher der letzten 100 Jahre"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where]
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
  - ["Tintenherz", 2003]
  - ["Kafka am Strand", 2002]
  - ["Drachenreiter", 1997]
  - ["Naokos Laecheln", 1987]
  - ["Die linke Hand der Dunkelheit", 1969]
  - ["Erdsee", 1968]
  - ["Karlsson vom Dach", 1955]
  - ["1984", 1949]
  - ["Farm der Tiere", 1945]
  - ["Pippi Langstrumpf", 1945]
  - ["Die Welt von Gestern", 1942]
  - ["Schachnovelle", 1942]
  - ["Der Steppenwolf", 1927]
hints:
  - kosten: 0
    text: |
      WHERE jahr >= 1926 (Stand 2026).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher seit 1926

Bücher der letzten 100 Jahre (Stand 2026).
