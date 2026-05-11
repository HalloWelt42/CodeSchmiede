SELECT p.name, p.preis, ROUND(AVG(p.preis) OVER (PARTITION BY p.kategorie_id), 2) AS kat_schnitt FROM produkte p ORDER BY p.kategorie_id, p.name;
