SELECT kategorie, COUNT(*) AS anzahl FROM buecher GROUP BY kategorie HAVING COUNT(*) >= 3 ORDER BY anzahl DESC, kategorie;
