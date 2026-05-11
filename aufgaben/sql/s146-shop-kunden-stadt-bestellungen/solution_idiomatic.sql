SELECT k.ort, COUNT(*) AS bestellungen FROM bestellungen b JOIN kunden k ON b.kunde_id = k.id GROUP BY k.ort ORDER BY bestellungen DESC, k.ort;
