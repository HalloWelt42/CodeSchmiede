SELECT titel, seiten, RANK() OVER (ORDER BY seiten DESC) AS rang FROM buecher ORDER BY rang, titel;
