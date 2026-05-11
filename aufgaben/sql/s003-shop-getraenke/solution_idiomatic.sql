SELECT p.name, p.preis FROM produkte p
JOIN kategorien k ON p.kategorie_id = k.id
WHERE k.name = 'Getränke' AND p.preis < 2.0
ORDER BY p.id;
