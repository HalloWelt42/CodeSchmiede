SELECT k.name, COUNT(*) AS anzahl FROM produkte p JOIN kategorien k ON p.kategorie_id = k.id GROUP BY k.id, k.name ORDER BY anzahl DESC, k.name;
