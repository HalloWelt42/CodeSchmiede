---
schema_version: 1
id: s117-shop-status-zaehler-zeile
revision: 1
titel: "Shop: Anzahl Bestellungen + Anteil offen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [case, sum, prozent]
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
erwartete_spalten: ["gesamt", "offen", "anteil_offen"]
sortierung_egal: false
erwartetes_ergebnis:
  - [16, 3, 18.8]
hints:
  - kosten: 0
    text: |
      Conditional Aggregate plus Prozentrechnung.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anteil offener Bestellungen

Eine Zeile: Gesamtanzahl, Anzahl offen, Anteil offen in Prozent (1 Nachkommastelle).
