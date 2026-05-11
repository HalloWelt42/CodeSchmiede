SELECT k.name AS kategorie, ROUND(AVG(p.preis), 2) AS schnitt FROM produkte p JOIN kategorien k ON p.kategorie_id = k.id GROUP BY k.id, k.name ORDER BY schnitt DESC, k.name;
