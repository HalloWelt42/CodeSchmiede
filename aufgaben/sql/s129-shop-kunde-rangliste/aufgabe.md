---
schema_version: 1
id: s129-shop-kunde-rangliste
revision: 1
titel: "Shop: Kunden-Rangliste nach Umsatz"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 12
tags: [cte, window-function, rank]
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
erwartete_spalten: ["name", "gesamt", "rang"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Elena Vogel", 17.63, 1]
  - ["Alex Becker", 15.84, 2]
  - ["Beate Frank", 13.65, 3]
  - ["Gisela Hahn", 12.66, 4]
  - ["Karin Berger", 12.47, 5]
  - ["Carla Diaz", 10.17, 6]
  - ["Iris Schaefer", 9.47, 7]
  - ["Frank Berger", 7.88, 8]
  - ["Daniel Engel", 6.94, 9]
  - ["Hugo Meier", 6.56, 10]
  - ["Jan Petersen", 3.69, 11]
  - ["Leon Wolf", 3.28, 12]
hints:
  - kosten: 0
    text: |
      CTE mit Pro-Kunde-Umsatz, dann RANK in der aeusseren Query.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kunden-Rangliste

Name + Umsatz + Rang, hoechster Umsatz = Rang 1.
