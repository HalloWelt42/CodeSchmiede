SELECT titel, seiten FROM buecher WHERE kategorie = 'Roman' AND seiten BETWEEN 200 AND 500 ORDER BY seiten, titel;
