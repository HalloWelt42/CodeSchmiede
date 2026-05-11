SELECT kategorie, SUM(exemplare) AS gesamt FROM buecher GROUP BY kategorie ORDER BY gesamt DESC, kategorie;
