SELECT titel, kategorie, ROW_NUMBER() OVER (PARTITION BY kategorie ORDER BY titel) AS nummer FROM buecher ORDER BY kategorie, nummer;
