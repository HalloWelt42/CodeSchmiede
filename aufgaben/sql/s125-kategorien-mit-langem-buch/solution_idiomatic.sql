SELECT kategorie, MAX(seiten) AS max_seiten FROM buecher GROUP BY kategorie HAVING MAX(seiten) > 500 ORDER BY max_seiten DESC, kategorie;
