---
schema_version: 1
id: s081-shop-marge-fiktiv
revision: 1
titel: "Shop: Lagerwert pro Produkt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [math, order, limit]
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
erwartete_spalten: ["name", "lagerwert"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Mineralwasser 6x1L", 748.5]
  - ["Vollmilch 1L", 516.0]
  - ["Butter 250g", 448.2]
  - ["Karotte 1kg", 447.0]
  - ["Schokolade 100g", 437.8]
  - ["Gouda Scheiben 200g", 394.8]
  - ["Cola 1L", 387.0]
  - ["Apfelsaft 1L", 378.0]
  - ["Kekse 200g", 373.5]
  - ["Erdbeeren 500g", 319.2]
hints:
  - kosten: 0
    text: |
      `preis * lager` ergibt den Lagerwert.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Top 10 Lagerwert

Name + Preis-mal-Lager als Lagerwert, hoechster zuerst (max 10 Zeilen).
