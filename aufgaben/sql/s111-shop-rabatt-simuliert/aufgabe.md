---
schema_version: 1
id: s111-shop-rabatt-simuliert
revision: 1
titel: "Shop: 10% Rabatt simulieren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [math, where, round]
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
erwartete_spalten: ["name", "preis", "rabattpreis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Mineralwasser 6x1L", 4.99, 4.49]
  - ["Erdbeeren 500g", 3.99, 3.59]
  - ["Gouda Scheiben 200g", 3.29, 2.96]
  - ["Brot Roggen 500g", 2.79, 2.51]
  - ["Butter 250g", 2.49, 2.24]
  - ["Kekse 200g", 2.49, 2.24]
hints:
  - kosten: 0
    text: |
      `preis * 0.9` plus `ROUND(..., 2)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# 10% Rabatt simulieren

Produkte ab 2 EUR -- Name, Originalpreis, neuer Preis nach 10% Rabatt (auf 2 Stellen).
