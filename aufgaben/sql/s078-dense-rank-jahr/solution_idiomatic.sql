SELECT titel, jahr, DENSE_RANK() OVER (ORDER BY jahr) AS rang FROM buecher ORDER BY rang, titel;
