SELECT kategorie, MIN(jahr) AS frueh, MAX(jahr) AS spaet, MAX(jahr) - MIN(jahr) AS spanne FROM buecher GROUP BY kategorie ORDER BY spanne DESC, kategorie;
