SELECT k.name, COUNT(*) AS bestellungen FROM bestellungen b JOIN kunden k ON b.kunde_id = k.id GROUP BY k.id, k.name HAVING COUNT(*) > 1 ORDER BY bestellungen DESC, k.name;
