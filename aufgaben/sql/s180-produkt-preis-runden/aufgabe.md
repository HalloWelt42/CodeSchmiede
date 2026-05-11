---
schema_version: 1
id: s180-produkt-preis-runden
revision: 1
titel: "Shop: Preise auf 0.10 abrunden"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [math, round]
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
erwartete_spalten: ["name", "preis", "rund_zehn"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", 0.45, 0.5]
  - ["Apfelsaft 1L", 1.89, 1.9]
  - ["Banane", 0.3, 0.3]
  - ["Brokkoli", 1.99, 2.0]
  - ["Brot Roggen 500g", 2.79, 2.8]
  - ["Brötchen 5er-Pack", 1.49, 1.5]
  - ["Butter 250g", 2.49, 2.5]
  - ["Cola 1L", 1.29, 1.3]
  - ["Croissant", 0.99, 1.0]
  - ["Erdbeeren 500g", 3.99, 4.0]
  - ["Gouda Scheiben 200g", 3.29, 3.3]
  - ["Gurke", 1.2, 1.2]
  - ["Joghurt Natur 500g", 0.89, 0.9]
  - ["Karotte 1kg", 1.49, 1.5]
  - ["Kekse 200g", 2.49, 2.5]
  - ["Mineralwasser 6x1L", 4.99, 5.0]
  - ["Orange Navel", 0.55, 0.6]
  - ["Schokolade 100g", 1.99, 2.0]
  - ["Tomate Strauch", 0.65, 0.7]
  - ["Vollmilch 1L", 1.29, 1.3]
hints:
  - kosten: 0
    text: |
      ROUND(preis * 10) / 10.0 rundet auf 0.10.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Auf 0.10 abrunden

Name + Originalpreis + auf 10 Cent gerundeter Preis.
