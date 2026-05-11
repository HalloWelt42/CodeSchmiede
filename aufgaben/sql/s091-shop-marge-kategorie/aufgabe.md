---
schema_version: 1
id: s091-shop-marge-kategorie
revision: 1
titel: "Shop: Umsatzanteil je Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [join, sum, group-by]
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
erwartete_spalten: ["kategorie", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Milchprodukte", 27.57]
  - ["Getränke", 27.09]
  - ["Obst", 21.97]
  - ["Gemüse", 17.85]
  - ["Backwaren", 15.31]
  - ["Süßwaren", 10.45]
hints:
  - kosten: 0
    text: |
      3-fach-JOIN bestellpositionen -> produkte -> kategorien, SUM auf menge*einzelpreis.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Umsatz pro Kategorie

Kategorie + Gesamtumsatz, höchster zuerst.
