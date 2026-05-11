SELECT titel, seiten, NTILE(4) OVER (ORDER BY seiten) AS quartil FROM buecher ORDER BY seiten, titel;
