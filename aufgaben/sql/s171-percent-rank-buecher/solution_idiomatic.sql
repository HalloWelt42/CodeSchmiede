SELECT titel, seiten, ROUND(PERCENT_RANK() OVER (ORDER BY seiten), 3) AS perc FROM buecher ORDER BY seiten, titel;
