SELECT kategorie, COUNT(*) AS anzahl, ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM buecher), 1) AS prozent FROM buecher GROUP BY kategorie ORDER BY anzahl DESC, kategorie;
