---
schema_version: 1
id: s164-shop-paare-im-warenkorb
revision: 1
titel: "Shop: Produkt-Paare im Warenkorb"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 12
tags: [self-join, group-by, marktforschung]
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
erwartete_spalten: ["produkt_a", "produkt_b", "gemeinsam"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 9, 2]
  - [11, 16, 2]
  - [1, 10, 1]
  - [1, 13, 1]
  - [2, 17, 1]
  - [2, 19, 1]
  - [2, 20, 1]
  - [3, 7, 1]
  - [3, 17, 1]
  - [5, 6, 1]
hints:
  - kosten: 0
    text: |
      Self-JOIN auf bestellpositionen, JOIN-Bedingung: gleiche Bestellung, p1.id < p2.id.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Häufige Produkt-Paare

Welche Produkt-Paare landen oft zusammen in einer Bestellung? Top 10.
