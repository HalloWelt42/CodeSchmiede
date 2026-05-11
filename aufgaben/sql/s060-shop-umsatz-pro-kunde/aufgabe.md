---
schema_version: 1
id: s060-shop-umsatz-pro-kunde
revision: 1
titel: "Shop: Umsatz pro Kunde"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [join, group-by, sum, berechnung]
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
erwartete_spalten: ["name", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Elena Vogel", 17.63]
  - ["Alex Becker", 15.84]
  - ["Beate Frank", 13.65]
  - ["Gisela Hahn", 12.66]
  - ["Karin Berger", 12.47]
  - ["Carla Diaz", 10.17]
  - ["Iris Schaefer", 9.47]
  - ["Frank Berger", 7.88]
  - ["Daniel Engel", 6.94]
  - ["Hugo Meier", 6.56]
  - ["Jan Petersen", 3.69]
  - ["Leon Wolf", 3.28]
hints:
  - kosten: 0
    text: |
      Drei JOINs + SUM + GROUP BY auf Kunden.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Umsatz pro Kunde

Name + Gesamtumsatz aller Bestellungen, hoechster Umsatz zuerst.
