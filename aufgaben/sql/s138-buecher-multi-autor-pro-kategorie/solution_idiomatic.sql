SELECT kategorie, COUNT(DISTINCT autor_id) AS autoren FROM buecher GROUP BY kategorie ORDER BY autoren DESC, kategorie;
