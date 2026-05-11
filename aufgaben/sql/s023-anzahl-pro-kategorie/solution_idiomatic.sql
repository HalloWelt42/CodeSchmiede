SELECT kategorie, COUNT(*) AS anzahl FROM buecher GROUP BY kategorie ORDER BY anzahl DESC, kategorie;
