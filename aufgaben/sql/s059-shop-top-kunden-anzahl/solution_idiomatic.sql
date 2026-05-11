SELECT k.name, COUNT(*) AS anzahl_bestellungen FROM bestellungen b JOIN kunden k ON b.kunde_id = k.id GROUP BY k.id, k.name ORDER BY anzahl_bestellungen DESC, k.name LIMIT 5;
