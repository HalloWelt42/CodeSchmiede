---
schema_version: 1
id: s161-buecher-und-jahr-relativ
revision: 1
titel: "Buecher mit Jahrhundert-Label"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [case-when]
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
erwartete_spalten: ["titel", "jahr", "epoche"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Stolz und Vorurteil", 1813, "19. Jh"]
  - ["Emma", 1815, "19. Jh"]
  - ["Buddenbrooks", 1901, "20. Jh"]
  - ["Die Verwandlung", 1915, "20. Jh"]
  - ["Siddhartha", 1922, "20. Jh"]
  - ["Der Zauberberg", 1924, "20. Jh"]
  - ["Der Process", 1925, "20. Jh"]
  - ["Der Steppenwolf", 1927, "20. Jh"]
  - ["Die Welt von Gestern", 1942, "20. Jh"]
  - ["Schachnovelle", 1942, "20. Jh"]
  - ["Farm der Tiere", 1945, "20. Jh"]
  - ["Pippi Langstrumpf", 1945, "20. Jh"]
  - ["1984", 1949, "20. Jh"]
  - ["Karlsson vom Dach", 1955, "20. Jh"]
  - ["Erdsee", 1968, "20. Jh"]
  - ["Die linke Hand der Dunkelheit", 1969, "20. Jh"]
  - ["Naokos Laecheln", 1987, "20. Jh"]
  - ["Drachenreiter", 1997, "20. Jh"]
  - ["Kafka am Strand", 2002, "21. Jh"]
  - ["Tintenherz", 2003, "21. Jh"]
hints:
  - kosten: 0
    text: |
      CASE WHEN mit Jahr-Schwellen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher mit Epoche

Titel + Jahr + Epoche (19., 20., 21. Jh).
