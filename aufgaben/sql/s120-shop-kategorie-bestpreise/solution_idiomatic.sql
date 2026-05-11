SELECT k.name AS kategorie, MIN(p.preis) AS min_preis, MAX(p.preis) AS max_preis FROM produkte p JOIN kategorien k ON p.kategorie_id = k.id GROUP BY k.id, k.name ORDER BY kategorie;
