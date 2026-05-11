SELECT k.name FROM kunden k LEFT JOIN bestellungen b ON b.kunde_id = k.id WHERE b.id IS NULL ORDER BY k.name;
