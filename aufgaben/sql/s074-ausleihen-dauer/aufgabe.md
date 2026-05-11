---
schema_version: 1
id: s074-ausleihen-dauer
revision: 1
titel: "Ausleih-Dauer in Tagen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [date, julianday, cast]
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
erwartete_spalten: ["id", "tage"]
sortierung_egal: false
erwartetes_ergebnis:
  - [10, 28]
  - [12, 28]
  - [16, 27]
  - [25, 27]
  - [11, 26]
  - [15, 26]
  - [3, 25]
  - [8, 24]
  - [20, 24]
  - [21, 23]
  - [24, 23]
  - [19, 21]
  - [17, 19]
  - [2, 18]
  - [1, 14]
  - [9, 14]
  - [5, 12]
  - [22, 12]
  - [6, 7]
hints:
  - kosten: 0
    text: |
      `julianday(d2) - julianday(d1)` ergibt die Differenz in Tagen (als Float).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Ausleih-Dauer in Tagen

Fuer alle zurueckgegebenen Ausleihen: ID + Anzahl Tage (Integer), laengste zuerst.
