---
schema_version: 1
id: s190-buecher-mit-fiktivem-bestand
revision: 1
titel: "Buecher mit Verfügbarkeitsstatus"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [left-join, case, group-by]
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
erwartete_spalten: ["titel", "exemplare", "verfuegbar", "status"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Der Zauberberg", 1, -1, "verfuegbar"]
  - ["Emma", 1, 0, "ausgeliehen"]
  - ["Buddenbrooks", 1, 1, "verfuegbar"]
  - ["Der Process", 2, 1, "verfuegbar"]
  - ["Die Welt von Gestern", 1, 1, "verfuegbar"]
  - ["Der Steppenwolf", 2, 2, "verfuegbar"]
  - ["Die linke Hand der Dunkelheit", 2, 2, "verfuegbar"]
  - ["Erdsee", 2, 2, "verfuegbar"]
  - ["Naokos Laecheln", 2, 2, "verfuegbar"]
  - ["Stolz und Vorurteil", 2, 2, "verfuegbar"]
  - ["Drachenreiter", 4, 3, "verfuegbar"]
  - ["Farm der Tiere", 4, 3, "verfuegbar"]
  - ["Kafka am Strand", 3, 3, "verfuegbar"]
  - ["Siddhartha", 3, 3, "verfuegbar"]
  - ["Karlsson vom Dach", 4, 4, "verfuegbar"]
  - ["Schachnovelle", 4, 4, "verfuegbar"]
  - ["Tintenherz", 5, 4, "verfuegbar"]
  - ["1984", 5, 5, "verfuegbar"]
  - ["Die Verwandlung", 5, 5, "verfuegbar"]
  - ["Pippi Langstrumpf", 6, 5, "verfuegbar"]
hints:
  - kosten: 0
    text: |
      LEFT JOIN mit Filter, CASE auf berechnete Verfügbarkeit.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Verfügbarkeitsstatus

Titel + Exemplare + Verfügbar + Status-Label, wenig-verfügbare zuerst.
