SELECT titel, jahr, LEAD(jahr) OVER (ORDER BY jahr, titel) AS naechstes FROM buecher ORDER BY jahr, titel;
