SELECT titel, seiten, CASE   WHEN seiten < 200 THEN 'duenn'   WHEN seiten < 500 THEN 'mittel'   ELSE 'dick' END AS dicke FROM buecher ORDER BY seiten, titel;
