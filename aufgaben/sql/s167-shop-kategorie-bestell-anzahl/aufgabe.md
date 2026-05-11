---
schema_version: 1
id: s167-shop-kategorie-bestell-anzahl
revision: 1
titel: "Shop: Wieviele Bestellungen enthalten Kategorie X"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, count-distinct, group-by]
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
erwartete_spalten: ["kategorie", "bestellungen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Milchprodukte", 7]
  - ["Obst", 7]
  - ["Getraenke", 6]
  - ["Backwaren", 4]
  - ["Gemuese", 4]
  - ["Suesswaren", 2]
hints:
  - kosten: 0
    text: |
      JOIN-Kette + COUNT(DISTINCT bestellung_id).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen pro Kategorie

Kategorie + Anzahl distinkter Bestellungen mit dieser Kategorie.
