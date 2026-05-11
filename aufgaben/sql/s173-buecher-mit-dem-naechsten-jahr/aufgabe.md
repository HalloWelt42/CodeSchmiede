---
schema_version: 1
id: s173-buecher-mit-dem-naechsten-jahr
revision: 1
titel: "Buecher mit Jahr des nächsten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [window-function, lead]
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
erwartete_spalten: ["titel", "jahr", "naechstes"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Stolz und Vorurteil", 1813, 1815]
  - ["Emma", 1815, 1901]
  - ["Buddenbrooks", 1901, 1915]
  - ["Die Verwandlung", 1915, 1922]
  - ["Siddhartha", 1922, 1924]
  - ["Der Zauberberg", 1924, 1925]
  - ["Der Process", 1925, 1927]
  - ["Der Steppenwolf", 1927, 1942]
  - ["Die Welt von Gestern", 1942, 1942]
  - ["Schachnovelle", 1942, 1945]
  - ["Farm der Tiere", 1945, 1945]
  - ["Pippi Langstrumpf", 1945, 1949]
  - ["1984", 1949, 1955]
  - ["Karlsson vom Dach", 1955, 1968]
  - ["Erdsee", 1968, 1969]
  - ["Die linke Hand der Dunkelheit", 1969, 1987]
  - ["Naokos Laecheln", 1987, 1997]
  - ["Drachenreiter", 1997, 2002]
  - ["Kafka am Strand", 2002, 2003]
  - ["Tintenherz", 2003, null]
hints:
  - kosten: 0
    text: |
      LEAD spiegelt LAG, schaut nach vorne.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Lead: Jahr des nächsten Buchs

Titel + Jahr + Jahr des nächsten Buchs in Reihenfolge.
