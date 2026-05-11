---
schema_version: 1
id: s077-prozent-am-gesamt
revision: 1
titel: "Shop: Anteil jeder Bestellung am Gesamtumsatz"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 12
tags: [window-function, sum-over, prozent]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: shop
schema_hinweis: |
  kategorien(id, name)
  produkte(id, name, kategorie_id, preis, lager, marke)
  kunden(id, name, ort, plz, alter_jahre)
  bestellungen(id, kunde_id, bestellt_am, status)
  bestellpositionen(bestellung_id, produkt_id, menge, einzelpreis)
erwartete_spalten: ["bestellung_id", "umsatz", "prozent"]
sortierung_egal: false
erwartetes_ergebnis:
  - [8, 12.76, 10.61]
  - [11, 12.66, 10.53]
  - [15, 12.47, 10.37]
  - [3, 9.78, 8.13]
  - [13, 9.47, 7.88]
  - [1, 8.07, 6.71]
  - [5, 7.97, 6.63]
  - [10, 7.88, 6.55]
  - [2, 7.77, 6.46]
  - [7, 6.94, 5.77]
  - [12, 6.56, 5.46]
  - [9, 4.87, 4.05]
  - [4, 3.87, 3.22]
  - [14, 3.69, 3.07]
  - [16, 3.28, 2.73]
  - [6, 2.2, 1.83]
hints:
  - kosten: 0
    text: |
      `SUM(SUM(...)) OVER ()` -- aeussere SUM über alle gruppierten Zeilen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anteil am Gesamtumsatz

Pro Bestellung: Umsatz + prozentualer Anteil am Gesamtumsatz aller Bestellungen.
