---
schema_version: 1
id: s119-shop-top-produkte-pro-kunde
revision: 1
titel: "Shop: meistbestelltes Produkt pro Kunde"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 15
tags: [cte, window-function, top-per-group]
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
erwartete_spalten: ["kunde", "produkt", "menge"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Alex Becker", "Apfel Boskoop", 6]
  - ["Frank Berger", "Tomate Strauch", 6]
  - ["Jan Petersen", "Banane", 6]
  - ["Carla Diaz", "Banane", 5]
  - ["Beate Frank", "Tomate Strauch", 4]
  - ["Daniel Engel", "Croissant", 4]
  - ["Elena Vogel", "Apfel Boskoop", 4]
  - ["Gisela Hahn", "Gouda Scheiben 200g", 3]
  - ["Hugo Meier", "Cola 1L", 2]
  - ["Iris Schaefer", "Erdbeeren 500g", 2]
  - ["Karin Berger", "Mineralwasser 6x1L", 2]
  - ["Leon Wolf", "Brokkoli", 1]
hints:
  - kosten: 0
    text: |
      CTE: pro Kunde+Produkt aggregierte Menge + ROW_NUMBER nach Menge. Aussen WHERE rn = 1.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Top-Produkt pro Kunde

Fuer jeden Kunden: das Produkt, von dem er am meisten bestellt hat (mit Stueckzahl).
