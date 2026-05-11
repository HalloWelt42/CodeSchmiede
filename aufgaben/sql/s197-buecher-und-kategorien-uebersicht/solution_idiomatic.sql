SELECT kategorie, COUNT(*) AS anzahl, ROUND(AVG(seiten), 1) AS schnitt_seiten, SUM(exemplare) AS exemplare FROM buecher GROUP BY kategorie ORDER BY anzahl DESC, kategorie;
