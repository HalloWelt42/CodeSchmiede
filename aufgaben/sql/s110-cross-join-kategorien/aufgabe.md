---
schema_version: 1
id: s110-cross-join-kategorien
revision: 1
titel: "CROSS JOIN: Kategorie-Paare"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [cross-join]
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
erwartete_spalten: ["a", "b"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Backwaren", "Getraenke"]
  - ["Backwaren", "Suesswaren"]
  - ["Gemuese", "Backwaren"]
  - ["Gemuese", "Getraenke"]
  - ["Gemuese", "Milchprodukte"]
  - ["Gemuese", "Suesswaren"]
  - ["Getraenke", "Suesswaren"]
  - ["Milchprodukte", "Backwaren"]
  - ["Milchprodukte", "Getraenke"]
  - ["Milchprodukte", "Suesswaren"]
  - ["Obst", "Backwaren"]
  - ["Obst", "Gemuese"]
  - ["Obst", "Getraenke"]
  - ["Obst", "Milchprodukte"]
  - ["Obst", "Suesswaren"]
hints:
  - kosten: 0
    text: |
      CROSS JOIN kombiniert jedes Paar. WHERE k1.id < k2.id vermeidet Duplikate.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kategorie-Paare

Alle Paare verschiedener Kategorien (jedes Paar nur einmal), alphabetisch sortiert.
